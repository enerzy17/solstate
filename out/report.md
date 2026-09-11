# Solana Ecosystem State Report

Generated **2026-09-11T11:29:20Z** in 7.4s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 243 prior runs.

## Anomalies

- [WARNING] **commission_zero_count** (statistical) - commission_zero_count is 5.7 robust deviations from its 243-point median of 255, a 6.7% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 20.4 robust deviations from its 243-point median of 0.023, a 1851.7% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,032 |
| Epoch progress | 74.51% |
| Epoch time remaining (est.) | 12h 14m |
| Absolute slot | 446,145,876 |
| Block height | 424,189,086 |
| TPS (all) | 3,985.47 |
| TPS (non-vote) | 1,887.93 |
| TPS (30-sample mean) | 3,993.57 |
| Slot time | 320.90 ms |
| Block lag vs wall clock | 11s |
| Lifetime transactions | 547,357,328,734 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 673 |
| Delinquent | 16 |
| Delinquent share of stake | 0.45% |
| Total active stake | 439.19M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.21% |
| Stake in top 20 | 35.48% |
| Stake in top 50 | 55.13% |
| Median commission | 5.00% |
| Validators at 0% commission | 238 |
| Validators at 100% commission | 65 |

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
| `pSo1KZXgG1EG...` | 1.64M | 446,093,575 |
| `EBk678aQvc3c...` | 95.16K | 446,087,868 |
| `mrgn2vUPsPyn...` | 90.78K | 446,141,645 |
| `scs2Ra91pMbv...` | 58.59K | 445,879,082 |
| `EWARp8Syq8cT...` | 35.14K | 446,141,354 |
| `mrgn4atx3Jnf...` | 19.89K | 446,139,556 |
| `AYY1TCe347UZ...` | 10.81K | 445,854,157 |
| `inWVrrYJ38Vi...` | 8.46K | 445,699,097 |
| `xLabscif2DLn...` | 3.36K | 443,788,373 |
| `5ZjxMYBbnKd4...` | 3.21K | 443,965,922 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $98.98 |
| SOL 24h | -2.23% |
| SOL 7d | -4.92% |
| SOL 30d | 29.02% |
| Market cap | $58.05B |
| Spot volume 24h | $3.04B |
| Circulating supply | 586.54M SOL |
| Circulating share | 92.54% |
| DeFi TVL | $5.80B |
| TVL 24h | -0.90% |
| TVL 7d | -2.15% |
| Stablecoin supply | $15.99B |
| DEX volume 24h | $2.95B |
| DEX volume 7d | $16.62B |
| Chain fees 24h (REV proxy) | $14.81M |

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
