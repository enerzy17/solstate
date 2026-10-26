# Solana Ecosystem State Report

Generated **2026-10-26T07:52:27Z** in 9.7s across 15 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 100.0% (14/14 probes returned data). History depth: 142 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1589 is 65% below the trailing median of 4592.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 6.1 robust deviations from its 142-point median of 9, a 100.0% move.
- [WARNING] **delinquent_pct_by_count** (statistical) - delinquent_pct_by_count is 3.9 robust deviations from its 142-point median of 1.539, a 135.4% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 4.4 robust deviations from its 142-point median of 0.0185, a 567.0% move.
- [WARNING] **tps_avg_30_samples** (statistical) - tps_avg_30_samples is 5.6 robust deviations from its 142-point median of 4626, a 70.1% move.
- [WARNING] **validators_delinquent** (statistical) - validators_delinquent is 3.9 robust deviations from its 142-point median of 10.5, a 138.1% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,068 |
| Epoch progress | 48.63% |
| Epoch time remaining (est.) | 24h 39m |
| Absolute slot | 461,586,061 |
| Block height | 439,613,308 |
| TPS (all) | 1,589.32 |
| TPS (non-vote) | 1,589.32 |
| TPS (30-sample mean) | 1,380.97 |
| Slot time | 212.00 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 563,797,115,604 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 665 |
| Delinquent | 25 |
| Delinquent share of stake | 0.12% |
| Total active stake | 437.72M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.54% |
| Stake in top 20 | 35.73% |
| Stake in top 50 | 55.37% |
| Median commission | 5.00% |
| Validators at 0% commission | 229 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.10M | 3.91% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.64M | 3.80% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.59M | 2.88% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.88M | 2.49% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.49M | 2.17% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.19M | 2.10% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.79M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.99M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.61M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.98M | 1.37% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.71M | 1.30% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `BGAjnivVWqLq...` | 266.14K | 461,375,999 |
| `GkFT5nmcFVmJ...` | 135.67K | 460,943,999 |
| `2jS8AX38m8F9...` | 102.99K | 461,375,999 |
| `SANDCxXBbQhv...` | 34.64K | 460,079,999 |
| `GqDCbnafLmKk...` | 397.56 | 460,079,999 |
| `BGD4V7L4aZF5...` | 374.87 | 458,009,563 |
| `Eu6FQvMfaVav...` | 4.49 | 460,079,999 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |
| `BZBKHmW1DhBa...` | 2.45 | 402,784,479 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $100.57 |
| SOL 24h | -1.08% |
| SOL 7d | -4.84% |
| SOL 30d | -16.34% |
| Market cap | $59.32B |
| Spot volume 24h | $1.81B |
| Circulating supply | 589.82M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.70B |
| TVL 24h | -1.31% |
| TVL 7d | -2.67% |
| Stablecoin supply | $15.69B |
| DEX volume 24h | $1.35B |
| DEX volume 7d | $12.50B |
| Chain fees 24h (REV proxy) | $9.63M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0670, SIMD-0683, SIMD-0529, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558

## Ecosystem news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [SIMD-0670: ABIv1 invoke signed v2 syscall (#670)](https://github.com/solana-foundation/solana-improvement-documents/commit/c9ec366af14dd32a74259f5d9f5772249188bd25)
- [v4.4.0-rc.0: Bump version to 4.4.0-rc.0 (#16364)](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0)
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5 (#683)](https://github.com/solana-foundation/solana-improvement-documents/commit/a084840a512454a7ee5e2ef8dd736c790102bea0)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
