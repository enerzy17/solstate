# Solana Ecosystem State Report

Generated **2026-10-14T01:16:05Z** in 10.9s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 141 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 3.8 robust deviations from its 141-point median of 1.101e+08, a 18.4% move.
- [WARNING] **dex_protocols_tracked** (statistical) - dex_protocols_tracked is 4.7 robust deviations from its 141-point median of 126, a 5.6% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 8.9 robust deviations from its 141-point median of 266.7, a 17.3% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,057 |
| Epoch progress | 6.64% |
| Epoch time remaining (est.) | 44h 48m |
| Absolute slot | 456,652,691 |
| Block height | 434,689,019 |
| TPS (all) | 5,152.07 |
| TPS (non-vote) | 2,114.33 |
| TPS (30-sample mean) | 4,911.35 |
| Slot time | 220.60 ms |
| Block lag vs wall clock | 8s |
| Lifetime transactions | 559,823,711,489 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 673 |
| Delinquent | 5 |
| Delinquent share of stake | 0.00% |
| Total active stake | 438.13M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.59% |
| Stake in top 20 | 35.72% |
| Stake in top 50 | 55.50% |
| Median commission | 5.00% |
| Validators at 0% commission | 230 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.79M | 4.06% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.83M | 3.61% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.31M | 2.81% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 11.14M | 2.54% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 10.76M | 2.46% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.41M | 2.15% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.11% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.70M | 1.76% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.91M | 1.58% | 5.00% |
| 10 | `JD549HsbJHeE...` | 6.64M | 1.52% | 0.00% |
| 11 | `Awes4Tr6TX8J...` | 6.41M | 1.46% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.96M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.67M | 1.29% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.87M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.71M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `tboxdsRMjUfY...` | 4.47K | 455,988,360 |
| `rssaJ2iKcE9Q...` | 1.55K | 456,203,301 |
| `9bjXFvs3ygxH...` | 5.00 | 0 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |
| `6mygxmZxmTqq...` | 2.00 | 456,290,998 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $107.33 |
| SOL 24h | 3.34% |
| SOL 7d | -10.97% |
| SOL 30d | 7.73% |
| Market cap | $63.21B |
| Spot volume 24h | $3.17B |
| Circulating supply | 589.22M SOL |
| Circulating share | 92.68% |
| DeFi TVL | $6.03B |
| TVL 24h | -3.04% |
| TVL 7d | -10.65% |
| Stablecoin supply | $16.21B |
| DEX volume 24h | $2.28B |
| DEX volume 7d | $12.91B |
| Chain fees 24h (REV proxy) | $11.69M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0464, SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)
- [Solana Changelog: September 24, 2026](https://solana.com/news/solana-changelog-september-24-2026)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1)
- [Release v4.3.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.1)
- [Release v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
