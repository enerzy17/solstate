# Solana Ecosystem State Report

Generated **2026-09-24T17:16:52Z** in 8.1s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 148 prior runs.

## Anomalies

- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 6.9 robust deviations from its 148-point median of 315.8, a 15.9% move.
- [WARNING] **tvl_usd** (statistical) - tvl_usd is 4.2 robust deviations from its 148-point median of 5.887e+09, a 8.9% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,041 |
| Epoch progress | 88.38% |
| Epoch time remaining (est.) | 5h 34m |
| Absolute slot | 450,093,803 |
| Block height | 428,133,889 |
| TPS (all) | 4,958.07 |
| TPS (non-vote) | 2,423.92 |
| TPS (30-sample mean) | 4,945.27 |
| Slot time | 265.50 ms |
| Block lag vs wall clock | 9s |
| Lifetime transactions | 552,171,251,746 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 674 |
| Delinquent | 12 |
| Delinquent share of stake | 0.05% |
| Total active stake | 439.96M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.38% |
| Stake in top 20 | 35.66% |
| Stake in top 50 | 55.38% |
| Median commission | 5.00% |
| Validators at 0% commission | 233 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.84M | 4.06% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.84M | 3.60% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.36M | 2.81% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.26M | 2.56% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 10.34M | 2.35% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.23M | 2.10% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.16M | 2.08% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.60M | 1.73% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.09M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.56M | 1.49% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.22M | 1.41% | 0.00% |
| 12 | `9jxgosAfHgHz...` | 6.13M | 1.39% | 100.00% |
| 13 | `5pPRHniefFjk...` | 5.94M | 1.35% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.61M | 1.27% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.83M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `6DTkuiey2RgM...` | 89.15K | 0 |
| `HDRqPft5ioWZ...` | 71.15K | 0 |
| `t23p8aBQN6P6...` | 14.37K | 447,595,236 |
| `AYY1TCe347UZ...` | 10.70K | 450,015,156 |
| `NWY18yrPHsTo...` | 9.76K | 448,798,710 |
| `mrgn4atx3Jnf...` | 2.21K | 448,597,405 |
| `pSoLoZx55zZz...` | 1.51K | 447,874,752 |
| `HgozywotiKv4...` | 797.43 | 448,492,871 |
| `ARKk6RgiFq4M...` | 63.92 | 450,022,154 |
| `9fTWmMqVz5cW...` | 23.86 | 448,762,375 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $117.15 |
| SOL 24h | 2.74% |
| SOL 7d | 15.66% |
| SOL 30d | 19.33% |
| Market cap | $68.84B |
| Spot volume 24h | $4.23B |
| Circulating supply | 587.58M SOL |
| Circulating share | 92.59% |
| DeFi TVL | $6.41B |
| TVL 24h | -1.89% |
| TVL 7d | 10.88% |
| Stablecoin supply | $15.97B |
| DEX volume 24h | $2.55B |
| DEX volume 7d | $20.98B |
| Chain fees 24h (REV proxy) | $16.12M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550, SIMD-0599, SIMD-0340, SIMD-0433

## Ecosystem news

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)
- [SIMD-0558: Describe pointer validation & update CU cost (#651)](https://github.com/solana-foundation/solana-improvement-documents/commit/8b157e1def5fb3b3779f0935ec71cd7cae271207)
- [Increase TxV1 Account Lock Limit to 96 (#596)](https://github.com/solana-foundation/solana-improvement-documents/commit/b7ca332f0aabe11ecc6cf36143462d4487d59a39)
- [Release v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
