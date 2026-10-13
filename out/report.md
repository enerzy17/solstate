# Solana Ecosystem State Report

Generated **2026-10-13T21:19:25Z** in 10.0s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 142 prior runs.

## Anomalies

- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 4.7 robust deviations from its 142-point median of 126, a 5.6% move.
- [WARNING] **dex_volume_change_24h_pct** (statistical) - dex_volume_change_24h_pct is 4.8 robust deviations from its 142-point median of -0.05, a 149640.0% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 8.7 robust deviations from its 142-point median of 266.7, a 17.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,056 |
| Epoch progress | 91.54% |
| Epoch time remaining (est.) | 4h 3m |
| Absolute slot | 456,587,469 |
| Block height | 434,623,837 |
| TPS (all) | 4,837.28 |
| TPS (non-vote) | 1,812.33 |
| TPS (30-sample mean) | 4,946.94 |
| Slot time | 221.40 ms |
| Block lag vs wall clock | 7s |
| Lifetime transactions | 559,753,642,172 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 673 |
| Delinquent | 7 |
| Delinquent share of stake | 0.01% |
| Total active stake | 438.79M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.55% |
| Stake in top 20 | 35.66% |
| Stake in top 50 | 55.41% |
| Median commission | 5.00% |
| Validators at 0% commission | 228 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.79M | 4.05% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.96M | 3.64% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.31M | 2.80% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 11.15M | 2.54% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 10.76M | 2.45% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.40M | 2.14% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.68M | 1.75% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.81M | 1.55% | 5.00% |
| 10 | `JD549HsbJHeE...` | 6.64M | 1.51% | 0.00% |
| 11 | `Awes4Tr6TX8J...` | 6.41M | 1.46% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.98M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.67M | 1.29% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `rssaJ2iKcE9Q...` | 34.39K | 456,203,301 |
| `tboxdsRMjUfY...` | 18.53K | 455,988,360 |
| `ApVnoa3r3okD...` | 180.14 | 454,213,509 |
| `BZBKHmW1DhBa...` | 9.59 | 402,784,479 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `TQmxEmTFVn5g...` | 2.14 | 454,213,564 |
| `6mygxmZxmTqq...` | 2.00 | 456,290,998 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $106.98 |
| SOL 24h | -1.00% |
| SOL 7d | -11.59% |
| SOL 30d | 5.45% |
| Market cap | $63.03B |
| Spot volume 24h | $4.07B |
| Circulating supply | 589.16M SOL |
| Circulating share | 92.68% |
| DeFi TVL | $6.04B |
| TVL 24h | -3.00% |
| TVL 7d | -8.23% |
| Stablecoin supply | $16.03B |
| DEX volume 24h | $2.23B |
| DEX volume 7d | $13.68B |
| Chain fees 24h (REV proxy) | $13.10M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Solana Changelog: September 24, 2026](https://solana.com/news/solana-changelog-september-24-2026)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)
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
