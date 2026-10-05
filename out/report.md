# Solana Ecosystem State Report

Generated **2026-10-05T05:49:38Z** in 11.4s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 156 prior runs.

## Anomalies

- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 12.4 robust deviations from its 156-point median of 0.0365, a 929.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,049 |
| Epoch progress | 74.44% |
| Epoch time remaining (est.) | 12h 16m |
| Absolute slot | 453,489,599 |
| Block height | 431,527,809 |
| TPS (all) | 3,991.20 |
| TPS (non-vote) | 1,447.30 |
| TPS (30-sample mean) | 4,020.44 |
| Slot time | 260.90 ms |
| Block lag vs wall clock | 10s |
| Lifetime transactions | 556,245,554,231 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 670 |
| Delinquent | 16 |
| Delinquent share of stake | 0.38% |
| Total active stake | 441.85M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.56% |
| Stake in top 20 | 35.47% |
| Stake in top 50 | 55.16% |
| Median commission | 5.00% |
| Validators at 0% commission | 228 |
| Validators at 100% commission | 64 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.94M | 4.06% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.93M | 3.60% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.35M | 2.79% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 11.31M | 2.56% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 11.14M | 2.52% | 5.00% |
| 6 | `C8Bey3LKVJHV...` | 9.25M | 2.09% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.24M | 2.09% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.62M | 1.72% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.06M | 1.60% | 5.00% |
| 10 | `JD549HsbJHeE...` | 6.69M | 1.51% | 0.00% |
| 11 | `Awes4Tr6TX8J...` | 6.50M | 1.47% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.93M | 1.34% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.64M | 1.28% | 100.00% |
| 14 | `9rkJMARqK6VB...` | 4.70M | 1.06% | 8.00% |
| 15 | `GnC339vkyXRm...` | 4.63M | 1.05% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `BkoS26vBuaXn...` | 1.54M | 453,462,364 |
| `vtav4QSdUYDb...` | 63.85K | 453,020,473 |
| `LandXx5ebB8B...` | 29.39K | 452,980,806 |
| `AccReGBNBdUC...` | 14.01K | 451,953,922 |
| `AYY1TCe347UZ...` | 10.70K | 452,491,297 |
| `ECNnK4VjcKTs...` | 1.30K | 451,647,060 |
| `8Cia7Yc8QzCd...` | 639.61 | 451,830,270 |
| `VicAQ3U2GjjA...` | 283.66 | 451,647,273 |
| `4YGgmwyqztpJ...` | 63.19 | 450,345,071 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $120.44 |
| SOL 24h | -0.39% |
| SOL 7d | 0.39% |
| SOL 30d | 18.34% |
| Market cap | $70.86B |
| Spot volume 24h | $2.32B |
| Circulating supply | 588.31M SOL |
| Circulating share | 92.61% |
| DeFi TVL | $6.71B |
| TVL 24h | 1.43% |
| TVL 7d | 1.09% |
| Stablecoin supply | $16.52B |
| DEX volume 24h | $1.65B |
| DEX volume 7d | $15.58B |
| Chain fees 24h (REV proxy) | $15.99M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0376, SIMD-0215, SIMD-0558, SIMD-0582, SIMD-0377, SIMD-0609, SIMD-0610, SIMD-0608, SIMD-0550, SIMD-0599

## Ecosystem news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)
- [Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)
- [Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1)
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)
- [Release v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1)
- [Release v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0)
- [Amend simd 0376 ed25519-zebra verification (#616)](https://github.com/solana-foundation/solana-improvement-documents/commit/4b643ca8746742183a469681765e694b385bb315)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
