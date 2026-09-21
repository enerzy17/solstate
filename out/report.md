# Solana Ecosystem State Report

Generated **2026-09-21T19:32:07Z** in 7.8s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 171 prior runs.

## Anomalies

- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 4.9 robust deviations from its 171-point median of 317.5, a 15.2% move.
- [WARNING] **tvl_usd** (statistical) - tvl_usd is 4.1 robust deviations from its 171-point median of 5.839e+09, a 10.8% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,039 |
| Epoch progress | 69.94% |
| Epoch time remaining (est.) | 14h 25m |
| Absolute slot | 449,150,154 |
| Block height | 427,190,750 |
| TPS (all) | 4,983.50 |
| TPS (non-vote) | 2,474.23 |
| TPS (30-sample mean) | 5,023.44 |
| Slot time | 269.10 ms |
| Block lag vs wall clock | 9s |
| Lifetime transactions | 551,050,145,326 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 675 |
| Delinquent | 15 |
| Delinquent share of stake | 0.09% |
| Total active stake | 439.91M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.26% |
| Stake in top 20 | 35.60% |
| Stake in top 50 | 55.30% |
| Median commission | 5.00% |
| Validators at 0% commission | 239 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.86M | 4.06% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.83M | 3.60% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.52M | 2.85% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.25M | 2.56% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.79M | 2.23% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.25M | 2.10% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.11M | 2.07% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.44M | 1.69% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.09M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.57M | 1.49% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.38M | 1.45% | 100.00% |
| 12 | `JD549HsbJHeE...` | 6.21M | 1.41% | 0.00% |
| 13 | `5pPRHniefFjk...` | 5.96M | 1.35% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.65M | 1.28% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.84M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `1ggyZGbYtEo1...` | 177.53K | 449,147,455 |
| `6DTkuiey2RgM...` | 89.15K | 0 |
| `HDRqPft5ioWZ...` | 71.15K | 0 |
| `t23p8aBQN6P6...` | 14.48K | 447,595,236 |
| `AYY1TCe347UZ...` | 10.81K | 449,084,940 |
| `NWY18yrPHsTo...` | 9.76K | 448,798,710 |
| `mrgn4atx3Jnf...` | 2.26K | 448,597,405 |
| `pSoLoZx55zZz...` | 1.51K | 447,874,752 |
| `HgozywotiKv4...` | 797.43 | 448,492,871 |
| `EWARp8Syq8cT...` | 64.91 | 446,995,996 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $117.82 |
| SOL 24h | 7.13% |
| SOL 7d | 13.72% |
| SOL 30d | 24.81% |
| Market cap | $69.22B |
| Spot volume 24h | $6.44B |
| Circulating supply | 587.44M SOL |
| Circulating share | 92.59% |
| DeFi TVL | $6.47B |
| TVL 24h | 4.78% |
| TVL 7d | 10.90% |
| Stablecoin supply | $16.06B |
| DEX volume 24h | $2.80B |
| DEX volume 7d | $19.83B |
| Chain fees 24h (REV proxy) | $14.46M |

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
