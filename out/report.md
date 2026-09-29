# Solana Ecosystem State Report

Generated **2026-09-29T06:47:57Z** in 11.8s across 15 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 100.0% (14/14 probes returned data). History depth: 145 prior runs.

## Anomalies

- [WARNING] **commission_zero_count** (statistical) - commission_zero_count is 4.4 robust deviations from its 145-point median of 242, a 5.4% move.
- [WARNING] **slot_time_ms** (statistical) - slot_time_ms is 4.8 robust deviations from its 145-point median of 312.5, a 15.0% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,045 |
| Epoch progress | 29.00% |
| Epoch time remaining (est.) | 34h 4m |
| Absolute slot | 451,565,261 |
| Block height | 429,604,825 |
| TPS (all) | 3,780.40 |
| TPS (non-vote) | 1,247.48 |
| TPS (30-sample mean) | 3,786.34 |
| Slot time | 265.50 ms |
| Block lag vs wall clock | 10s |
| Lifetime transactions | 553,946,005,762 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 675 |
| Delinquent | 7 |
| Delinquent share of stake | 0.01% |
| Total active stake | 441.25M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.45% |
| Stake in top 20 | 35.33% |
| Stake in top 50 | 55.04% |
| Median commission | 5.00% |
| Validators at 0% commission | 229 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.82M | 4.04% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 15.89M | 3.60% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.34M | 2.80% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 11.30M | 2.56% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 11.21M | 2.54% | 5.00% |
| 6 | `C8Bey3LKVJHV...` | 9.24M | 2.09% | 7.00% |
| 7 | `CAo1dCGYrB6N...` | 9.22M | 2.09% | 10.00% |
| 8 | `EvnRmnMrd69k...` | 7.64M | 1.73% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.70M | 1.52% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.52M | 1.48% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.27M | 1.42% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.92M | 1.34% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.63M | 1.27% | 100.00% |
| 14 | `9rkJMARqK6VB...` | 4.70M | 1.07% | 8.00% |
| 15 | `GnC339vkyXRm...` | 4.63M | 1.05% | 7.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `4YGgmwyqztpJ...` | 12.74K | 450,345,071 |
| `AYY1TCe347UZ...` | 10.70K | 451,520,406 |
| `ARKk6RgiFq4M...` | 63.93 | 450,022,154 |
| `R1parD2CtxPB...` | 2.87 | 384,048,870 |
| `6mygxmZxmTqq...` | 2.00 | 451,518,013 |
| `CQYPRQ4vqn8e...` | 1.00 | 451,558,327 |
| `AEAJtnjjB19X...` | 1.00 | 451,436,763 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $118.94 |
| SOL 24h | 0.10% |
| SOL 7d | 1.76% |
| SOL 30d | 13.22% |
| Market cap | $69.90B |
| Spot volume 24h | $3.72B |
| Circulating supply | 587.85M SOL |
| Circulating share | 92.59% |
| DeFi TVL | $6.44B |
| TVL 24h | -2.98% |
| TVL 7d | -0.28% |
| Stablecoin supply | $16.21B |
| DEX volume 24h | $2.29B |
| DEX volume 7d | $16.34B |
| Chain fees 24h (REV proxy) | $17.45M |

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
- [Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1)
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
