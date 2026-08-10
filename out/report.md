# Solana Ecosystem State Report

Generated **2026-08-10T17:12:14Z** in 10.2s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 24 prior runs.

## Anomalies

- [WARNING] **dex_volume_24h_usd** (statistical) - dex_volume_24h_usd is 6.4 robust deviations from its 24-point median of 1.479e+09, a 8.9% move.
- [WARNING] **dex_volume_change_24h_pct** (statistical) - dex_volume_change_24h_pct is 12.2 robust deviations from its 24-point median of 8.67, a 212.6% move.
- [WARNING] **sol_change_24h_pct** (statistical) - sol_change_24h_pct is 4.4 robust deviations from its 24-point median of 1.35, a 232.6% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,014 |
| Epoch progress | 91.15% |
| Epoch time remaining (est.) | 4h 14m |
| Absolute slot | 438,441,776 |
| Block height | 416,495,545 |
| TPS (all) | 4,434.02 |
| TPS (non-vote) | 2,786.95 |
| TPS (30-sample mean) | 4,332.90 |
| Slot time | 416.70 ms |
| Block lag vs wall clock | 14s |
| Lifetime transactions | 536,894,375,637 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 690 |
| Delinquent | 8 |
| Delinquent share of stake | 0.01% |
| Total active stake | 434.05M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.39% |
| Stake in top 20 | 35.74% |
| Stake in top 50 | 55.42% |
| Median commission | 5.00% |
| Validators at 0% commission | 257 |
| Validators at 100% commission | 64 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 16.92M | 3.90% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.98M | 3.68% | 0.00% |
| 3 | `JUPiTERrZqgf...` | 12.49M | 2.88% | 5.00% |
| 4 | `DRpbCBMxVnDK...` | 12.29M | 2.83% | 0.00% |
| 5 | `C8Bey3LKVJHV...` | 9.18M | 2.12% | 7.00% |
| 6 | `CAo1dCGYrB6N...` | 8.95M | 2.06% | 10.00% |
| 7 | `E1r4Psq84tHf...` | 8.17M | 1.88% | 0.00% |
| 8 | `EvnRmnMrd69k...` | 7.94M | 1.83% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.37M | 1.70% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.57M | 1.51% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.12M | 1.41% | 100.00% |
| 12 | `JD549HsbJHeE...` | 5.98M | 1.38% | 0.00% |
| 13 | `5pPRHniefFjk...` | 5.91M | 1.36% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.80M | 1.34% | 100.00% |
| 15 | `9rkJMARqK6VB...` | 4.63M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `23U4mgK9DMCx...` | 29.53K | 437,861,171 |
| `ChaossRPGKns...` | 12.75K | 438,322,645 |
| `CpuDNi3iVoHX...` | 527.97 | 437,185,456 |
| `AjGby82yXeYg...` | 527.20 | 438,028,228 |
| `3iQqh65Gby53...` | 389.70 | 436,812,576 |
| `5HCTsoKM7vwj...` | 121.83 | 435,891,365 |
| `Drk2bcinK75J...` | 75.17 | 437,163,253 |
| `32jCuWyy4aJj...` | 2.70 | 436,736,029 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $75.81 |
| SOL 24h | -1.79% |
| SOL 7d | 3.37% |
| SOL 30d | -2.68% |
| Market cap | $44.11B |
| Spot volume 24h | $1.38B |
| Circulating supply | 582.17M SOL |
| Circulating share | 92.13% |
| DeFi TVL | $4.83B |
| TVL 24h | 0.71% |
| TVL 7d | 2.10% |
| Stablecoin supply | $15.60B |
| DEX volume 24h | $1.35B |
| DEX volume 7d | $10.68B |
| Chain fees 24h (REV proxy) | $9.10M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0286, SIMD-0340, SIMD-0433, SIMD-0550, SIMD-0553, SIMD-0392, SIMD-0290, SIMD-0565, SIMD-0529, SIMD-0525, SIMD-0022

## Ecosystem news

- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)
- [Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)
- [Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)
- [Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)
- [Solana Changelog: July 23, 2026](https://solana.com/news/solana-changelog-july-23-2026)
- [Deploying enterprise stablecoin rails on Solana in days with Crossmint](https://solana.com/news/case-study-crossmint)
- [Solana Changelog: July 16, 2026](https://solana.com/news/solana-changelog-july-16-2026)
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)
- [Rent Reduction on Solana: A Data-Backed Analysis](https://solana.com/news/rent-reduction-deep-dive)
- [Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)
- [The Sun Rises in Seoul and Trades on Solana: $SKHY is Now Live](https://solana.com/news/skhy-is-now-live)
- [Release v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0)
- [Release v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3)
- [Release v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
