# Solana Ecosystem State Report

Generated **2026-08-11T19:28:49Z** in 21.6s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 36 prior runs.

## Anomalies

- [WARNING] **chain_fees_24h_usd** (statistical) - chain_fees_24h_usd is 8.2 robust deviations from its 36-point median of 9.166e+06, a 14.5% move.
- [WARNING] **rev_proxy_24h_usd** (statistical) - rev_proxy_24h_usd is 8.2 robust deviations from its 36-point median of 9.166e+06, a 14.5% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,015 |
| Epoch progress | 43.08% |
| Epoch time remaining (est.) | 27h 19m |
| Absolute slot | 438,666,125 |
| Block height | 416,719,767 |
| TPS (all) | 4,381.27 |
| TPS (non-vote) | 2,716.40 |
| TPS (30-sample mean) | 3,969.86 |
| Slot time | 413.80 ms |
| Block lag vs wall clock | 15s |
| Lifetime transactions | 537,234,326,370 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 690 |
| Delinquent | 9 |
| Delinquent share of stake | 0.02% |
| Total active stake | 434.93M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.37% |
| Stake in top 20 | 35.70% |
| Stake in top 50 | 55.35% |
| Median commission | 5.00% |
| Validators at 0% commission | 259 |
| Validators at 100% commission | 61 |

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
| `SPHERExTW7Ga...` | 52.22K | 438,638,200 |
| `23U4mgK9DMCx...` | 28.58K | 437,861,171 |
| `ECeaWy82Cxpe...` | 3.01K | 438,622,652 |
| `CpuDNi3iVoHX...` | 527.97 | 437,185,456 |
| `3iQqh65Gby53...` | 389.70 | 436,812,576 |
| `AjGby82yXeYg...` | 305.80 | 438,028,228 |
| `Drk2bcinK75J...` | 75.17 | 437,163,253 |
| `32jCuWyy4aJj...` | 2.70 | 436,736,029 |
| `R1parD2CtxPB...` | 1.62 | 384,048,870 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $75.21 |
| SOL 24h | -1.02% |
| SOL 7d | 1.53% |
| SOL 30d | -2.99% |
| Market cap | $43.80B |
| Spot volume 24h | $1.25B |
| Circulating supply | 582.48M SOL |
| Circulating share | 92.16% |
| DeFi TVL | $4.80B |
| TVL 24h | -0.79% |
| TVL 7d | 1.05% |
| Stablecoin supply | $15.73B |
| DEX volume 24h | $1.58B |
| DEX volume 7d | $10.55B |
| Chain fees 24h (REV proxy) | $10.49M |

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
