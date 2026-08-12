# Solana Ecosystem State Report

Generated **2026-08-12T19:30:12Z** in 9.5s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 47 prior runs.

## Anomalies

- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 261.3 robust deviations from its 47-point median of 0.0072, a 1613.9% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,015 |
| Epoch progress | 90.73% |
| Epoch time remaining (est.) | 4h 27m |
| Absolute slot | 438,871,934 |
| Block height | 416,923,927 |
| TPS (all) | 4,303.95 |
| TPS (non-vote) | 2,725.80 |
| TPS (30-sample mean) | 4,598.06 |
| Slot time | 428.60 ms |
| Block lag vs wall clock | 16s |
| Lifetime transactions | 537,554,984,816 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 686 |
| Delinquent | 13 |
| Delinquent share of stake | 0.12% |
| Total active stake | 434.93M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.37% |
| Stake in top 20 | 35.70% |
| Stake in top 50 | 55.35% |
| Median commission | 5.00% |
| Validators at 0% commission | 255 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 16.99M | 3.91% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.98M | 3.67% | 0.00% |
| 3 | `JUPiTERrZqgf...` | 12.50M | 2.87% | 5.00% |
| 4 | `DRpbCBMxVnDK...` | 12.33M | 2.84% | 0.00% |
| 5 | `C8Bey3LKVJHV...` | 9.15M | 2.10% | 7.00% |
| 6 | `CAo1dCGYrB6N...` | 8.96M | 2.06% | 10.00% |
| 7 | `E1r4Psq84tHf...` | 8.17M | 1.88% | 0.00% |
| 8 | `EvnRmnMrd69k...` | 7.95M | 1.83% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.37M | 1.69% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.58M | 1.51% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.12M | 1.41% | 100.00% |
| 12 | `JD549HsbJHeE...` | 5.98M | 1.38% | 0.00% |
| 13 | `5pPRHniefFjk...` | 5.92M | 1.36% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.80M | 1.33% | 100.00% |
| 15 | `9rkJMARqK6VB...` | 4.63M | 1.06% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `BULKzVM41WAy...` | 328.10K | 438,858,490 |
| `ArMBx6veRq33...` | 84.51K | 438,870,643 |
| `SPHERExTW7Ga...` | 52.22K | 438,638,200 |
| `7knvB4bbqHCK...` | 38.96K | 438,864,657 |
| `23U4mgK9DMCx...` | 28.58K | 437,861,171 |
| `ECeaWy82Cxpe...` | 3.01K | 438,622,652 |
| `CpuDNi3iVoHX...` | 527.97 | 437,185,456 |
| `3iQqh65Gby53...` | 389.70 | 436,812,576 |
| `AjGby82yXeYg...` | 305.80 | 438,028,228 |
| `Drk2bcinK75J...` | 75.17 | 437,163,253 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $75.73 |
| SOL 24h | 0.69% |
| SOL 7d | 1.71% |
| SOL 30d | 1.24% |
| Market cap | $44.11B |
| Spot volume 24h | $1.35B |
| Circulating supply | 582.50M SOL |
| Circulating share | 92.17% |
| DeFi TVL | $4.82B |
| TVL 24h | -0.15% |
| TVL 7d | 0.55% |
| Stablecoin supply | $15.56B |
| DEX volume 24h | $1.65B |
| DEX volume 7d | $10.45B |
| Chain fees 24h (REV proxy) | $9.98M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0286, SIMD-0340, SIMD-0433, SIMD-0550, SIMD-0553, SIMD-0392, SIMD-0290, SIMD-0565, SIMD-0529, SIMD-0525, SIMD-0022

## Ecosystem news

- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)
- [Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)
- [Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)
- [Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)
- [Solana Changelog: July 23, 2026](https://solana.com/news/solana-changelog-july-23-2026)
- [Deploying enterprise stablecoin rails on Solana in days with Crossmint](https://solana.com/news/case-study-crossmint)
- [Solana Changelog: July 16, 2026](https://solana.com/news/solana-changelog-july-16-2026)
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)
- [Rent Reduction on Solana: A Data-Backed Analysis](https://solana.com/news/rent-reduction-deep-dive)
- [Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)
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
