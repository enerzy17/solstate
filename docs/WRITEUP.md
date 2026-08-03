# Write-up

The brief asks for a short document covering the data sources and how they are
integrated, the automation strategy, any anomaly detection, and setup
instructions. This is that document.

---

## 1. Data sources and how they are integrated

Every source below was fetched successfully from a clean machine, with no
account and no key, before it was written into the code. One candidate feed
(`blog.superteam.fun/rss`) returned 404 during that check and was removed rather
than shipped, because a dead feed makes a news panel look maintained when it is
not.

### Solana JSON-RPC (primary)

| Method | Used for |
| --- | --- |
| `getHealth` | cluster health, and the highest-severity anomaly rule |
| `getEpochInfo` | epoch, slot index, slots in epoch, block height, absolute slot, lifetime transaction count |
| `getRecentPerformanceSamples` | TPS, non-vote TPS, 30-sample mean, slot time |
| `getSlot` + `getBlockTime` | block lag against wall clock |
| `getVoteAccounts` | the entire validator section |
| `getSupply` | circulating, non-circulating and total SOL |

Endpoints are **rotated, not pinned**. `net.JsonClient.rpc` walks a list of four
public RPCs, retrying with exponential backoff on 429 and 503 and moving to the
next host on anything else. This is the single most important resilience
decision in the project: public RPCs rate-limit aggressively, and a hard-coded
URL is the usual reason a dashboard like this works on the author's laptop and
is dead a week later.

Two derived figures are worth calling out because they are computed here rather
than read from anywhere:

- **Non-vote TPS.** Raw TPS is dominated by consensus vote transactions. The
  report shows both and labels which is which, because quoting the raw number
  alone overstates real throughput by roughly 2x.
- **Nakamoto coefficient.** The smallest number of validators whose combined
  active stake exceeds one third of the total, i.e. the smallest group that
  could halt the chain. Computed by sorting the active set by stake and walking
  it. In the captured sample run this was 18.

### Off-chain, key-free

| Source | Endpoint | Provides |
| --- | --- | --- |
| CoinGecko | `/api/v3/coins/solana` | SOL price, 24h/7d/30d change, market cap, FDV, spot volume, ATH |
| DeFiLlama | `/v2/historicalChainTvl/Solana` | TVL now, 24h/7d/30d change, and 90 days of series for the sparkline |
| DeFiLlama | `stablecoins.llama.fi/stablecoinchains` | stablecoin supply on Solana, by peg type |
| DeFiLlama | `/overview/dexs/solana` | DEX volume 24h and 7d, 24h change, protocol count |
| DeFiLlama | `/overview/fees/solana` | chain fees, used as the REV proxy |

### Feeds

`solana.com/news/rss.xml`, the Agave releases atom feed, and the
solana-improvement-documents commit atom feed. Parsed with `xml.etree` from the
standard library, handling both RSS 2.0 and Atom element names. SIMD identifiers
are extracted from titles and summaries by regex, which is how the report picks
up **SIMD-0525** and its neighbours live rather than from a hard-coded list.

### Dune (optional)

The brief lists Dune first among data sources and also prefers no API keys.
Both are honoured by making Dune purely additive. With no key, `sources/dune.py`
returns a note explaining what is skipped and the report's **Not collected**
section names the affected metrics. With a key and one or more query ids, it
reads cached results via `/query/{id}/results`, which spends no execution
credits.

### What is deliberately not collected

Declared in `sources/market.py::UNAVAILABLE_WITHOUT_KEY` and rendered in all
three outputs:

- **Daily active addresses** — no key-free public endpoint; available via Dune.
- **Tokenized equity volume** — issuer-level breakdown needs Dune or a vendor.
- **MEV tips** — needs the Jito API, which would break the key-free property.

Naming these was a choice. The alternative, quietly omitting them, would make
the report look more complete than it is.

---

## 2. Automation strategy

**Three layers, each degrading safely into the one below.**

1. **`--watch`** refreshes on a configurable interval in-process. A failed
   refresh is caught, logged to stderr and does not break the loop; the previous
   good outputs stay on disk and the next cycle retries. A crash-on-error loop
   would leave a dashboard permanently stale after one transient 429.

2. **GitHub Actions** (`.github/workflows/report.yml`) runs on cron, commits the
   refreshed outputs back to the repository, and deploys `out/` to GitHub Pages.
   This is the hosted live demo. It configures **no secrets**, which is only
   possible because of the key-free constraint.

3. **The sqlite history is cached between Actions runs.** Without this the
   baseline resets every run and statistical detection never activates. With it,
   the anomaly engine gets progressively better the longer the workflow has been
   running.

**Atomic writes.** Each output is written to `name.tmp` and then `os.replace`d.
A reader, or Pages mid-deploy, never sees a half-written dashboard.

**One canonical object.** `report.build()` returns a single dict; the JSON,
Markdown and HTML renderers are pure functions of it. Three outputs that are
generated independently drift apart, and the drift is invisible until someone
compares them. This makes disagreement structurally impossible.

---

## 3. Anomaly detection

### Rules — for failures that can be named in advance

| Check | Threshold | Severity |
| --- | --- | --- |
| `getHealth` not `ok` | any | critical |
| TPS below trailing median | −40% | critical |
| TPS above trailing median | +80% | info |
| Slot time | > 800ms (target 400ms) | warning |
| Delinquent stake | > 5% / > 10% | warning / critical |
| Block lag vs wall clock | > 60s | warning |
| TVL 24h move | ±15% | warning |
| SOL price 24h move | ±12% | warning |
| Validator count or Nakamoto drop | −10% vs median | warning |

### Statistics — for everything else

Every scalar metric is scored against its own stored history:

```
robust_z = 0.6745 * (x - median(history)) / MAD(history)
```

`MAD` is the median absolute deviation; `0.6745` is the 75th percentile of the
standard normal, which rescales MAD so the cutoff is comparable to a
conventional z-score. The default cutoff is 3.5.

**Why MAD and not standard deviation.** Chain metrics are spiky and
heavy-tailed. A single outage or a single RPC glitch inflates a standard
deviation enough to hide the next several genuine anomalies. MAD has a breakdown
point of 50%: half the history can be garbage and the estimate still holds.
`tests/test_anomaly.py::test_mad_ignores_a_single_wild_outlier` demonstrates the
difference directly — one outlier moves `pstdev` by over 100x while MAD and the
median barely move.

### Two design details that matter

- **Statistical detection stays off below 8 stored runs**, and both the
  Markdown and HTML say so explicitly. Reporting deviations against a
  three-point "baseline" would be noise wearing a lab coat.
- **A rule suppresses the duplicate statistical finding** for the same metric,
  so a TPS collapse is reported once, with the rule's clearer message, not twice.

Findings sort worst-first and carry the metric, severity, kind (`rule` or
`statistical`), the value, the baseline, and the z-score where one applies.

### Calibration against live mainnet, and what it changed

The detector was run repeatedly against mainnet while building, which surfaced
three failure modes that no amount of unit testing would have found. All three
are fixed, and each fix has a regression test.

**1. Monotonic counters produced a critical finding on every single run.**
`block_height`, `absolute_slot`, `block_time_unix`, `transaction_count` and
`epoch` only ever increase, so they are permanently far from their own trailing
median. The first run with 8 points of history emitted five criticals, all
meaningless. `epoch_progress_pct` and `epoch_remaining_seconds_est` are worse:
they sawtooth, screaming at both ends of every epoch.

Fixed by excluding both classes from z-scoring (`MONOTONIC`, `CYCLIC` in
`anomaly.py`) and monitoring them the way counters should be monitored instead:
**a counter that goes backwards** means the endpoint served stale or forked
data, and **a block height that has not advanced since the last run** means the
cluster or the endpoint is stalled. Both are critical, both are invisible to any
z-score, and both are genuinely worth waking up for.

**2. Stable metrics scored enormous z on trivial moves.** `sol_total_supply`
barely changes between runs minutes apart, so its MAD collapses to near zero and
a rounding-error change scored z=10. `sol_volume_24h_usd` scored z=95 on a move
nobody would notice. The original code made this worse by inventing a fallback
value when MAD was exactly zero.

Fixed twice over: `robust_z` now returns `None` on zero dispersion rather than
manufacturing a number, and a statistical finding must also clear a **minimum
relative move** (`min_rel_change`, default 5%). Statistical significance is not
practical significance, and a panel full of arithmetically-true noise trains the
reader to ignore it.

**3. Statistical findings were claiming `critical`.** Solana TPS genuinely
swings 40% or more between one-minute samples. That is worth a glance, not an
alarm. A z-score knows a value is unusual against its own history; it does not
know anything is *wrong*.

Fixed by capping statistical findings at `warning`. **Only rules may say
critical**, because only rules encode domain knowledge about what bad actually
looks like.

After these three, a live run against mainnet reports `0 critical, 1 warning`,
and the one warning is a real 70% relative move in the 7-day price change. That
is the behaviour to want: quiet by default, loud when it matters.

---

## 4. Setup

Requires Python 3.9+. Nothing else.

```bash
git clone <this repo>
cd solstate
python -m solstate
open out/index.html          # or: python -m solstate --serve 8080
```

Continuous local operation:

```bash
python -m solstate --watch --interval 900
```

Hosted: fork, enable GitHub Pages with source "GitHub Actions", and enable
workflows. The schedule in `.github/workflows/report.yml` takes over. No secrets
to configure.

Optional Dune enrichment:

```bash
export SOLSTATE_DUNE_API_KEY=...
python -m solstate --dune-query 1234567
```

Tests:

```bash
python -m unittest discover -s tests
```

---

## 5. Honest limitations

- **The REV figure is a proxy**, specifically DeFiLlama's Solana chain fees over
  24h. There is no canonical key-free REV series. It is labelled as a proxy in
  the JSON (`rev_proxy_basis`), the Markdown and the dashboard.
- **Epoch time remaining is an estimate** derived from the 400ms target slot
  time, not a measurement, and is labelled "est." everywhere.
- **News is feed-scoped.** Three feeds is not the whole ecosystem conversation.
  Twitter/X sentiment is not included because doing it properly needs an API key
  and doing it improperly means scraping.
- **The Nakamoto coefficient counts validators, not operators.** One operator
  running several validators is counted several times, so the true figure is
  likely lower than reported. This is a limitation of `getVoteAccounts`, which
  has no operator identity.
- **A first run has no baseline.** Statistical detection needs history, and
  history needs runs. The hosted workflow with a cached database is the intended
  way to accumulate it.
