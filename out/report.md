# Solana Ecosystem State Report

Generated **2026-09-15T04:59:56Z** in 9.1s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 217 prior runs.

## Anomalies

- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 17.2 robust deviations from its 217-point median of 0.0323, a 1728.2% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,035 |
| Epoch progress | 10.34% |
| Epoch time remaining (est.) | 43h 2m |
| Absolute slot | 447,164,663 |
| Block height | 425,206,619 |
| TPS (all) | 3,610.70 |
| TPS (non-vote) | 1,444.03 |
| TPS (30-sample mean) | 3,516.74 |
| Slot time | 312.50 ms |
| Block lag vs wall clock | 11s |
| Lifetime transactions | 548,592,443,480 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 679 |
| Delinquent | 10 |
| Delinquent share of stake | 0.59% |
| Total active stake | 439.25M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.32% |
| Stake in top 20 | 35.56% |
| Stake in top 50 | 55.20% |
| Median commission | 5.00% |
| Validators at 0% commission | 244 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.76M | 4.04% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.37M | 3.73% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.49M | 2.84% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.37M | 2.59% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.67M | 2.20% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.26M | 2.11% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.04M | 2.06% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.37M | 1.68% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.94M | 1.58% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.55M | 1.49% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.11M | 1.39% | 100.00% |
| 12 | `5pPRHniefFjk...` | 5.96M | 1.36% | 5.00% |
| 13 | `JD549HsbJHeE...` | 5.88M | 1.34% | 0.00% |
| 14 | `5Cchr1XGEg7d...` | 5.65M | 1.29% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.84M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `ana2y2YvQ3ZP...` | 2.45M | 447,164,099 |
| `FGiEdzde7Fco...` | 128.30K | 446,560,438 |
| `AYY1TCe347UZ...` | 10.81K | 446,874,801 |
| `pSoLoZx55zZz...` | 1.51K | 447,044,285 |
| `4GEEKSwuiBHW...` | 196.81 | 445,809,612 |
| `EWARp8Syq8cT...` | 99.64 | 446,995,996 |
| `inWVrrYJ38Vi...` | 14.05 | 445,699,097 |
| `R1parD2CtxPB...` | 1.63 | 384,048,870 |
| `Fb77sbwgXmtj...` | 1.08 | 446,256,027 |
| `4kdjgZKJUwPK...` | 1.05 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $101.27 |
| SOL 24h | 0.21% |
| SOL 7d | -1.97% |
| SOL 30d | 34.09% |
| Market cap | $59.45B |
| Spot volume 24h | $3.31B |
| Circulating supply | 587.03M SOL |
| Circulating share | 92.57% |
| DeFi TVL | $5.89B |
| TVL 24h | 0.96% |
| TVL 7d | -0.56% |
| Stablecoin supply | $16.07B |
| DEX volume 24h | $2.21B |
| DEX volume 7d | $17.14B |
| Chain fees 24h (REV proxy) | $13.55M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0558, SIMD-0608, SIMD-0550, SIMD-0599, SIMD-0340, SIMD-0433, SIMD-0553, SIMD-0392, SIMD-0290, SIMD-0565

## Ecosystem news

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)
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
