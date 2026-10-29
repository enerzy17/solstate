# Solana Ecosystem State Report

Generated **2026-10-29T13:12:42Z** in 19.6s across 17 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 92.9% (13/14 probes returned data). History depth: 138 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1705 is 63% below the trailing median of 4552.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 5.4 robust deviations from its 138-point median of 8, a 100.0% move.
- [WARNING] **delinquent_pct_by_count** (statistical) - delinquent_pct_by_count is 4.2 robust deviations from its 138-point median of 1.616, a 115.5% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 22.5 robust deviations from its 138-point median of 0.02535, a 3020.7% move.
- [WARNING] **tps_avg_30_samples** (statistical) - tps_avg_30_samples is 3.6 robust deviations from its 138-point median of 4550, a 62.3% move.
- [WARNING] **validators_delinquent** (statistical) - validators_delinquent is 4.4 robust deviations from its 138-point median of 11, a 118.2% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,071 |
| Epoch progress | 51.25% |
| Epoch time remaining (est.) | 23h 24m |
| Absolute slot | 462,893,385 |
| Block height | 440,916,811 |
| TPS (all) | 1,704.97 |
| TPS (non-vote) | 1,704.97 |
| TPS (30-sample mean) | 1,713.88 |
| Slot time | 215.10 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 564,288,431,691 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 665 |
| Delinquent | 24 |
| Delinquent share of stake | 0.79% |
| Total active stake | 436.78M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.53% |
| Stake in top 20 | 35.80% |
| Stake in top 50 | 55.52% |
| Median commission | 5.00% |
| Validators at 0% commission | 227 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.03M | 3.90% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.67M | 3.82% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.88M | 2.95% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.76M | 2.46% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.71M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.47M | 2.17% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.22M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.76M | 1.78% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.65M | 1.52% | 5.00% |
| 11 | `JD549HsbJHeE...` | 6.60M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.11M | 1.40% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.72M | 1.31% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `722RdWmHC5TG...` | 1.53M | 462,239,999 |
| `BXAxLMMMUNYf...` | 794.31K | 462,239,999 |
| `7cVfgArCheMR...` | 792.80K | 462,239,999 |
| `9GHvMeJ4ZWuA...` | 234.50K | 462,891,015 |
| `2dfgsiSaZ51Q...` | 83.87K | 462,239,999 |
| `LwXL9d7Ug3fY...` | 20.45K | 0 |
| `HzrEstnLfzsi...` | 2.61K | 461,807,999 |
| `JDvwML44fiV2...` | 290.16 | 0 |
| `Bi9kKNxfW2Xq...` | 63.43 | 462,464,506 |
| `9Ukj3PkyD3ig...` | 2.45 | 408,332,659 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $100.52 |
| SOL 24h | -0.78% |
| SOL 7d | -3.63% |
| SOL 30d | -16.80% |
| Market cap | $59.31B |
| Spot volume 24h | $2.82B |
| Circulating supply | 589.98M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.62B |
| TVL 24h | -1.21% |
| TVL 7d | -5.67% |
| Stablecoin supply | $15.42B |
| DEX volume 24h | $1.73B |
| DEX volume 7d | $12.30B |
| Chain fees 24h (REV proxy) | $10.35M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0123, SIMD-0607, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0529, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464

## Ecosystem news

- [Release v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0)
- [Mark SIMDs as Activated (#710)](https://github.com/solana-foundation/solana-improvement-documents/commit/6cc17538e26601e65beca89bbfa761e755720956)
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate prec…](https://github.com/solana-foundation/solana-improvement-documents/commit/2934dbeb1c8a7dfecc4f70a93a6b152e525b1698)
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

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
