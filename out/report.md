# Solana Ecosystem State Report

Generated **2026-11-13T01:10:01Z** in 19.2s across 17 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 92.9% (13/14 probes returned data). History depth: 120 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 4.2 robust deviations from its 120-point median of 7.85e+07, a 30.1% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,085 |
| Epoch progress | 4.04% |
| Epoch time remaining (est.) | 46h 3m |
| Absolute slot | 468,737,431 |
| Block height | 446,752,917 |
| TPS (all) | 2,006.20 |
| TPS (non-vote) | 2,006.20 |
| TPS (30-sample mean) | 2,145.49 |
| Slot time | 218.20 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 566,433,023,803 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 659 |
| Delinquent | 40 |
| Delinquent share of stake | 0.13% |
| Total active stake | 432.41M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.54% |
| Stake in top 20 | 35.91% |
| Stake in top 50 | 56.07% |
| Median commission | 5.00% |
| Validators at 0% commission | 223 |
| Validators at 100% commission | 59 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 16.82M | 3.89% | 0.00% |
| 2 | `Fd7btgySsrju...` | 16.14M | 3.73% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 12.98M | 3.00% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.12M | 2.34% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.70M | 2.24% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.58M | 2.22% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.14% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.86M | 1.82% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.99M | 1.62% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.71M | 1.55% | 5.00% |
| 11 | `5pPRHniefFjk...` | 6.11M | 1.41% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.79M | 1.34% | 10.00% |
| 13 | `JD549HsbJHeE...` | 5.51M | 1.27% | 0.00% |
| 14 | `GnC339vkyXRm...` | 5.45M | 1.26% | 7.00% |
| 15 | `Fc6NNdS2j3Em...` | 4.95M | 1.14% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7cVfgArCheMR...` | 214.59K | 462,239,999 |
| `tkmaiSoZ3F8M...` | 80.39K | 467,356,299 |
| `pitch9cMruwj...` | 79.94K | 467,356,334 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `ssx2rHZNVy6J...` | 52.34K | 468,719,999 |
| `ark1hdnnfmus...` | 42.48K | 468,719,999 |
| `sfvTq7ojrEc5...` | 23.78K | 467,855,999 |
| `H4TCC7HNnsSV...` | 10.63K | 0 |
| `HzrEstnLfzsi...` | 2.59K | 461,807,999 |
| `CTDGxTK789Zv...` | 1.64K | 464,160,502 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $81.33 |
| SOL 24h | -2.37% |
| SOL 7d | -9.79% |
| SOL 30d | -24.26% |
| Market cap | $48.10B |
| Spot volume 24h | $2.10B |
| Circulating supply | 591.51M SOL |
| Circulating share | 92.79% |
| DeFi TVL | $5.01B |
| TVL 24h | -0.00% |
| TVL 7d | -4.75% |
| Stablecoin supply | $14.11B |
| DEX volume 24h | $1.61B |
| DEX volume 7d | $8.37B |
| Chain fees 24h (REV proxy) | $9.73M |

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
