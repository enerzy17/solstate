# Solana Ecosystem State Report

Generated **2026-09-10T20:55:50Z** in 11.5s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 244 prior runs.

## Anomalies

- [WARNING] **commission_zero_count** (statistical) - commission_zero_count is 5.1 robust deviations from its 244-point median of 255, a 5.9% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 29.3 robust deviations from its 244-point median of 0.0221, a 2527.1% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,032 |
| Epoch progress | 36.14% |
| Epoch time remaining (est.) | 30h 39m |
| Absolute slot | 445,980,104 |
| Block height | 424,023,439 |
| TPS (all) | 3,887.65 |
| TPS (non-vote) | 1,730.37 |
| TPS (30-sample mean) | 3,908.82 |
| Slot time | 312.50 ms |
| Block lag vs wall clock | 12s |
| Lifetime transactions | 547,162,036,431 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 676 |
| Delinquent | 13 |
| Delinquent share of stake | 0.58% |
| Total active stake | 439.19M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.21% |
| Stake in top 20 | 35.48% |
| Stake in top 50 | 55.08% |
| Median commission | 5.00% |
| Validators at 0% commission | 240 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.44M | 3.97% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.32M | 3.72% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.52M | 2.85% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.38M | 2.59% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.57M | 2.18% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.28M | 2.11% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.04M | 2.06% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.34M | 1.67% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.88M | 1.57% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.55M | 1.49% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.12M | 1.39% | 0.00% |
| 12 | `9jxgosAfHgHz...` | 6.12M | 1.39% | 100.00% |
| 13 | `5pPRHniefFjk...` | 5.95M | 1.35% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.63M | 1.28% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.83M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `ana2y2YvQ3ZP...` | 2.44M | 445,978,724 |
| `scs2Ra91pMbv...` | 58.59K | 445,879,082 |
| `mrgn4atx3Jnf...` | 19.89K | 445,964,239 |
| `AYY1TCe347UZ...` | 10.81K | 445,854,157 |
| `inWVrrYJ38Vi...` | 8.46K | 445,699,097 |
| `xLabscif2DLn...` | 3.36K | 443,788,373 |
| `5ZjxMYBbnKd4...` | 3.21K | 443,965,922 |
| `pSoLoZx55zZz...` | 1.51K | 445,795,162 |
| `4GEEKSwuiBHW...` | 326.50 | 445,809,612 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $100.04 |
| SOL 24h | -2.22% |
| SOL 7d | -4.90% |
| SOL 30d | 32.31% |
| Market cap | $58.65B |
| Spot volume 24h | $3.24B |
| Circulating supply | 586.34M SOL |
| Circulating share | 92.51% |
| DeFi TVL | $5.78B |
| TVL 24h | -2.89% |
| TVL 7d | 1.21% |
| Stablecoin supply | $15.95B |
| DEX volume 24h | $3.00B |
| DEX volume 7d | $17.54B |
| Chain fees 24h (REV proxy) | $15.72M |

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
- [Release v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4)
- [SIMD-0558 - Leader Info Syscall (#621)](https://github.com/solana-foundation/solana-improvement-documents/commit/0616093b2952ed6de52c4a27d66aadd11d48d4f9)
- [Release v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
