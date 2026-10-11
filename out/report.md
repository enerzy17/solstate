# Solana Ecosystem State Report

Generated **2026-10-11T18:58:27Z** in 8.4s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 145 prior runs.

## Anomalies

- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 9.3 robust deviations from its 145-point median of 267.9, a 18.6% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,054 |
| Epoch progress | 99.58% |
| Epoch time remaining (est.) | 12m 2s |
| Absolute slot | 455,758,194 |
| Block height | 433,795,326 |
| TPS (all) | 5,232.92 |
| TPS (non-vote) | 2,165.40 |
| TPS (30-sample mean) | 5,188.22 |
| Slot time | 218.20 ms |
| Block lag vs wall clock | 8s |
| Lifetime transactions | 558,841,561,406 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 672 |
| Delinquent | 8 |
| Delinquent share of stake | 0.03% |
| Total active stake | 438.74M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.47% |
| Stake in top 20 | 35.55% |
| Stake in top 50 | 55.30% |
| Median commission | 5.00% |
| Validators at 0% commission | 231 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.78M | 4.05% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.95M | 3.64% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.31M | 2.81% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 11.15M | 2.54% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 10.75M | 2.45% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.33M | 2.13% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.60M | 1.73% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.81M | 1.55% | 5.00% |
| 10 | `JD549HsbJHeE...` | 6.42M | 1.46% | 0.00% |
| 11 | `Awes4Tr6TX8J...` | 6.41M | 1.46% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.97M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.68M | 1.29% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.85M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `tboxdsRMjUfY...` | 63.41K | 455,692,077 |
| `FFevTkywysWf...` | 32.81K | 455,716,932 |
| `TQmxEmTFVn5g...` | 8.95K | 454,213,564 |
| `9gMjDS6WPahW...` | 5.00K | 455,566,680 |
| `ApVnoa3r3okD...` | 208.75 | 454,213,509 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 455,500,251 |
| `BAqygpJA82ZJ...` | 1.00 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $111.45 |
| SOL 24h | 1.13% |
| SOL 7d | -8.25% |
| SOL 30d | 9.33% |
| Market cap | $65.61B |
| Spot volume 24h | $1.81B |
| Circulating supply | 589.05M SOL |
| Circulating share | 92.68% |
| DeFi TVL | $6.27B |
| TVL 24h | 1.21% |
| TVL 7d | -3.91% |
| Stablecoin supply | $16.07B |
| DEX volume 24h | $1.29B |
| DEX volume 7d | $13.93B |
| Chain fees 24h (REV proxy) | $11.94M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Solana Changelog: September 24, 2026](https://solana.com/news/solana-changelog-september-24-2026)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [Release v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2)
- [amend SIMD-0464: clarify aliasing rules (#618)](https://github.com/solana-foundation/solana-improvement-documents/commit/f1f6c8b05dc205552d3c290a854a438392701107)
- [Release v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
