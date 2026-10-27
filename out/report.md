# Solana Ecosystem State Report

Generated **2026-10-27T07:58:11Z** in 9.5s across 15 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 100.0% (14/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1079 is 76% below the trailing median of 4572.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 5.4 robust deviations from its 141-point median of 8, a 100.0% move.
- [WARNING] **tps_avg_30_samples** (statistical) - tps_avg_30_samples is 5.1 robust deviations from its 141-point median of 4569, a 74.2% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,069 |
| Epoch progress | 43.11% |
| Epoch time remaining (est.) | 27h 18m |
| Absolute slot | 461,994,256 |
| Block height | 440,020,046 |
| TPS (all) | 1,078.53 |
| TPS (non-vote) | 1,078.53 |
| TPS (30-sample mean) | 1,179.95 |
| Slot time | 209.80 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 563,960,481,527 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 665 |
| Delinquent | 20 |
| Delinquent share of stake | 0.09% |
| Total active stake | 436.87M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.58% |
| Stake in top 20 | 35.67% |
| Stake in top 50 | 55.34% |
| Median commission | 5.00% |
| Validators at 0% commission | 230 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.06M | 3.90% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.64M | 3.81% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.66M | 2.90% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.81M | 2.48% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.49M | 2.17% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.21M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.75M | 1.77% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 11 | `5pPRHniefFjk...` | 6.08M | 1.39% | 5.00% |
| 12 | `JD549HsbJHeE...` | 5.95M | 1.36% | 0.00% |
| 13 | `5Cchr1XGEg7d...` | 5.71M | 1.31% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.73M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `BGAjnivVWqLq...` | 266.14K | 461,375,999 |
| `2jS8AX38m8F9...` | 102.51K | 461,375,999 |
| `HzrEstnLfzsi...` | 2.61K | 461,807,999 |
| `GqDCbnafLmKk...` | 397.56 | 460,079,999 |
| `JDvwML44fiV2...` | 290.16 | 0 |
| `SANDCxXBbQhv...` | 181.00 | 460,079,999 |
| `Eu6FQvMfaVav...` | 4.49 | 460,079,999 |
| `FdPyYztZ3DoK...` | 2.00 | 0 |
| `Guv98LNBMw8z...` | 1.01 | 0 |
| `2RbUD2jPMugJ...` | 1.01 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $100.13 |
| SOL 24h | -0.46% |
| SOL 7d | -4.27% |
| SOL 30d | -17.45% |
| Market cap | $59.06B |
| Spot volume 24h | $2.37B |
| Circulating supply | 589.87M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.69B |
| TVL 24h | -0.30% |
| TVL 7d | -2.74% |
| Stablecoin supply | $15.37B |
| DEX volume 24h | $1.72B |
| DEX volume 7d | $12.70B |
| Chain fees 24h (REV proxy) | $11.60M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0529, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215

## Ecosystem news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026)
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4)
- [v4.5.0-alpha.3: Bump version to 4.5.0-alpha.3 (#16402)](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.3)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
