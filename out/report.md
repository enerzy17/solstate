# Solana Ecosystem State Report

Generated **2026-11-06T15:58:46Z** in 18.2s across 17 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 92.9% (13/14 probes returned data). History depth: 121 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1948 is 50% below the trailing median of 3882.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 3.9 robust deviations from its 121-point median of 0.0491, a 556.8% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,079 |
| Epoch progress | 9.33% |
| Epoch time remaining (est.) | 43h 31m |
| Absolute slot | 466,168,317 |
| Block height | 444,187,510 |
| TPS (all) | 1,947.92 |
| TPS (non-vote) | 1,947.92 |
| TPS (30-sample mean) | 2,043.74 |
| Slot time | 214.30 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 565,527,235,965 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 657 |
| Delinquent | 39 |
| Delinquent share of stake | 0.32% |
| Total active stake | 434.92M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.65% |
| Stake in top 20 | 36.06% |
| Stake in top 50 | 55.97% |
| Median commission | 5.00% |
| Validators at 0% commission | 224 |
| Validators at 100% commission | 61 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.04M | 3.92% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.72M | 3.84% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 13.02M | 2.99% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.44M | 2.40% | 0.00% |
| 5 | `JUPiTERkf97e...` | 9.53M | 2.19% | 5.00% |
| 6 | `7jtWrBuj9k2E...` | 9.52M | 2.19% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.12% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.74M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.98M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.97M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.29M | 1.45% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.03M | 1.39% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.76M | 1.32% | 100.00% |
| 14 | `GnC339vkyXRm...` | 5.35M | 1.23% | 7.00% |
| 15 | `Fc6NNdS2j3Em...` | 4.80M | 1.10% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `vR6bU4NATnWq...` | 500.00K | 459,643,077 |
| `7cVfgArCheMR...` | 234.31K | 462,239,999 |
| `97jbhVBYcSmw...` | 194.07K | 465,663,873 |
| `ByszyWdqC3rV...` | 127.44K | 466,127,999 |
| `SaGAgdkowooX...` | 98.45K | 466,166,963 |
| `7nzTzRZzezmu...` | 70.76K | 465,263,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `mds3Df1ieBon...` | 56.91K | 466,127,999 |
| `7d7x84jiVtqp...` | 53.00K | 466,163,999 |
| `HzrEstnLfzsi...` | 2.60K | 461,807,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $90.52 |
| SOL 24h | 0.57% |
| SOL 7d | -4.18% |
| SOL 30d | -21.86% |
| Market cap | $53.44B |
| Spot volume 24h | $3.27B |
| Circulating supply | 590.34M SOL |
| Circulating share | 92.66% |
| DeFi TVL | $5.30B |
| TVL 24h | -4.22% |
| TVL 7d | -0.81% |
| Stablecoin supply | $14.55B |
| DEX volume 24h | $2.20B |
| DEX volume 7d | $12.29B |
| Chain fees 24h (REV proxy) | $9.64M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0504, SIMD-0123, SIMD-0685, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550, SIMD-0607, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0648

## Ecosystem news

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
- [SIMD-0690: Hash validation in program migrations and upgrades (#690)](https://github.com/solana-foundation/solana-improvement-documents/commit/eac20f2994dd064482d96f178a4bbc0f4e358fd0)
- [SIMD-0670: ABIv1 invoke signed v2 syscall (#670)](https://github.com/solana-foundation/solana-improvement-documents/commit/c9ec366af14dd32a74259f5d9f5772249188bd25)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
