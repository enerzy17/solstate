# Solana Ecosystem State Report

Generated **2026-11-05T06:57:07Z** in 19.5s across 17 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 92.9% (13/14 probes returned data). History depth: 121 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1046 is 75% below the trailing median of 4151.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 8.2 robust deviations from its 121-point median of 0.0432, a 1169.7% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,077 |
| Epoch progress | 80.57% |
| Epoch time remaining (est.) | 9h 19m |
| Absolute slot | 465,612,082 |
| Block height | 443,632,295 |
| TPS (all) | 1,045.80 |
| TPS (non-vote) | 1,045.80 |
| TPS (30-sample mean) | 1,118.83 |
| Slot time | 217.40 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 565,307,171,698 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 661 |
| Delinquent | 32 |
| Delinquent share of stake | 0.55% |
| Total active stake | 433.02M SOL |
| Nakamoto coefficient | 17 |
| Stake in top 10 | 24.75% |
| Stake in top 20 | 36.15% |
| Stake in top 50 | 56.09% |
| Median commission | 5.00% |
| Validators at 0% commission | 224 |
| Validators at 100% commission | 61 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.04M | 3.93% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.71M | 3.86% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 13.01M | 3.00% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.43M | 2.41% | 0.00% |
| 5 | `JUPiTERkf97e...` | 9.52M | 2.20% | 5.00% |
| 6 | `7jtWrBuj9k2E...` | 9.44M | 2.18% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.22M | 2.13% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.83M | 1.81% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.98M | 1.61% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.98M | 1.61% | 5.00% |
| 11 | `JD549HsbJHeE...` | 6.29M | 1.45% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.02M | 1.39% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.73M | 1.32% | 100.00% |
| 14 | `GnC339vkyXRm...` | 5.31M | 1.23% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.09% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `722RdWmHC5TG...` | 1.27M | 462,239,999 |
| `EUDis6LJeJzD...` | 397.13K | 465,596,513 |
| `7S22CYpfBRV1...` | 300.00K | 465,263,999 |
| `7cVfgArCheMR...` | 237.14K | 462,239,999 |
| `7nzTzRZzezmu...` | 76.35K | 465,263,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `LandXx5ebB8B...` | 17.54K | 463,967,999 |
| `C7NL6J5xomAR...` | 13.44K | 0 |
| `BXAxLMMMUNYf...` | 2.61K | 462,239,999 |
| `HzrEstnLfzsi...` | 2.60K | 461,807,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $96.22 |
| SOL 24h | 3.53% |
| SOL 7d | -3.98% |
| SOL 30d | -19.67% |
| Market cap | $56.79B |
| Spot volume 24h | $3.79B |
| Circulating supply | 590.26M SOL |
| Circulating share | 92.66% |
| DeFi TVL | $5.54B |
| TVL 24h | 2.85% |
| TVL 7d | -2.79% |
| Stablecoin supply | $14.87B |
| DEX volume 24h | $2.22B |
| DEX volume 7d | $11.20B |
| Chain fees 24h (REV proxy) | $10.96M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0123, SIMD-0685, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550, SIMD-0607, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0648

## Ecosystem news

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
- [SIMD-0690: Hash validation in program migrations and upgrades (#690)](https://github.com/solana-foundation/solana-improvement-documents/commit/eac20f2994dd064482d96f178a4bbc0f4e358fd0)
- [SIMD-0670: ABIv1 invoke signed v2 syscall (#670)](https://github.com/solana-foundation/solana-improvement-documents/commit/c9ec366af14dd32a74259f5d9f5772249188bd25)
- [v4.4.0-rc.0: Bump version to 4.4.0-rc.0 (#16364)](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0)
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5 (#683)](https://github.com/solana-foundation/solana-improvement-documents/commit/a084840a512454a7ee5e2ef8dd736c790102bea0)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
