# Solana Ecosystem State Report

Generated **2026-10-28T16:41:57Z** in 16.8s across 17 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 92.9% (13/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1951 is 57% below the trailing median of 4562.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 4.7 robust deviations from its 141-point median of 8, a 87.5% move.
- [WARNING] **delinquent_pct_by_count** (statistical) - delinquent_pct_by_count is 6.5 robust deviations from its 141-point median of 1.613, a 178.2% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 31.0 robust deviations from its 141-point median of 0.0212, a 4117.5% move.
- [WARNING] **validators_delinquent** (statistical) - validators_delinquent is 6.7 robust deviations from its 141-point median of 11, a 181.8% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,070 |
| Epoch progress | 71.23% |
| Epoch time remaining (est.) | 13h 48m |
| Absolute slot | 462,547,725 |
| Block height | 440,572,196 |
| TPS (all) | 1,950.73 |
| TPS (non-vote) | 1,950.73 |
| TPS (30-sample mean) | 2,118.65 |
| Slot time | 212.80 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 564,166,852,844 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 660 |
| Delinquent | 31 |
| Delinquent share of stake | 0.89% |
| Total active stake | 437.29M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.57% |
| Stake in top 20 | 35.70% |
| Stake in top 50 | 55.35% |
| Median commission | 5.00% |
| Validators at 0% commission | 227 |
| Validators at 100% commission | 64 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.01M | 3.89% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.66M | 3.81% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.79M | 2.93% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.82M | 2.47% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.46M | 2.16% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.21M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.76M | 1.77% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 11 | `5pPRHniefFjk...` | 6.11M | 1.40% | 5.00% |
| 12 | `JD549HsbJHeE...` | 6.05M | 1.38% | 0.00% |
| 13 | `5Cchr1XGEg7d...` | 5.71M | 1.31% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.73M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `722RdWmHC5TG...` | 1.56M | 462,239,999 |
| `7cVfgArCheMR...` | 1.19M | 462,239,999 |
| `BXAxLMMMUNYf...` | 794.31K | 462,239,999 |
| `2dfgsiSaZ51Q...` | 292.98K | 462,239,999 |
| `ssx2rHZNVy6J...` | 35.70K | 462,239,999 |
| `7d7x84jiVtqp...` | 35.43K | 462,546,962 |
| `HzrEstnLfzsi...` | 2.61K | 461,807,999 |
| `GqDCbnafLmKk...` | 397.56 | 460,079,999 |
| `JDvwML44fiV2...` | 290.16 | 0 |
| `SANDCxXBbQhv...` | 181.00 | 460,079,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $100.94 |
| SOL 24h | -0.03% |
| SOL 7d | -6.91% |
| SOL 30d | -14.96% |
| Market cap | $59.53B |
| Spot volume 24h | $2.06B |
| Circulating supply | 589.93M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.71B |
| TVL 24h | 0.87% |
| TVL 7d | -4.22% |
| Stablecoin supply | $15.16B |
| DEX volume 24h | $1.58B |
| DEX volume 7d | $12.83B |
| Chain fees 24h (REV proxy) | $10.91M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0123, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0529, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215

## Ecosystem news

- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4)
- [v4.5.0-alpha.3: Bump version to 4.5.0-alpha.3 (#16402)](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.3)
- [SIMD-0690: Hash validation in program migrations and upgrades (#690)](https://github.com/solana-foundation/solana-improvement-documents/commit/eac20f2994dd064482d96f178a4bbc0f4e358fd0)
- [SIMD-0670: ABIv1 invoke signed v2 syscall (#670)](https://github.com/solana-foundation/solana-improvement-documents/commit/c9ec366af14dd32a74259f5d9f5772249188bd25)
- [v4.4.0-rc.0: Bump version to 4.4.0-rc.0 (#16364)](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0)
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5 (#683)](https://github.com/solana-foundation/solana-improvement-documents/commit/a084840a512454a7ee5e2ef8dd736c790102bea0)
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp…](https://github.com/solana-foundation/solana-improvement-documents/commit/51dbb649da0233481cc40f5640f33fe74d6dbffe)
- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2)
- [SIMD-0648: Unbound LoaderV3 Instruction Data (#648)](https://github.com/solana-foundation/solana-improvement-documents/commit/27ff5a704391d121869dd3bc8cfa8127483329d0)
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 sy…](https://github.com/solana-foundation/solana-improvement-documents/commit/f13f5d657ccae32cb19cae84ccb6c781cd125ad7)
- [simd-0504: remove identical signature requirement (#593)](https://github.com/solana-foundation/solana-improvement-documents/commit/33c75cffdeb38468989313c6381c179a541808f1)
- [SIMD-0686: Single Program Runtime Environment (#688)](https://github.com/solana-foundation/solana-improvement-documents/commit/749dc8635821383c5c259d616e337687707f3ef9)
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData (#684)](https://github.com/solana-foundation/solana-improvement-documents/commit/f24b888c352c115f08438ebdb57f5bba46136745)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
