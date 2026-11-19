# Solana Ecosystem State Report

Generated **2026-11-19T10:27:42Z** in 15.9s across 17 HTTP calls.

> **Status:** No anomalies above threshold. Data completeness 92.9% (13/14 probes returned data). History depth: 109 prior runs.

## Anomalies

Nothing outside the configured thresholds or the statistical baseline.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,090 |
| Epoch progress | 97.72% |
| Epoch time remaining (est.) | 1h 5m |
| Absolute slot | 471,302,156 |
| Block height | 449,316,439 |
| TPS (all) | 1,318.43 |
| TPS (non-vote) | 1,318.43 |
| TPS (30-sample mean) | 1,254.28 |
| Slot time | 215.10 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 567,400,549,159 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 660 |
| Delinquent | 25 |
| Delinquent share of stake | 0.02% |
| Total active stake | 426.75M SOL |
| Nakamoto coefficient | 17 |
| Stake in top 10 | 24.98% |
| Stake in top 20 | 36.20% |
| Stake in top 50 | 56.49% |
| Median commission | 5.00% |
| Validators at 0% commission | 219 |
| Validators at 100% commission | 61 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 17.03M | 3.99% | 0.00% |
| 2 | `Fd7btgySsrju...` | 16.48M | 3.86% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 12.42M | 2.91% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.30M | 2.41% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.82M | 2.30% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.57M | 2.24% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.22M | 2.16% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.97M | 1.87% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 7.00M | 1.64% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.77M | 1.59% | 5.00% |
| 11 | `5pPRHniefFjk...` | 6.17M | 1.45% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.87M | 1.37% | 10.00% |
| 13 | `GnC339vkyXRm...` | 5.36M | 1.26% | 7.00% |
| 14 | `9rkJMARqK6VB...` | 4.69M | 1.10% | 8.00% |
| 15 | `Fc6NNdS2j3Em...` | 4.63M | 1.08% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `ssx2rHZNVy6J...` | 35.52K | 469,583,999 |
| `DaRKu4L3qAgX...` | 30.47K | 470,879,999 |
| `EUcJwf7jXskR...` | 9.10 | 470,879,999 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `7cVfgArCheMR...` | 2.10 | 462,239,999 |
| `e1STgSzsMaxT...` | 2.03 | 470,447,999 |
| `FhFB8MAj5Kzx...` | 1.50 | 469,698,063 |
| `Bi9kKNxfW2Xq...` | 1.00 | 462,464,506 |
| `BXAxLMMMUNYf...` | 1.00 | 462,239,999 |
| `EKgSCR3ahdyp...` | 1.00 | 465,702,670 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $74.49 |
| SOL 24h | -0.36% |
| SOL 7d | -10.31% |
| SOL 30d | -28.33% |
| Market cap | $44.08B |
| Spot volume 24h | $2.12B |
| Circulating supply | 591.80M SOL |
| Circulating share | 92.79% |
| DeFi TVL | $4.76B |
| TVL 24h | -0.76% |
| TVL 7d | -5.44% |
| Stablecoin supply | $12.64B |
| DEX volume 24h | $1.70B |
| DEX volume 7d | $10.05B |
| Chain fees 24h (REV proxy) | $9.97M |

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
