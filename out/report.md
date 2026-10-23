# Solana Ecosystem State Report

Generated **2026-10-23T07:38:09Z** in 7.8s across 15 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 100.0% (14/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1843 is 60% below the trailing median of 4639.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 6.1 robust deviations from its 141-point median of 9, a 100.0% move.
- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 4.8 robust deviations from its 141-point median of 1.096e+08, a 26.6% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 12.9 robust deviations from its 141-point median of 0.0174, a 1597.7% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 8.1 robust deviations from its 141-point median of 126, a 9.5% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 4.8 robust deviations from its 141-point median of 263.2, a 19.1% move.
- [WARNING] **tps_avg_30_samples** (statistical) - tps_avg_30_samples is 6.5 robust deviations from its 141-point median of 4653, a 61.8% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,065 |
| Epoch progress | 64.96% |
| Epoch time remaining (est.) | 16h 49m |
| Absolute slot | 460,360,629 |
| Block height | 438,392,923 |
| TPS (all) | 1,842.62 |
| TPS (non-vote) | 1,842.62 |
| TPS (30-sample mean) | 1,775.88 |
| Slot time | 212.80 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 563,352,430,228 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 656 |
| Delinquent | 20 |
| Delinquent share of stake | 0.30% |
| Total active stake | 438.32M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.38% |
| Stake in top 20 | 35.55% |
| Stake in top 50 | 55.29% |
| Median commission | 5.00% |
| Validators at 0% commission | 221 |
| Validators at 100% commission | 64 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.13M | 3.91% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.97M | 3.64% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.56M | 2.86% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.94M | 2.50% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.73M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.48M | 2.16% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.80M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.61M | 1.51% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.99M | 1.37% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.68M | 1.30% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `EdFUcP2f6j9i...` | 558.47K | 460,079,999 |
| `9GHvMeJ4ZWuA...` | 234.44K | 460,079,999 |
| `SyndicAgdEph...` | 156.88K | 460,079,999 |
| `8nbE53mcKhy7...` | 115.58K | 460,079,999 |
| `uEhHSnCXvWgt...` | 99.96K | 460,079,999 |
| `SANDCxXBbQhv...` | 43.62K | 460,079,999 |
| `ark1hdnnfmus...` | 42.39K | 460,079,999 |
| `2Le6TjeEescF...` | 20.43K | 460,079,999 |
| `9fa5wcqnAQqH...` | 11.73K | 459,643,077 |
| `Xoir1BnQX9Tb...` | 10.27K | 460,079,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $104.55 |
| SOL 24h | 0.22% |
| SOL 7d | -1.57% |
| SOL 30d | -12.06% |
| Market cap | $61.64B |
| Spot volume 24h | $2.16B |
| Circulating supply | 589.65M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.85B |
| TVL 24h | -2.18% |
| TVL 7d | -2.22% |
| Stablecoin supply | $15.68B |
| DEX volume 24h | $2.12B |
| DEX volume 7d | $12.63B |
| Chain fees 24h (REV proxy) | $11.34M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0529, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp…](https://github.com/solana-foundation/solana-improvement-documents/commit/51dbb649da0233481cc40f5640f33fe74d6dbffe)
- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2)
- [SIMD-0648: Unbound LoaderV3 Instruction Data (#648)](https://github.com/solana-foundation/solana-improvement-documents/commit/27ff5a704391d121869dd3bc8cfa8127483329d0)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
