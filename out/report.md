# Solana Ecosystem State Report

Generated **2026-11-05T16:31:19Z** in 21.8s across 17 HTTP calls.

> **Status:** No anomalies above threshold. Data completeness 92.9% (13/14 probes returned data). History depth: 121 prior runs.

## Anomalies

Nothing outside the configured thresholds or the statistical baseline.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,078 |
| Epoch progress | 17.96% |
| Epoch time remaining (est.) | 39h 22m |
| Absolute slot | 465,773,604 |
| Block height | 443,793,531 |
| TPS (all) | 2,929.18 |
| TPS (non-vote) | 2,929.18 |
| TPS (30-sample mean) | 3,735.95 |
| Slot time | 216.60 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 565,369,904,667 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 663 |
| Delinquent | 31 |
| Delinquent share of stake | 0.13% |
| Total active stake | 430.87M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.74% |
| Stake in top 20 | 35.99% |
| Stake in top 50 | 56.09% |
| Median commission | 5.00% |
| Validators at 0% commission | 226 |
| Validators at 100% commission | 61 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.06M | 3.96% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.74M | 3.88% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 13.02M | 3.02% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.43M | 2.42% | 0.00% |
| 5 | `JUPiTERkf97e...` | 9.53M | 2.21% | 5.00% |
| 6 | `7jtWrBuj9k2E...` | 9.46M | 2.20% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.22M | 2.14% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.86M | 1.82% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.99M | 1.62% | 0.00% |
| 10 | `JD549HsbJHeE...` | 6.29M | 1.46% | 0.00% |
| 11 | `5pPRHniefFjk...` | 6.02M | 1.40% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.76M | 1.34% | 100.00% |
| 13 | `GnC339vkyXRm...` | 5.35M | 1.24% | 7.00% |
| 14 | `9eGrDohdNTAo...` | 5.10M | 1.18% | 5.00% |
| 15 | `Fc6NNdS2j3Em...` | 4.83M | 1.12% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7cVfgArCheMR...` | 234.31K | 462,239,999 |
| `97jbhVBYcSmw...` | 203.75K | 465,663,873 |
| `7nzTzRZzezmu...` | 73.36K | 465,263,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `HzrEstnLfzsi...` | 2.60K | 461,807,999 |
| `CTDGxTK789Zv...` | 1.85K | 464,160,502 |
| `yJeahQNRHNWt...` | 700.23 | 465,263,999 |
| `BXAxLMMMUNYf...` | 527.30 | 462,239,999 |
| `722RdWmHC5TG...` | 131.28 | 462,239,999 |
| `Bi9kKNxfW2Xq...` | 62.83 | 462,464,506 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $91.04 |
| SOL 24h | -5.63% |
| SOL 7d | -11.24% |
| SOL 30d | -24.49% |
| Market cap | $53.74B |
| Spot volume 24h | $4.41B |
| Circulating supply | 590.32M SOL |
| Circulating share | 92.66% |
| DeFi TVL | $5.42B |
| TVL 24h | 0.74% |
| TVL 7d | -4.78% |
| Stablecoin supply | $14.96B |
| DEX volume 24h | $2.39B |
| DEX volume 7d | $12.39B |
| Chain fees 24h (REV proxy) | $11.23M |

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
