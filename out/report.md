# Solana Ecosystem State Report

Generated **2026-10-17T22:24:32Z** in 10.1s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 142 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 4.5 robust deviations from its 142-point median of 1.099e+08, a 23.3% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 6.7 robust deviations from its 142-point median of 126, a 7.9% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 8.0 robust deviations from its 142-point median of 265.5, a 16.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,060 |
| Epoch progress | 65.07% |
| Epoch time remaining (est.) | 16h 45m |
| Absolute slot | 458,201,111 |
| Block height | 436,236,480 |
| TPS (all) | 4,815.77 |
| TPS (non-vote) | 1,817.93 |
| TPS (30-sample mean) | 5,173.62 |
| Slot time | 223.00 ms |
| Block lag vs wall clock | 8s |
| Lifetime transactions | 561,493,992,610 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 671 |
| Delinquent | 10 |
| Delinquent share of stake | 0.00% |
| Total active stake | 438.75M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.41% |
| Stake in top 20 | 35.61% |
| Stake in top 50 | 55.44% |
| Median commission | 5.00% |
| Validators at 0% commission | 229 |
| Validators at 100% commission | 64 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.53M | 4.00% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.74M | 3.59% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.49M | 2.85% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.97M | 2.50% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 10.19M | 2.32% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.45M | 2.15% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.25M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.76M | 1.77% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.99M | 1.59% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.73M | 1.53% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.60M | 1.50% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.98M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.67M | 1.29% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.87M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `rssaJ2iKcE9Q...` | 1.42K | 456,203,301 |
| `HyperSPG8w4j...` | 397.89 | 457,059,085 |
| `BGD4V7L4aZF5...` | 373.86 | 458,009,563 |
| `AqyRvpjjSN6j...` | 26.06 | 457,389,885 |
| `9bjXFvs3ygxH...` | 5.00 | 0 |
| `tboxdsRMjUfY...` | 4.01 | 455,988,360 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 457,884,144 |
| `FdPyYztZ3DoK...` | 2.00 | 0 |
| `JDY2ADULVm1u...` | 1.00 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $102.71 |
| SOL 24h | -1.69% |
| SOL 7d | -6.81% |
| SOL 30d | 1.66% |
| Market cap | $60.54B |
| Spot volume 24h | $1.66B |
| Circulating supply | 589.38M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.91B |
| TVL 24h | -1.22% |
| TVL 7d | -4.02% |
| Stablecoin supply | $15.63B |
| DEX volume 24h | $2.17B |
| DEX volume 7d | $14.38B |
| Chain fees 24h (REV proxy) | $12.52M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1)
- [Release v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
