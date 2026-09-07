# Solana Ecosystem State Report

Generated **2026-09-07T18:45:37Z** in 14.6s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 265 prior runs.

## Anomalies

- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 4.0 robust deviations from its 265-point median of 0.0202, a 379.7% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,030 |
| Epoch progress | 40.89% |
| Epoch time remaining (est.) | 28h 22m |
| Absolute slot | 445,136,666 |
| Block height | 423,180,869 |
| TPS (all) | 4,528.43 |
| TPS (non-vote) | 2,434.87 |
| TPS (30-sample mean) | 4,134.91 |
| Slot time | 320.90 ms |
| Block lag vs wall clock | 12s |
| Lifetime transactions | 546,091,377,275 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 674 |
| Delinquent | 14 |
| Delinquent share of stake | 0.10% |
| Total active stake | 439.48M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.19% |
| Stake in top 20 | 35.45% |
| Stake in top 50 | 55.13% |
| Median commission | 5.00% |
| Validators at 0% commission | 245 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.44M | 3.97% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.34M | 3.72% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.52M | 2.85% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.40M | 2.59% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.56M | 2.18% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.18M | 2.09% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.04M | 2.06% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.38M | 1.68% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.86M | 1.56% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.60M | 1.50% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.12M | 1.39% | 100.00% |
| 12 | `JD549HsbJHeE...` | 6.12M | 1.39% | 0.00% |
| 13 | `5pPRHniefFjk...` | 5.97M | 1.36% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.64M | 1.28% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.85M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7RtC1QgiNVLA...` | 276.02K | 445,133,225 |
| `EATpCzQNs8Bz...` | 100.31K | 445,132,723 |
| `mrgn4atx3Jnf...` | 20.30K | 445,047,030 |
| `xLabscif2DLn...` | 8.89K | 443,788,373 |
| `prt1st4RSxAt...` | 7.04K | 443,486,942 |
| `E4xNK4UwGnMt...` | 6.26K | 443,348,723 |
| `5ZjxMYBbnKd4...` | 3.79K | 443,965,922 |
| `pSoLoZx55zZz...` | 1.51K | 444,539,191 |
| `4GEEKSwuiBHW...` | 1.34K | 443,438,639 |
| `CpdzCVzaR9gj...` | 193.38 | 442,800,351 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $103.75 |
| SOL 24h | -2.47% |
| SOL 7d | 0.13% |
| SOL 30d | 35.91% |
| Market cap | $60.81B |
| Spot volume 24h | $3.29B |
| Circulating supply | 586.17M SOL |
| Circulating share | 92.51% |
| DeFi TVL | $5.91B |
| TVL 24h | -0.01% |
| TVL 7d | 2.04% |
| Stablecoin supply | $16.37B |
| DEX volume 24h | $2.90B |
| DEX volume 7d | $16.07B |
| Chain fees 24h (REV proxy) | $14.66M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0550, SIMD-0599, SIMD-0340, SIMD-0433, SIMD-0553, SIMD-0392, SIMD-0290, SIMD-0565, SIMD-0529

## Ecosystem news

- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic)
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)
- [v1 Transactions and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)
- [# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)
- [Resource and Inclusion Fee: Digging into Data](https://solana.com/news/resource-and-inclusion-fee-digging-into-data)
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)
- [Release v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0)
- [Release v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3)
- [Remove floating point arithmetic from Runtime critical inflation and …](https://github.com/solana-foundation/solana-improvement-documents/commit/4828b2dd994c98032af401acfa20d37688878003)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
