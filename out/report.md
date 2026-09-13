# Solana Ecosystem State Report

Generated **2026-09-13T11:58:58Z** in 8.6s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 231 prior runs.

## Anomalies

- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 16.9 robust deviations from its 231-point median of 0.0242, a 1588.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,034 |
| Epoch progress | 2.15% |
| Epoch time remaining (est.) | 46h 58m |
| Absolute slot | 446,697,282 |
| Block height | 424,739,940 |
| TPS (all) | 3,065.30 |
| TPS (non-vote) | 940.37 |
| TPS (30-sample mean) | 3,382.43 |
| Slot time | 315.80 ms |
| Block lag vs wall clock | 12s |
| Lifetime transactions | 548,022,689,394 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 677 |
| Delinquent | 12 |
| Delinquent share of stake | 0.41% |
| Total active stake | 438.74M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.29% |
| Stake in top 20 | 35.52% |
| Stake in top 50 | 55.20% |
| Median commission | 5.00% |
| Validators at 0% commission | 243 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.57M | 4.00% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.36M | 3.73% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.50M | 2.85% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.37M | 2.59% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.62M | 2.19% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.25M | 2.11% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.03M | 2.06% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.37M | 1.68% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.94M | 1.58% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.55M | 1.49% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.12M | 1.40% | 100.00% |
| 12 | `5pPRHniefFjk...` | 5.96M | 1.36% | 5.00% |
| 13 | `JD549HsbJHeE...` | 5.88M | 1.34% | 0.00% |
| 14 | `5Cchr1XGEg7d...` | 5.63M | 1.28% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.83M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `pSo1KZXgG1EG...` | 1.63M | 446,256,027 |
| `FGiEdzde7Fco...` | 128.30K | 446,560,438 |
| `mrgn4atx3Jnf...` | 19.58K | 446,552,232 |
| `AYY1TCe347UZ...` | 10.81K | 446,256,027 |
| `pSoLoZx55zZz...` | 1.51K | 446,256,027 |
| `4GEEKSwuiBHW...` | 196.81 | 445,809,612 |
| `EWARp8Syq8cT...` | 99.63 | 446,691,993 |
| `inWVrrYJ38Vi...` | 14.05 | 445,699,097 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $99.80 |
| SOL 24h | -2.25% |
| SOL 7d | -6.39% |
| SOL 30d | 32.49% |
| Market cap | $58.56B |
| Spot volume 24h | $1.83B |
| Circulating supply | 586.73M SOL |
| Circulating share | 92.54% |
| DeFi TVL | $5.83B |
| TVL 24h | -1.10% |
| TVL 7d | -1.42% |
| Stablecoin supply | $16.16B |
| DEX volume 24h | $1.69B |
| DEX volume 7d | $19.13B |
| Chain fees 24h (REV proxy) | $13.52M |

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
