# Solana Ecosystem State Report

Generated **2026-10-15T04:48:51Z** in 8.9s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 4.3 robust deviations from its 141-point median of 1.101e+08, a 20.7% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 4.7 robust deviations from its 141-point median of 126, a 5.6% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 9.9 robust deviations from its 141-point median of 266.7, a 19.3% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,058 |
| Epoch progress | 12.47% |
| Epoch time remaining (est.) | 42h 0m |
| Absolute slot | 457,109,878 |
| Block height | 435,145,804 |
| TPS (all) | 4,571.50 |
| TPS (non-vote) | 1,460.78 |
| TPS (30-sample mean) | 4,817.66 |
| Slot time | 215.10 ms |
| Block lag vs wall clock | 8s |
| Lifetime transactions | 560,320,675,676 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 672 |
| Delinquent | 8 |
| Delinquent share of stake | 0.00% |
| Total active stake | 437.89M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.48% |
| Stake in top 20 | 35.62% |
| Stake in top 50 | 55.37% |
| Median commission | 5.00% |
| Validators at 0% commission | 231 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.56M | 4.01% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.48M | 3.53% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.34M | 2.82% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 11.13M | 2.54% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 10.78M | 2.46% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.41M | 2.15% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.23M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.74M | 1.77% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.91M | 1.58% | 5.00% |
| 10 | `JD549HsbJHeE...` | 6.64M | 1.52% | 0.00% |
| 11 | `Awes4Tr6TX8J...` | 6.41M | 1.46% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.97M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.67M | 1.30% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.87M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `rssaJ2iKcE9Q...` | 1.42K | 456,203,301 |
| `HyperSPG8w4j...` | 397.89 | 457,059,085 |
| `9bjXFvs3ygxH...` | 5.00 | 0 |
| `tboxdsRMjUfY...` | 4.01 | 455,988,360 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 457,086,608 |
| `TQmxEmTFVn5g...` | 1.41 | 454,213,564 |
| `JDY2ADULVm1u...` | 1.00 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $104.06 |
| SOL 24h | -3.65% |
| SOL 7d | -10.05% |
| SOL 30d | 2.53% |
| Market cap | $61.33B |
| Spot volume 24h | $4.09B |
| Circulating supply | 589.27M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.92B |
| TVL 24h | -1.13% |
| TVL 7d | -7.80% |
| Stablecoin supply | $15.76B |
| DEX volume 24h | $2.25B |
| DEX volume 7d | $12.96B |
| Chain fees 24h (REV proxy) | $10.64M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0123, SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1)
- [Release v4.3.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.1)
- [Release v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
