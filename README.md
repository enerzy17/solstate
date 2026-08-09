# solstate

**An auto-updating report on the state of the Solana ecosystem.** One command
produces three outputs from the same data: an interactive HTML dashboard, a
human-readable Markdown report, and machine-readable JSON.

```bash
git clone <this repo> && cd solstate
python -m solstate
```

That is the entire setup. No `pip install`, no `requirements.txt`, no `.env`, no
account to register, no API key to paste. Python 3.9 or newer and a network
connection.

```bash
python -m solstate                 # one run -> out/index.html, report.md, report.json
python -m solstate --watch         # refresh forever, default every 30 minutes
python -m solstate --interval 900  # every 15 minutes instead
python -m solstate --serve 8080    # run, then serve out/ at http://127.0.0.1:8080
python -m unittest discover -s tests
```

## See it without running it

The workflow here regenerates all three outputs on a schedule and commits them,
so the copies in `out/` are current and the commit history is the audit trail of
the chain rather than a claim about it.

| where | what it is |
| --- | --- |
| **[Latest report](out/report.md)** | GitHub renders this itself. No third party sits between you and it, so this link cannot rot. |
| [Interactive dashboard](https://raw.githack.com/enerzy17/solstate/main/out/index.html) | the committed `out/index.html`, served through a third party CDN because there is no Pages URL yet |
| [Raw JSON](out/report.json) | every figure, each with the endpoint it came from |
| [Refresh history](https://github.com/enerzy17/solstate/commits/main/out/report.md) | what changed, run by run, timestamped by GitHub |

There is no `github.io` URL yet, and that is a permissions fact rather than a
bug: GitHub does not let `GITHUB_TOKEN` create a Pages site that has never
existed, so `actions/configure-pages` cannot succeed no matter how often it
runs. It takes one manual action, in Settings, Pages, Source, GitHub Actions.
Until then the workflow skips the deploy, prints a warning annotation saying so,
and stays green on the work it actually did.

---

## The two constraints that shaped this

The brief said solutions needing **no API keys and no dependencies beyond the
standard library and Solana RPC** are preferred. Rather than treat that as a
nice-to-have, it was treated as the hard constraint, and it drove every design
decision below.

**Zero dependencies.** The whole project imports only `urllib`, `json`,
`sqlite3`, `xml.etree`, `http.server`, `argparse`, `dataclasses` and friends.
There is no lockfile to rot, no transitive CVE to patch, and no build step. It
will still run unchanged on a clean Python install in five years.

**Zero keys for everything published.** Every number in the report comes from a
public unauthenticated endpoint. Dune is supported but strictly optional and
strictly additive: with no key the report is complete and says plainly which
metrics are missing; with a key those metrics fill in. Nothing degrades into a
silent blank.

## The third constraint, which was self-imposed

**A missing number is never replaced by a plausible one.**

This is the part worth arguing for. A dashboard's real failure mode is not
crashing, it is confidently displaying a stale or invented figure that a reader
then acts on. So:

- Every probe records `status`, `source`, `latency_ms` and `fetched_at`, and all
  of them are published in the **Probe log** at the bottom of the dashboard.
- A source that is down renders as `unavailable`, never as `0` and never as the
  last known value silently reused.
- The header carries a **data completeness percentage**, so a half-broken run
  cannot look like a healthy one at a glance.
- Metrics that genuinely need a paid or keyed source (daily active addresses,
  issuer-level tokenized-equity volume, Jito MEV tips) are listed by name in a
  **Not collected** section with the reason. A named gap can be reasoned about;
  a silent omission cannot.
- The REV figure is labelled a proxy everywhere it appears, because there is no
  canonical key-free REV series and pretending otherwise would be the exact
  failure this section exists to prevent.

## What it reports

| Area | Metrics |
| --- | --- |
| Network | cluster health, TPS (all and non-vote), 30-sample mean TPS, slot time, block height, absolute slot, epoch and progress with estimated time remaining, block lag vs wall clock, lifetime transaction count |
| Validators | active and delinquent counts, delinquency by count and by stake, total active stake, **Nakamoto coefficient**, stake concentration in top 10/20/50, median commission, count at 0% and 100%, ranked table of the largest validators, and the largest delinquent ones by stake |
| Economics | SOL price with 24h/7d/30d change, market cap, FDV, spot volume, circulating vs total supply, DeFi TVL with 24h/7d/30d change, stablecoin supply broken down by peg type, DEX volume, chain fees as a REV proxy |
| Ecosystem | release and SIMD feeds, SIMDs referenced in the current window (SIMD-0525 among them), tracked upgrades including Alpenglow and Firedancer, recent news |
| Meta | probe-level status and latency, data completeness, history depth, run duration, HTTP call count |

## Anomaly detection

Two halves, because one is not enough.

**Rules** cover the failures we can already name: cluster health not `ok`, TPS
collapsing below the trailing median, slot times above 800ms against a 400ms
target, delinquent stake over 5%, block lag over 60s, TVL or SOL price moving
beyond a configured band, and a validator set or Nakamoto coefficient that drops
sharply.

**Statistics** cover the rest. Every scalar is scored against its own history
using a **median absolute deviation** robust z-score:

```
robust_z = 0.6745 * (x - median) / MAD
```

MAD rather than standard deviation is a deliberate choice. Chain metrics are
spiky and heavy-tailed, and a single outage inflates a standard deviation enough
to mask the next three outages. MAD has a 50% breakdown point, so half the
history can be garbage and the baseline still holds. There is a unit test that
demonstrates exactly this: one outlier moves `pstdev` by more than 100x while
leaving MAD and the median essentially unchanged.

Statistical detection stays switched off until at least 8 runs are stored, and
the report says so rather than implying a baseline it does not have. A rule and
a statistical check never double-report the same metric.

**Statistical findings are capped at `warning`.** Only rules may say `critical`,
because only rules encode domain knowledge about what "bad" means. A z-score
knows a value is unusual against its own history; it does not know anything is
wrong, and Solana TPS genuinely swings 40% between samples.

Three further calibrations came from running this against mainnet rather than
from theory: monotonic counters are excluded from z-scoring (and monitored for
stalls and backwards jumps instead), zero-dispersion history returns no z-score
rather than an invented one, and a statistical hit must also clear a minimum
relative move. Each has a regression test; the reasoning is in
[`docs/WRITEUP.md`](docs/WRITEUP.md#calibration-against-live-mainnet-and-what-it-changed).

## Automation

**Local.** `--watch` refreshes on `--interval` and never dies on a failed
refresh; the last good dashboard stays in place and the next cycle retries.

**Hosted.** `.github/workflows/report.yml` runs on a cron schedule, commits the
refreshed outputs, and publishes `out/` to GitHub Pages. The history database is
cached between runs, which is what lets anomaly detection accumulate a real
baseline instead of restarting cold every time. No secrets are configured on the
workflow, because none are needed.

**Resilience.** Public Solana RPCs rate-limit hard, so endpoints are rotated on
failure rather than pinned; a single hard-coded URL is the most common reason a
project like this quietly stops updating a week after it is judged. Outputs are
written to a temp file and atomically replaced, so a reader or GitHub Pages
never sees a half-written page.

## The dashboard

`out/index.html` is a **single self-contained file**. No CDN, no external
stylesheet, no webfont, no image request, no analytics. It renders identically
from `file://`, from GitHub Pages, and on an air-gapped machine. Dark theme,
responsive, with sortable tables, a validator filter, an anomaly severity
filter, a live "generated N minutes ago" counter that turns amber when the page
is stale, and SVG sparklines drawn from the real sqlite history.

Sparklines only appear once there are at least three real datapoints. An empty
chart that implies data is worse than no chart.

## Layout

```
solstate/
  __main__.py      CLI
  config.py        dataclass config, env and flag overrides
  net.py           urllib client, retries, RPC endpoint rotation, Fetched result type
  report.py        assembles the one canonical report dict
  history.py       sqlite time-series store
  anomaly.py       rules + MAD robust z-scores
  sources/         chain.py  market.py  ecosystem.py  dune.py
  render/          html.py  markdown.py  json_out.py
tests/             37 unittest cases, standard library only
samples/           a real captured run of all three outputs
docs/WRITEUP.md    data sources, automation strategy, anomaly design
```

The three renderers are **pure functions of one report dict**, so the HTML,
Markdown and JSON cannot disagree with each other. Two outputs drifting apart is
easy to ship and hard to notice.

## Configuration

Nothing is required. Everything is overridable by flag or environment variable:

| Flag | Env | Default |
| --- | --- | --- |
| `--interval` | `SOLSTATE_INTERVAL` | 1800 |
| `--out` | `SOLSTATE_OUT_DIR` | `out` |
| `--rpc` (repeatable) | `SOLSTATE_RPCS` (comma separated) | 4 public endpoints |
| `--validators` | `SOLSTATE_VALIDATOR_SAMPLE` | 25 |
| `--dune-key` | `SOLSTATE_DUNE_API_KEY` | unset, Dune skipped |
| `--dune-query` (repeatable) | | none |
| `--no-history` | | history on |

## Sample run

A real run captured while building this, against Solana mainnet:

```
[solstate] 2026-08-03T22:57:38Z  14/14 probes ok (100.0%)  15 calls  12.6s  anomalies: 0C/0W/0I
```

Epoch 1011 at 71% complete, 3,287 TPS (1,695 non-vote), 419.6ms slot time,
691 active validators with 12 delinquent holding 0.13% of stake, Nakamoto
coefficient 18. Full captured outputs are in [`samples/`](samples/).

## Tests

```bash
python -m unittest discover -s tests
```

37 cases covering the statistics (including the MAD-vs-stdev robustness
property), every anomaly rule, rule/statistical de-duplication, history
round-trip and pruning, renderer behaviour on empty and hostile input, HTML
escaping, the no-external-resources guarantee, and the table scroll-container
invariant.

## Licence

MIT. See [LICENSE](LICENSE).

## Notes

Built for the Superteam Canada bounty *Develop Solana Ecosystem Auto-Updating
Report & Interactive Dashboard*. Written with AI assistance; the design
decisions, the source verification and the constraints above are the author's,
and every endpoint used here was checked live before it was relied on.
