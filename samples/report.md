# Solana Ecosystem State Report

Generated **2026-08-03T23:05:32Z** in 11.1s across 15 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 100.0% (14/14 probes returned data). History depth: 11 prior runs.

## Anomalies

- [WARNING] **sol_change_7d_pct** (statistical) - sol_change_7d_pct is 60.0 robust deviations from its 11-point median of -2.51, a 70.9% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,011 |
| Epoch progress | 71.50% |
| Epoch time remaining (est.) | 13h 40m |
| Absolute slot | 437,060,871 |
| Block height | 415,115,793 |
| TPS (all) | 3,704.98 |
| TPS (non-vote) | 2,124.93 |
| TPS (30-sample mean) | 3,714.39 |
| Slot time | 431.70 ms |
| Block lag vs wall clock | 13s |
| Lifetime transactions | 534,858,800,331 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 691 |
| Delinquent | 12 |
| Delinquent share of stake | 0.13% |
| Total active stake | 432.65M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.41% |
| Stake in top 20 | 35.71% |
| Stake in top 50 | 55.40% |
| Median commission | 5.00% |
| Validators at 0% commission | 260 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 16.80M | 3.88% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.03M | 3.70% | 0.00% |
| 3 | `JUPiTERrZqgf...` | 12.54M | 2.90% | 5.00% |
| 4 | `DRpbCBMxVnDK...` | 12.26M | 2.83% | 0.00% |
| 5 | `q9XWcZ7T1wP4...` | 9.15M | 2.12% | 7.00% |
| 6 | `CAo1dCGYrB6N...` | 8.82M | 2.04% | 10.00% |
| 7 | `E1r4Psq84tHf...` | 8.15M | 1.88% | 0.00% |
| 8 | `EvnRmnMrd69k...` | 7.92M | 1.83% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 7.30M | 1.69% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.65M | 1.54% | 0.00% |
| 11 | `9jxgosAfHgHz...` | 6.12M | 1.42% | 100.00% |
| 12 | `5pPRHniefFjk...` | 5.91M | 1.36% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.77M | 1.33% | 100.00% |
| 14 | `JD549HsbJHeE...` | 5.75M | 1.33% | 0.00% |
| 15 | `9rkJMARqK6VB...` | 4.63M | 1.07% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7RtC1QgiNVLA...` | 274.84K | 436,844,203 |
| `AoUwfPuiEek2...` | 268.12K | 435,023,998 |
| `6c6RrC9TWNgi...` | 1.25K | 435,006,439 |
| `3iQqh65Gby53...` | 389.68 | 436,812,576 |
| `BirdeyeK5yoo...` | 127.40 | 435,360,263 |
| `5HCTsoKM7vwj...` | 121.83 | 435,891,365 |
| `8cnksBVjDPsp...` | 116.73 | 434,612,175 |
| `32jCuWyy4aJj...` | 2.70 | 436,736,029 |
| `7Hp1e6BrTBkb...` | 2.00 | 435,239,778 |
| `R1parD2CtxPB...` | 1.61 | 384,048,870 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $73.40 |
| SOL 24h | -0.20% |
| SOL 7d | -0.73% |
| SOL 30d | -10.32% |
| Market cap | $42.66B |
| Spot volume 24h | $1.40B |
| Circulating supply | 581.19M SOL |
| Circulating share | 92.03% |
| DeFi TVL | $4.77B |
| TVL 24h | 1.41% |
| TVL 7d | -2.75% |
| Stablecoin supply | $15.82B |
| DEX volume 24h | $1.34B |
| DEX volume 7d | $11.46B |
| Chain fees 24h (REV proxy) | $7.51M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0286, SIMD-0340, SIMD-0433, SIMD-0550, SIMD-0553, SIMD-0392, SIMD-0290, SIMD-0565, SIMD-0529, SIMD-0525, SIMD-0022

## Ecosystem news

- [How External Assets Start Trading on Solana From Day One](https://solana.com/news/how-external-assets-start-trading-on-solana-from-day-one)
- [Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)
- [Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)
- [Solana Changelog: July 23, 2026](https://solana.com/news/solana-changelog-july-23-2026)
- [Deploying enterprise stablecoin rails on Solana in days with Crossmint](https://solana.com/news/case-study-crossmint)
- [Solana Changelog: July 16, 2026](https://solana.com/news/solana-changelog-july-16-2026)
- [Solana Changelog: July 9, 2026](https://solana.com/news/solana-changelog-july-9-2026)
- [Solana Changelog: Agave v4.1.0, RPC 2.0, and Alpenglow](https://solana.com/news/solana-changelog-agave-v4-1-0-rpc-2-0-and-alpenglow)
- [Rent Reduction on Solana: A Data-Backed Analysis](https://solana.com/news/rent-reduction-deep-dive)
- [Solana Ecosystem Roundup: June 2026](https://solana.com/news/solana-ecosystem-roundup-june-2026)
- [Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)
- [The Sun Rises in Seoul and Trades on Solana: $SKHY is Now Live](https://solana.com/news/skhy-is-now-live)
- [Release v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1)
- [re-amend SIMD-0340: additional inter- and intra- validation (#551)](https://github.com/solana-foundation/solana-improvement-documents/commit/fc519fb3d1ef0f7624b6232bda958438feba09ce)
- [SIMD-0433: Loader V3: Set Program Data to ELF Length (#433)](https://github.com/solana-foundation/solana-improvement-documents/commit/06bd4bd6b0b835d110bf4ccb0bc7c759ae88e997)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
