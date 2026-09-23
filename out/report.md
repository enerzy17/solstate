# Solana Ecosystem State Report

Generated **2026-09-23T07:48:47Z** in 8.1s across 15 HTTP calls.

> **Status:** 6 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 160 prior runs.

## Anomalies

- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 6.3 robust deviations from its 160-point median of 316.6, a 17.6% move.
- [WARNING] **sol_ath_change_pct** (statistical) - sol_ath_change_pct is 3.7 robust deviations from its 160-point median of -65.28, a 8.3% move.
- [WARNING] **sol_fdv_usd** (statistical) - sol_fdv_usd is 3.9 robust deviations from its 160-point median of 6.453e+10, a 15.8% move.
- [WARNING] **sol_market_cap_usd** (statistical) - sol_market_cap_usd is 3.9 robust deviations from its 160-point median of 5.968e+10, a 15.9% move.
- [WARNING] **sol_price_usd** (statistical) - sol_price_usd is 3.8 robust deviations from its 160-point median of 101.8, a 15.6% move.
- [WARNING] **tvl_usd** (statistical) - tvl_usd is 5.4 robust deviations from its 160-point median of 5.858e+09, a 11.7% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,040 |
| Epoch progress | 83.33% |
| Epoch time remaining (est.) | 8h 0m |
| Absolute slot | 449,639,983 |
| Block height | 427,680,270 |
| TPS (all) | 4,339.92 |
| TPS (non-vote) | 1,755.33 |
| TPS (30-sample mean) | 4,129.57 |
| Slot time | 260.90 ms |
| Block lag vs wall clock | 9s |
| Lifetime transactions | 551,630,660,946 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 676 |
| Delinquent | 12 |
| Delinquent share of stake | 0.05% |
| Total active stake | 439.86M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.32% |
| Stake in top 20 | 35.62% |
| Stake in top 50 | 55.35% |
| Median commission | 5.00% |
| Validators at 0% commission | 235 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.83M | 4.05% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.84M | 3.60% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.35M | 2.81% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.27M | 2.56% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 10.21M | 2.32% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.21M | 2.09% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.14M | 2.08% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.46M | 1.70% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.09M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.56M | 1.49% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.25M | 1.42% | 100.00% |
| 12 | `JD549HsbJHeE...` | 6.23M | 1.42% | 0.00% |
| 13 | `5pPRHniefFjk...` | 5.94M | 1.35% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.62M | 1.28% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.83M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `6DTkuiey2RgM...` | 89.15K | 0 |
| `HDRqPft5ioWZ...` | 71.15K | 0 |
| `t23p8aBQN6P6...` | 14.37K | 447,595,236 |
| `AYY1TCe347UZ...` | 10.71K | 449,555,141 |
| `NWY18yrPHsTo...` | 9.76K | 448,798,710 |
| `mrgn4atx3Jnf...` | 2.26K | 448,597,405 |
| `pSoLoZx55zZz...` | 1.51K | 447,874,752 |
| `HgozywotiKv4...` | 797.43 | 448,492,871 |
| `9fTWmMqVz5cW...` | 23.86 | 448,762,375 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $117.74 |
| SOL 24h | 1.33% |
| SOL 7d | 21.02% |
| SOL 30d | 24.57% |
| Market cap | $69.20B |
| Spot volume 24h | $4.25B |
| Circulating supply | 587.51M SOL |
| Circulating share | 92.59% |
| DeFi TVL | $6.54B |
| TVL 24h | 1.30% |
| TVL 7d | 14.30% |
| Stablecoin supply | $16.54B |
| DEX volume 24h | $3.45B |
| DEX volume 7d | $20.08B |
| Chain fees 24h (REV proxy) | $17.84M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0558, SIMD-0608, SIMD-0550, SIMD-0599, SIMD-0340, SIMD-0433

## Ecosystem news

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)
- [Increase TxV1 Account Lock Limit to 96 (#596)](https://github.com/solana-foundation/solana-improvement-documents/commit/b7ca332f0aabe11ecc6cf36143462d4487d59a39)
- [Release v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0)
- [Release v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
