# Solana Ecosystem State Report

Generated **2026-10-22T12:01:06Z** in 9.2s across 15 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 100.0% (14/14 probes returned data). History depth: 142 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1865 is 60% below the trailing median of 4646.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 5.4 robust deviations from its 142-point median of 9, a 88.9% move.
- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 5.0 robust deviations from its 142-point median of 1.099e+08, a 25.8% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 8.1 robust deviations from its 142-point median of 126, a 9.5% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 5.5 robust deviations from its 142-point median of 263.2, a 20.3% move.
- [WARNING] **tps_avg_30_samples** (statistical) - tps_avg_30_samples is 6.0 robust deviations from its 142-point median of 4657, a 55.4% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,064 |
| Epoch progress | 87.87% |
| Epoch time remaining (est.) | 5h 49m |
| Absolute slot | 460,027,578 |
| Block height | 438,061,366 |
| TPS (all) | 1,865.12 |
| TPS (non-vote) | 1,865.12 |
| TPS (30-sample mean) | 2,078.39 |
| Slot time | 209.80 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 563,208,010,938 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 668 |
| Delinquent | 9 |
| Delinquent share of stake | 0.01% |
| Total active stake | 438.87M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.35% |
| Stake in top 20 | 35.56% |
| Stake in top 50 | 55.36% |
| Median commission | 5.00% |
| Validators at 0% commission | 227 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.13M | 3.90% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.96M | 3.64% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.55M | 2.86% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.93M | 2.49% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.73M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.48M | 2.16% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.25M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.81M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.60% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.61M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.99M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.67M | 1.29% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `9fa5wcqnAQqH...` | 11.69K | 459,643,077 |
| `FWD1aVC1U1zV...` | 10.00K | 459,643,077 |
| `BGD4V7L4aZF5...` | 374.87 | 458,009,563 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 459,478,085 |
| `FdPyYztZ3DoK...` | 2.00 | 0 |
| `4qJwZS4hw25j...` | 1.01 | 0 |
| `JDY2ADULVm1u...` | 1.00 | 459,648,469 |
| `spur5CDwBvTZ...` | 0.00 | 458,389,272 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $104.40 |
| SOL 24h | -2.20% |
| SOL 7d | 2.23% |
| SOL 30d | -10.98% |
| Market cap | $61.55B |
| Spot volume 24h | $2.89B |
| Circulating supply | 589.60M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.88B |
| TVL 24h | -1.39% |
| TVL 7d | -0.88% |
| Stablecoin supply | $15.90B |
| DEX volume 24h | $2.27B |
| DEX volume 7d | $14.45B |
| Chain fees 24h (REV proxy) | $11.89M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377

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
- [SIMD-0648: Unbound LoaderV3 Instruction Data (#648)](https://github.com/solana-foundation/solana-improvement-documents/commit/27ff5a704391d121869dd3bc8cfa8127483329d0)
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 sy…](https://github.com/solana-foundation/solana-improvement-documents/commit/f13f5d657ccae32cb19cae84ccb6c781cd125ad7)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
