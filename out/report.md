# Solana Ecosystem State Report

Generated **2026-09-12T22:21:51Z** in 13.4s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 233 prior runs.

## Anomalies

- [WARNING] **commission_zero_count** (statistical) - commission_zero_count is 4.4 robust deviations from its 233-point median of 255, a 5.1% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 16.1 robust deviations from its 233-point median of 0.023, a 1572.6% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,033 |
| Epoch progress | 66.15% |
| Epoch time remaining (est.) | 16h 14m |
| Absolute slot | 446,541,772 |
| Block height | 424,584,500 |
| TPS (all) | 3,356.08 |
| TPS (non-vote) | 1,203.47 |
| TPS (30-sample mean) | 3,661.07 |
| Slot time | 314.10 ms |
| Block lag vs wall clock | 12s |
| Lifetime transactions | 547,850,052,990 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 679 |
| Delinquent | 11 |
| Delinquent share of stake | 0.38% |
| Total active stake | 436.84M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.40% |
| Stake in top 20 | 35.72% |
| Stake in top 50 | 55.49% |
| Median commission | 5.00% |
| Validators at 0% commission | 242 |
| Validators at 100% commission | 66 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.56M | 4.02% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.36M | 3.75% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.52M | 2.87% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.37M | 2.60% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.67M | 2.21% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.23M | 2.11% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.02M | 2.07% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.36M | 1.68% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.94M | 1.59% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.55M | 1.50% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.13M | 1.40% | 0.00% |
| 12 | `9jxgosAfHgHz...` | 6.12M | 1.40% | 100.00% |
| 13 | `5pPRHniefFjk...` | 5.96M | 1.36% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.62M | 1.29% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.83M | 1.11% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `pSo1KZXgG1EG...` | 1.64M | 446,256,027 |
| `EWARp8Syq8cT...` | 31.93K | 446,424,161 |
| `AYY1TCe347UZ...` | 10.81K | 446,256,027 |
| `pSoLoZx55zZz...` | 1.51K | 446,256,027 |
| `4GEEKSwuiBHW...` | 326.50 | 445,809,612 |
| `inWVrrYJ38Vi...` | 14.05 | 445,699,097 |
| `6mygxmZxmTqq...` | 2.00 | 0 |
| `R1parD2CtxPB...` | 1.63 | 384,048,870 |
| `Fb77sbwgXmtj...` | 1.08 | 446,256,027 |
| `4kdjgZKJUwPK...` | 1.05 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $101.65 |
| SOL 24h | -0.41% |
| SOL 7d | -2.00% |
| SOL 30d | 33.49% |
| Market cap | $59.63B |
| Spot volume 24h | $1.92B |
| Circulating supply | 586.63M SOL |
| Circulating share | 92.54% |
| DeFi TVL | $5.90B |
| TVL 24h | 2.53% |
| TVL 7d | 0.42% |
| Stablecoin supply | $16.22B |
| DEX volume 24h | $3.18B |
| DEX volume 7d | $19.31B |
| Chain fees 24h (REV proxy) | $17.88M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0558, SIMD-0608, SIMD-0550, SIMD-0599, SIMD-0340, SIMD-0433, SIMD-0553, SIMD-0392, SIMD-0290, SIMD-0565

## Ecosystem news

- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic)
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)
- [Resource and Inclusion Fee: Digging into Data](https://solana.com/news/resource-and-inclusion-fee-digging-into-data)
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)
- [Release v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1)
- [Release v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4)
- [SIMD-0558 - Leader Info Syscall (#621)](https://github.com/solana-foundation/solana-improvement-documents/commit/0616093b2952ed6de52c4a27d66aadd11d48d4f9)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
