# Solana Ecosystem State Report

Generated **2026-10-25T16:30:20Z** in 9.1s across 15 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 100.0% (14/14 probes returned data). History depth: 142 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1813 is 61% below the trailing median of 4611.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 6.1 robust deviations from its 142-point median of 9, a 100.0% move.
- [WARNING] **delinquent_pct_by_count** (statistical) - delinquent_pct_by_count is 4.9 robust deviations from its 142-point median of 1.468, a 146.7% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 3.7 robust deviations from its 142-point median of 127, a 8.7% move.
- [WARNING] **tps_avg_30_samples** (statistical) - tps_avg_30_samples is 5.5 robust deviations from its 142-point median of 4632, a 64.9% move.
- [WARNING] **validators_delinquent** (statistical) - validators_delinquent is 5.1 robust deviations from its 142-point median of 10, a 150.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,067 |
| Epoch progress | 88.34% |
| Epoch time remaining (est.) | 5h 35m |
| Absolute slot | 461,325,628 |
| Block height | 439,354,321 |
| TPS (all) | 1,813.43 |
| TPS (non-vote) | 1,813.43 |
| TPS (30-sample mean) | 1,627.65 |
| Slot time | 212.80 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 563,701,062,069 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 665 |
| Delinquent | 25 |
| Delinquent share of stake | 0.05% |
| Total active stake | 437.19M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.58% |
| Stake in top 20 | 35.77% |
| Stake in top 50 | 55.43% |
| Median commission | 5.00% |
| Validators at 0% commission | 226 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.10M | 3.91% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.65M | 3.81% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.59M | 2.88% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.88M | 2.49% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.48M | 2.17% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.22M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.79M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.01M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.61M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.97M | 1.37% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.70M | 1.30% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `GkFT5nmcFVmJ...` | 136.18K | 460,943,999 |
| `ssx2rHZNVy6J...` | 43.05K | 460,511,999 |
| `SANDCxXBbQhv...` | 34.63K | 460,079,999 |
| `GqDCbnafLmKk...` | 397.56 | 460,079,999 |
| `BGD4V7L4aZF5...` | 374.87 | 458,009,563 |
| `Eu6FQvMfaVav...` | 4.49 | 460,079,999 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |
| `FdPyYztZ3DoK...` | 2.00 | 0 |
| `Bi9vzmxLRWRN...` | 1.10 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $101.21 |
| SOL 24h | 1.73% |
| SOL 7d | -0.85% |
| SOL 30d | -15.72% |
| Market cap | $59.69B |
| Spot volume 24h | $1.48B |
| Circulating supply | 589.76M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.72B |
| TVL 24h | -0.90% |
| TVL 7d | -2.93% |
| Stablecoin supply | $15.58B |
| DEX volume 24h | $1.42B |
| DEX volume 7d | $13.69B |
| Chain fees 24h (REV proxy) | $10.05M |

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
- [Release v4.4.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0)
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5 (#683)](https://github.com/solana-foundation/solana-improvement-documents/commit/a084840a512454a7ee5e2ef8dd736c790102bea0)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
