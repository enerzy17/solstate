# Solana Ecosystem State Report

Generated **2026-09-26T16:28:34Z** in 7.5s across 15 HTTP calls.

> **Status:** 6 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 139 prior runs.

## Anomalies

- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 6.2 robust deviations from its 139-point median of 314.1, a 13.9% move.
- [WARNING] **sol_ath_change_pct** (statistical) - sol_ath_change_pct is 4.5 robust deviations from its 139-point median of -64.66, a 9.4% move.
- [WARNING] **sol_fdv_usd** (statistical) - sol_fdv_usd is 4.4 robust deviations from its 139-point median of 6.564e+10, a 17.5% move.
- [WARNING] **sol_market_cap_usd** (statistical) - sol_market_cap_usd is 4.6 robust deviations from its 139-point median of 6.066e+10, a 17.7% move.
- [WARNING] **sol_price_usd** (statistical) - sol_price_usd is 4.5 robust deviations from its 139-point median of 103.7, a 17.2% move.
- [WARNING] **tvl_usd** (statistical) - tvl_usd is 6.7 robust deviations from its 139-point median of 5.904e+09, a 11.9% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,043 |
| Epoch progress | 35.26% |
| Epoch time remaining (est.) | 31h 4m |
| Absolute slot | 450,728,337 |
| Block height | 428,768,090 |
| TPS (all) | 4,210.32 |
| TPS (non-vote) | 1,717.90 |
| TPS (30-sample mean) | 4,435.08 |
| Slot time | 270.30 ms |
| Block lag vs wall clock | 10s |
| Lifetime transactions | 552,937,795,664 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 676 |
| Delinquent | 11 |
| Delinquent share of stake | 0.01% |
| Total active stake | 437.54M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.61% |
| Stake in top 20 | 35.43% |
| Stake in top 50 | 55.23% |
| Median commission | 5.00% |
| Validators at 0% commission | 233 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.86M | 4.08% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.80M | 3.61% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.34M | 2.82% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.22M | 2.56% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 10.84M | 2.48% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.24M | 2.11% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.18M | 2.10% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.61M | 1.74% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.09M | 1.62% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.51M | 1.49% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.25M | 1.43% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.93M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.63M | 1.29% | 100.00% |
| 14 | `9rkJMARqK6VB...` | 4.70M | 1.07% | 8.00% |
| 15 | `GnC339vkyXRm...` | 4.62M | 1.06% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `4YGgmwyqztpJ...` | 12.74K | 450,345,071 |
| `AYY1TCe347UZ...` | 10.70K | 450,466,404 |
| `NWY18yrPHsTo...` | 9.76K | 448,798,710 |
| `mrgn4atx3Jnf...` | 2.21K | 448,597,405 |
| `HgozywotiKv4...` | 790.08 | 448,492,871 |
| `ARKk6RgiFq4M...` | 63.93 | 450,022,154 |
| `9fTWmMqVz5cW...` | 23.86 | 448,762,375 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |
| `6mygxmZxmTqq...` | 2.00 | 450,230,119 |
| `CZMekcZwyKLC...` | 1.00 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $121.50 |
| SOL 24h | 0.33% |
| SOL 7d | 8.85% |
| SOL 30d | 13.28% |
| Market cap | $71.41B |
| Spot volume 24h | $3.73B |
| Circulating supply | 587.71M SOL |
| Circulating share | 92.59% |
| DeFi TVL | $6.61B |
| TVL 24h | 1.91% |
| TVL 7d | 4.80% |
| Stablecoin supply | $16.50B |
| DEX volume 24h | $2.61B |
| DEX volume 7d | $19.91B |
| Chain fees 24h (REV proxy) | $15.60M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550, SIMD-0599

## Ecosystem news

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)
- [Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)
- [Amend simd 0376 ed25519-zebra verification (#616)](https://github.com/solana-foundation/solana-improvement-documents/commit/4b643ca8746742183a469681765e694b385bb315)
- [SIMD-0215: clarify LtHash security considerations (#669)](https://github.com/solana-foundation/solana-improvement-documents/commit/f1afd941b9fa5061ea80a5401feb72172121ebb5)
- [SIMD-0558: Describe pointer validation & update CU cost (#651)](https://github.com/solana-foundation/solana-improvement-documents/commit/8b157e1def5fb3b3779f0935ec71cd7cae271207)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
