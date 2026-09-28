# Solana Ecosystem State Report

Generated **2026-09-28T20:35:33Z** in 9.5s across 15 HTTP calls.

> **Status:** 3 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 143 prior runs.

## Anomalies

- [WARNING] **commission_zero_count** (statistical) - commission_zero_count is 4.7 robust deviations from its 143-point median of 242, a 5.8% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 5.9 robust deviations from its 143-point median of 312.5, a 13.9% move.
- [WARNING] **tvl_usd** (statistical) - tvl_usd is 4.1 robust deviations from its 143-point median of 5.914e+09, a 11.2% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,044 |
| Epoch progress | 97.22% |
| Epoch time remaining (est.) | 1h 20m |
| Absolute slot | 451,427,970 |
| Block height | 429,467,600 |
| TPS (all) | 4,677.07 |
| TPS (non-vote) | 2,173.08 |
| TPS (30-sample mean) | 5,016.43 |
| Slot time | 269.10 ms |
| Block lag vs wall clock | 9s |
| Lifetime transactions | 553,787,142,448 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 676 |
| Delinquent | 7 |
| Delinquent share of stake | 0.01% |
| Total active stake | 440.55M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.46% |
| Stake in top 20 | 35.37% |
| Stake in top 50 | 55.09% |
| Median commission | 5.00% |
| Validators at 0% commission | 228 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.87M | 4.06% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.84M | 3.60% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.33M | 2.80% | 0.00% |
| 4 | `JUPiTERrZqgf...` | 11.22M | 2.55% | 5.00% |
| 5 | `E1r4Psq84tHf...` | 10.84M | 2.46% | 0.00% |
| 6 | `C8Bey3LKVJHV...` | 9.24M | 2.10% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.21M | 2.09% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.62M | 1.73% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.09M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.51M | 1.48% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.27M | 1.42% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.91M | 1.34% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.63M | 1.28% | 100.00% |
| 14 | `9rkJMARqK6VB...` | 4.70M | 1.07% | 8.00% |
| 15 | `GnC339vkyXRm...` | 4.62M | 1.05% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `4YGgmwyqztpJ...` | 12.74K | 450,345,071 |
| `AYY1TCe347UZ...` | 10.70K | 451,280,677 |
| `ARKk6RgiFq4M...` | 63.93 | 450,022,154 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `6mygxmZxmTqq...` | 2.00 | 451,196,568 |
| `CZMekcZwyKLC...` | 1.00 | 0 |
| `CQYPRQ4vqn8e...` | 1.00 | 451,396,967 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $118.86 |
| SOL 24h | -3.24% |
| SOL 7d | 0.47% |
| SOL 30d | 12.81% |
| Market cap | $69.87B |
| Spot volume 24h | $4.14B |
| Circulating supply | 587.78M SOL |
| Circulating share | 92.59% |
| DeFi TVL | $6.58B |
| TVL 24h | -0.73% |
| TVL 7d | 5.97% |
| Stablecoin supply | $16.40B |
| DEX volume 24h | $1.93B |
| DEX volume 7d | $18.32B |
| Chain fees 24h (REV proxy) | $15.42M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550, SIMD-0599

## Ecosystem news

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)
- [Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)
- [Release v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0)
- [Amend simd 0376 ed25519-zebra verification (#616)](https://github.com/solana-foundation/solana-improvement-documents/commit/4b643ca8746742183a469681765e694b385bb315)
- [SIMD-0215: clarify LtHash security considerations (#669)](https://github.com/solana-foundation/solana-improvement-documents/commit/f1afd941b9fa5061ea80a5401feb72172121ebb5)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
