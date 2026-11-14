# Solana Ecosystem State Report

Generated **2026-11-14T06:37:19Z** in 18.4s across 17 HTTP calls.

> **Status:** 6 warning-level anomalies. Data completeness 92.9% (13/14 probes returned data). History depth: 118 prior runs.

## Anomalies

- [WARNING] **sol_ath_change_pct** (statistical) - sol_ath_change_pct is 3.6 robust deviations from its 118-point median of -65.73, a 12.9% move.
- [WARNING] **sol_change_7d_pct** (statistical) - sol_change_7d_pct is 3.6 robust deviations from its 118-point median of -5.31, a 205.8% move.
- [WARNING] **sol_fdv_usd** (statistical) - sol_fdv_usd is 3.6 robust deviations from its 118-point median of 6.397e+10, a 24.7% move.
- [WARNING] **sol_market_cap_usd** (statistical) - sol_market_cap_usd is 3.6 robust deviations from its 118-point median of 5.928e+10, a 24.6% move.
- [WARNING] **sol_price_usd** (statistical) - sol_price_usd is 3.6 robust deviations from its 118-point median of 100.5, a 24.8% move.
- [WARNING] **stablecoin_supply_usd** (statistical) - stablecoin_supply_usd is 3.6 robust deviations from its 118-point median of 1.544e+10, a 9.6% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,086 |
| Epoch progress | 18.01% |
| Epoch time remaining (est.) | 39h 21m |
| Absolute slot | 469,229,790 |
| Block height | 447,244,905 |
| TPS (all) | 1,575.05 |
| TPS (non-vote) | 1,575.05 |
| TPS (30-sample mean) | 1,323.16 |
| Slot time | 210.50 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 566,624,563,295 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 656 |
| Delinquent | 43 |
| Delinquent share of stake | 0.30% |
| Total active stake | 429.65M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.72% |
| Stake in top 20 | 35.88% |
| Stake in top 50 | 56.13% |
| Median commission | 5.00% |
| Validators at 0% commission | 222 |
| Validators at 100% commission | 61 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 16.96M | 3.95% | 0.00% |
| 2 | `Fd7btgySsrju...` | 16.37M | 3.81% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 12.61M | 2.94% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.14M | 2.36% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.74M | 2.27% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.57M | 2.23% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.20M | 2.14% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.91M | 1.84% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.99M | 1.63% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.71M | 1.56% | 5.00% |
| 11 | `5pPRHniefFjk...` | 6.12M | 1.43% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.81M | 1.35% | 10.00% |
| 13 | `GnC339vkyXRm...` | 5.35M | 1.25% | 7.00% |
| 14 | `Fc6NNdS2j3Em...` | 4.83M | 1.12% | 5.00% |
| 15 | `9rkJMARqK6VB...` | 4.68M | 1.09% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `PRGNnb8DxVcP...` | 294.11K | 469,228,086 |
| `7cVfgArCheMR...` | 209.27K | 462,239,999 |
| `E99w1XfS4UNM...` | 182.06K | 469,228,889 |
| `HMWXfjaeSHhw...` | 121.30K | 469,225,297 |
| `CARBN9PY1Qej...` | 87.45K | 469,229,416 |
| `nodeEgRVkbYL...` | 85.00K | 469,228,767 |
| `D3htsc6iRQJL...` | 78.69K | 469,225,428 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `tkmaiSoZ3F8M...` | 43.20K | 467,356,299 |
| `pitch9cMruwj...` | 42.51K | 467,356,334 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $75.56 |
| SOL 24h | -5.18% |
| SOL 7d | -16.24% |
| SOL 30d | -25.49% |
| Market cap | $44.70B |
| Spot volume 24h | $3.39B |
| Circulating supply | 591.57M SOL |
| Circulating share | 92.79% |
| DeFi TVL | $4.82B |
| TVL 24h | -3.61% |
| TVL 7d | -7.78% |
| Stablecoin supply | $13.96B |
| DEX volume 24h | $1.45B |
| DEX volume 7d | $8.69B |
| Chain fees 24h (REV proxy) | $9.34M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0504, SIMD-0123, SIMD-0701, SIMD-0602, SIMD-0685, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550, SIMD-0607, SIMD-0690, SIMD-0670, SIMD-0683

## Ecosystem news

- [SIMD-0701: Vote Account v5 (#701)](https://github.com/solana-foundation/solana-improvement-documents/commit/ae7b00f3287a614c5aa5d0a7ceb7bad0cdc4e022)
- [SIMD-0602: Disallow Nonce Account as Program ID (#602)](https://github.com/solana-foundation/solana-improvement-documents/commit/809a97a0b0e0f2190fa5d494bcc5856a06907969)
- [Release v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0)
- [Release v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1)
- [SIMD-0685: Loader V3: Remove ExtendProgram (#685)](https://github.com/solana-foundation/solana-improvement-documents/commit/540f6ab4b9b71b584eae4f00c156194308d6650e)
- [rekey simd-0529 big int mod exp (#715)](https://github.com/solana-foundation/solana-improvement-documents/commit/0434aab3b2c6b596f607194bee44e94088ff2591)
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`) (#567)](https://github.com/solana-foundation/solana-improvement-documents/commit/93cdf03a368a8bb2743a7f8d458a4cd36d2a904f)
- [SIMD-0650: bn254 pairing output (#650)](https://github.com/solana-foundation/solana-improvement-documents/commit/846194b6367badc2a5408d19f9341bf265e82e34)
- [Release v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0)
- [docs: align SIMD-0550 with the integer inflation schedule (#704)](https://github.com/solana-foundation/solana-improvement-documents/commit/2be4cb0c0fd1025df8c037b19372f7346119b231)
- [Mark SIMDs as Activated (#710)](https://github.com/solana-foundation/solana-improvement-documents/commit/6cc17538e26601e65beca89bbfa761e755720956)
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate prec…](https://github.com/solana-foundation/solana-improvement-documents/commit/2934dbeb1c8a7dfecc4f70a93a6b152e525b1698)
- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4)
- [v4.5.0-alpha.3: Bump version to 4.5.0-alpha.3 (#16402)](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.3)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
