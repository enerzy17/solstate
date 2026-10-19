# Solana Ecosystem State Report

Generated **2026-10-19T13:29:43Z** in 9.0s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 143 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 5.0 robust deviations from its 143-point median of 1.097e+08, a 26.9% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 6.7 robust deviations from its 143-point median of 126, a 7.9% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 9.8 robust deviations from its 143-point median of 264.3, a 19.8% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,062 |
| Epoch progress | 15.34% |
| Epoch time remaining (est.) | 40h 38m |
| Absolute slot | 458,850,289 |
| Block height | 436,885,489 |
| TPS (all) | 5,075.58 |
| TPS (non-vote) | 2,038.38 |
| TPS (30-sample mean) | 4,899.17 |
| Slot time | 212.00 ms |
| Block lag vs wall clock | 8s |
| Lifetime transactions | 562,164,929,621 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 667 |
| Delinquent | 12 |
| Delinquent share of stake | 0.02% |
| Total active stake | 437.88M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.27% |
| Stake in top 20 | 35.51% |
| Stake in top 50 | 55.38% |
| Median commission | 5.00% |
| Validators at 0% commission | 230 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.10M | 3.90% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.73M | 3.59% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.52M | 2.86% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.98M | 2.51% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.48M | 2.17% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.25M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.79M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.99M | 1.60% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.73M | 1.54% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.60M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.99M | 1.37% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.67M | 1.30% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.87M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `sce1oTWYVXv7...` | 58.95K | 458,828,444 |
| `DiFeTctQSaNc...` | 15.85K | 458,804,771 |
| `GqDCbnafLmKk...` | 702.18 | 458,710,110 |
| `HyperSPG8w4j...` | 397.89 | 457,059,085 |
| `BGD4V7L4aZF5...` | 374.87 | 458,009,563 |
| `AqyRvpjjSN6j...` | 26.06 | 457,389,885 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 458,681,794 |
| `FdPyYztZ3DoK...` | 2.00 | 0 |
| `4qJwZS4hw25j...` | 1.01 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $105.25 |
| SOL 24h | 2.06% |
| SOL 7d | -4.47% |
| SOL 30d | -5.82% |
| Market cap | $62.04B |
| Spot volume 24h | $2.68B |
| Circulating supply | 589.49M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.87B |
| TVL 24h | -0.47% |
| TVL 7d | -5.70% |
| Stablecoin supply | $15.52B |
| DEX volume 24h | $1.70B |
| DEX volume 7d | $14.76B |
| Chain fees 24h (REV proxy) | $9.71M |

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
