# Solana Ecosystem State Report

Generated **2026-10-28T01:26:31Z** in 9.8s across 15 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 100.0% (14/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 2194 is 52% below the trailing median of 4568.
- [WARNING] **block_lag_seconds** (statistical) - block_lag_seconds is 5.4 robust deviations from its 141-point median of 8, a 100.0% move.
- [WARNING] **delinquent_pct_by_count** (statistical) - delinquent_pct_by_count is 5.8 robust deviations from its 141-point median of 1.611, a 160.6% move.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 32.1 robust deviations from its 141-point median of 0.0206, a 4201.0% move.
- [WARNING] **validators_delinquent** (statistical) - validators_delinquent is 6.1 robust deviations from its 141-point median of 11, a 163.6% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,070 |
| Epoch progress | 11.52% |
| Epoch time remaining (est.) | 42h 28m |
| Absolute slot | 462,289,768 |
| Block height | 440,314,460 |
| TPS (all) | 2,193.75 |
| TPS (non-vote) | 2,193.75 |
| TPS (30-sample mean) | 2,033.39 |
| Slot time | 210.50 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 564,079,045,971 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 662 |
| Delinquent | 29 |
| Delinquent share of stake | 0.89% |
| Total active stake | 437.29M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.57% |
| Stake in top 20 | 35.70% |
| Stake in top 50 | 55.35% |
| Median commission | 5.00% |
| Validators at 0% commission | 230 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.01M | 3.89% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.66M | 3.81% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.79M | 2.93% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.82M | 2.47% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.72M | 2.22% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.46M | 2.16% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.21M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.76M | 1.77% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.04M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 7.00M | 1.60% | 0.00% |
| 11 | `5pPRHniefFjk...` | 6.11M | 1.40% | 5.00% |
| 12 | `JD549HsbJHeE...` | 6.05M | 1.38% | 0.00% |
| 13 | `5Cchr1XGEg7d...` | 5.71M | 1.31% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.86M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.73M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `722RdWmHC5TG...` | 1.56M | 462,239,999 |
| `7cVfgArCheMR...` | 1.19M | 462,239,999 |
| `BXAxLMMMUNYf...` | 794.31K | 462,239,999 |
| `2dfgsiSaZ51Q...` | 292.98K | 462,239,999 |
| `ssx2rHZNVy6J...` | 35.70K | 462,239,999 |
| `HzrEstnLfzsi...` | 2.61K | 461,807,999 |
| `GqDCbnafLmKk...` | 397.56 | 460,079,999 |
| `JDvwML44fiV2...` | 290.16 | 0 |
| `SANDCxXBbQhv...` | 181.00 | 460,079,999 |
| `Eu6FQvMfaVav...` | 4.49 | 460,079,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $101.26 |
| SOL 24h | 0.83% |
| SOL 7d | -4.96% |
| SOL 30d | -16.79% |
| Market cap | $59.73B |
| Spot volume 24h | $2.02B |
| Circulating supply | 589.93M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.69B |
| TVL 24h | -0.00% |
| TVL 7d | -4.59% |
| Stablecoin supply | $15.51B |
| DEX volume 24h | $1.85B |
| DEX volume 7d | $11.94B |
| Chain fees 24h (REV proxy) | $11.07M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0675, SIMD-0123, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0529, SIMD-0648, SIMD-0565, SIMD-0504, SIMD-0686, SIMD-0688, SIMD-0684, SIMD-0464, SIMD-0376, SIMD-0215

## Ecosystem news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Breakpoint 2026 Adds Revolut Chair, Former Prime Minister, Former Chancellor and City Leaders to London Lineup](https://solana.com/news/breakpoint-london-lineup)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026)
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4)
- [v4.5.0-alpha.3: Bump version to 4.5.0-alpha.3 (#16402)](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.3)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
