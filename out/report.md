# Solana Ecosystem State Report

Generated **2026-09-09T20:59:08Z** in 9.8s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 250 prior runs.

## Anomalies

- [WARNING] **commission_zero_count** (statistical) - commission_zero_count is 5.1 robust deviations from its 250-point median of 255, a 5.9% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 11.6 robust deviations from its 250-point median of 0.0202, a 1049.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,031 |
| Epoch progress | 73.03% |
| Epoch time remaining (est.) | 12h 56m |
| Absolute slot | 445,707,504 |
| Block height | 423,750,970 |
| TPS (all) | 4,249.55 |
| TPS (non-vote) | 2,148.22 |
| TPS (30-sample mean) | 4,350.92 |
| Slot time | 320.90 ms |
| Block lag vs wall clock | 11s |
| Lifetime transactions | 546,817,286,552 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 673 |
| Delinquent | 15 |
| Delinquent share of stake | 0.23% |
| Total active stake | 438.65M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.25% |
| Stake in top 20 | 35.53% |
| Stake in top 50 | 55.20% |
| Median commission | 5.00% |
| Validators at 0% commission | 240 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.44M | 3.98% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.35M | 3.73% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.53M | 2.86% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.39M | 2.60% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 9.57M | 2.18% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.29M | 2.12% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.03M | 2.06% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.32M | 1.67% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.86M | 1.56% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.60M | 1.51% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.12M | 1.40% | 0.00% |
| 12 | `9jxgosAfHgHz...` | 6.12M | 1.40% | 100.00% |
| 13 | `5pPRHniefFjk...` | 5.97M | 1.36% | 5.00% |
| 14 | `5Cchr1XGEg7d...` | 5.63M | 1.28% | 100.00% |
| 15 | `GnC339vkyXRm...` | 4.83M | 1.10% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `BULKzVM41WAy...` | 315.13K | 445,696,902 |
| `7RtC1QgiNVLA...` | 281.05K | 445,702,813 |
| `5pZvwjSpGYCx...` | 263.75K | 445,695,788 |
| `mrgn2vUPsPyn...` | 90.76K | 445,694,451 |
| `7d7x84jiVtqp...` | 35.22K | 445,704,501 |
| `inWVrrYJ38Vi...` | 9.89K | 445,699,097 |
| `E4xNK4UwGnMt...` | 6.26K | 443,348,723 |
| `prt1st4RSxAt...` | 5.87K | 443,486,942 |
| `xLabscif2DLn...` | 4.17K | 443,788,373 |
| `5ZjxMYBbnKd4...` | 3.21K | 443,965,922 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $102.47 |
| SOL 24h | -0.69% |
| SOL 7d | 3.12% |
| SOL 30d | 34.65% |
| Market cap | $60.04B |
| Spot volume 24h | $2.96B |
| Circulating supply | 586.25M SOL |
| Circulating share | 92.51% |
| DeFi TVL | $5.94B |
| TVL 24h | 0.35% |
| TVL 7d | 5.03% |
| Stablecoin supply | $16.21B |
| DEX volume 24h | $2.71B |
| DEX volume 7d | $16.83B |
| Chain fees 24h (REV proxy) | $16.56M |

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
- [SIMD-0558 - Leader Info Syscall (#621)](https://github.com/solana-foundation/solana-improvement-documents/commit/0616093b2952ed6de52c4a27d66aadd11d48d4f9)
- [Release v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0)
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts (#608)](https://github.com/solana-foundation/solana-improvement-documents/commit/18e2b3626a9339e7726ea5c1b5b07338bbaf1f52)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
