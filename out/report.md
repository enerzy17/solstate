# Solana Ecosystem State Report

Generated **2026-10-20T17:16:04Z** in 11.5s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 5.8 robust deviations from its 141-point median of 1.101e+08, a 28.1% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 6.7 robust deviations from its 141-point median of 126, a 7.9% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 7.2 robust deviations from its 141-point median of 264.3, a 19.5% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,063 |
| Epoch progress | 21.59% |
| Epoch time remaining (est.) | 37h 38m |
| Absolute slot | 459,309,247 |
| Block height | 437,344,280 |
| TPS (all) | 6,022.70 |
| TPS (non-vote) | 2,903.75 |
| TPS (30-sample mean) | 5,623.43 |
| Slot time | 212.80 ms |
| Block lag vs wall clock | 8s |
| Lifetime transactions | 562,671,906,706 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 667 |
| Delinquent | 12 |
| Delinquent share of stake | 0.04% |
| Total active stake | 438.58M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.35% |
| Stake in top 20 | 35.56% |
| Stake in top 50 | 55.39% |
| Median commission | 5.00% |
| Validators at 0% commission | 230 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.10M | 3.90% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.94M | 3.63% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.54M | 2.86% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.93M | 2.49% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.48M | 2.16% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.25M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.79M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.03M | 1.60% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.60M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.99M | 1.37% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.68M | 1.29% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `revtecFsGSRC...` | 112.90K | 459,302,111 |
| `BaDhUB1eWfun...` | 75.00K | 459,299,231 |
| `GqDCbnafLmKk...` | 554.86 | 458,710,110 |
| `HyperSPG8w4j...` | 397.89 | 457,059,085 |
| `BGD4V7L4aZF5...` | 374.87 | 458,009,563 |
| `AqyRvpjjSN6j...` | 26.06 | 457,389,885 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |
| `6mygxmZxmTqq...` | 2.00 | 459,079,478 |
| `FdPyYztZ3DoK...` | 2.00 | 0 |
| `FsEq1UFSucxy...` | 1.50 | 449,622,948 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $106.43 |
| SOL 24h | 2.05% |
| SOL 7d | -0.98% |
| SOL 30d | -3.44% |
| Market cap | $62.74B |
| Spot volume 24h | $2.72B |
| Circulating supply | 589.55M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.90B |
| TVL 24h | 0.86% |
| TVL 7d | -1.32% |
| Stablecoin supply | $15.66B |
| DEX volume 24h | $1.82B |
| DEX volume 7d | $14.36B |
| Chain fees 24h (REV proxy) | $11.99M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610

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
- [SIMD-0686: Single Program Runtime Environment (#688)](https://github.com/solana-foundation/solana-improvement-documents/commit/749dc8635821383c5c259d616e337687707f3ef9)
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData (#684)](https://github.com/solana-foundation/solana-improvement-documents/commit/f24b888c352c115f08438ebdb57f5bba46136745)
- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
