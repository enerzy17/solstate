# Solana Ecosystem State Report

Generated **2026-11-08T22:13:33Z** in 18.4s across 17 HTTP calls.

> **Status:** No anomalies above threshold. Data completeness 92.9% (13/14 probes returned data). History depth: 122 prior runs.

## Anomalies

Nothing outside the configured thresholds or the statistical baseline.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,081 |
| Epoch progress | 20.03% |
| Epoch time remaining (est.) | 38h 23m |
| Absolute slot | 467,078,513 |
| Block height | 445,096,649 |
| TPS (all) | 2,426.20 |
| TPS (non-vote) | 2,426.20 |
| TPS (30-sample mean) | 2,658.82 |
| Slot time | 215.80 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 565,821,240,972 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 661 |
| Delinquent | 36 |
| Delinquent share of stake | 0.14% |
| Total active stake | 433.92M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.63% |
| Stake in top 20 | 36.08% |
| Stake in top 50 | 56.04% |
| Median commission | 5.00% |
| Validators at 0% commission | 222 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.05M | 3.93% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.72M | 3.85% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 13.02M | 3.00% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.28M | 2.37% | 0.00% |
| 5 | `JUPiTERkf97e...` | 9.55M | 2.20% | 5.00% |
| 6 | `7jtWrBuj9k2E...` | 9.55M | 2.20% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.22M | 2.13% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.78M | 1.79% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.98M | 1.61% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.71M | 1.55% | 5.00% |
| 11 | `JD549HsbJHeE...` | 6.29M | 1.45% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.04M | 1.39% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.76M | 1.33% | 100.00% |
| 14 | `GnC339vkyXRm...` | 5.39M | 1.24% | 7.00% |
| 15 | `Fc6NNdS2j3Em...` | 4.82M | 1.11% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7cVfgArCheMR...` | 217.55K | 462,239,999 |
| `BULKzVM41WAy...` | 132.36K | 466,294,271 |
| `97jbhVBYcSmw...` | 100.94K | 465,663,873 |
| `E14p6tBtwUP4...` | 68.84K | 466,991,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `7nzTzRZzezmu...` | 40.43K | 465,263,999 |
| `HzrEstnLfzsi...` | 2.60K | 461,807,999 |
| `CTDGxTK789Zv...` | 1.84K | 464,160,502 |
| `yJeahQNRHNWt...` | 700.23 | 465,263,999 |
| `BXAxLMMMUNYf...` | 527.30 | 462,239,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $86.37 |
| SOL 24h | -3.03% |
| SOL 7d | -8.44% |
| SOL 30d | -20.68% |
| Market cap | $51.03B |
| Spot volume 24h | $1.32B |
| Circulating supply | 591.09M SOL |
| Circulating share | 92.76% |
| DeFi TVL | $5.19B |
| TVL 24h | -0.68% |
| TVL 7d | -4.06% |
| Stablecoin supply | $14.85B |
| DEX volume 24h | $917.44M |
| DEX volume 7d | $11.62B |
| Chain fees 24h (REV proxy) | $8.04M |

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
