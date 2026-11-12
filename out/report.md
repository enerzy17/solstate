# Solana Ecosystem State Report

Generated **2026-11-12T00:48:34Z** in 17.0s across 17 HTTP calls.

> **Status:** 2 warning-level anomalies. Data completeness 92.9% (13/14 probes returned data). History depth: 120 prior runs.

## Anomalies

- [WARNING] **chain_fees_7d_usd** (statistical) - chain_fees_7d_usd is 4.0 robust deviations from its 120-point median of 7.903e+07, a 30.8% move.
- [WARNING] **stablecoin_supply_usd** (statistical) - stablecoin_supply_usd is 3.6 robust deviations from its 120-point median of 1.554e+10, a 10.4% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,084 |
| Epoch progress | 9.68% |
| Epoch time remaining (est.) | 43h 21m |
| Absolute slot | 468,329,811 |
| Block height | 446,345,798 |
| TPS (all) | 2,336.32 |
| TPS (non-vote) | 2,336.32 |
| TPS (30-sample mean) | 1,829.03 |
| Slot time | 215.10 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 566,277,325,800 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 661 |
| Delinquent | 37 |
| Delinquent share of stake | 0.16% |
| Total active stake | 433.42M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.48% |
| Stake in top 20 | 36.01% |
| Stake in top 50 | 56.10% |
| Median commission | 5.00% |
| Validators at 0% commission | 223 |
| Validators at 100% commission | 61 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 16.79M | 3.87% | 0.00% |
| 2 | `Fd7btgySsrju...` | 16.12M | 3.72% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 13.03M | 3.01% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.12M | 2.33% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.68M | 2.23% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.58M | 2.21% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.23M | 2.13% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.84M | 1.81% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.99M | 1.61% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.73M | 1.55% | 5.00% |
| 11 | `JD549HsbJHeE...` | 6.30M | 1.45% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.10M | 1.41% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.78M | 1.33% | 10.00% |
| 14 | `GnC339vkyXRm...` | 5.40M | 1.25% | 7.00% |
| 15 | `Fc6NNdS2j3Em...` | 5.06M | 1.17% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7cVfgArCheMR...` | 217.20K | 462,239,999 |
| `BULKzVM41WAy...` | 129.22K | 466,294,271 |
| `tkmaiSoZ3F8M...` | 88.44K | 467,356,299 |
| `pitch9cMruwj...` | 79.76K | 467,356,334 |
| `sfvTq7ojrEc5...` | 78.88K | 467,855,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `Mwz8VgAEnPtf...` | 25.23K | 468,287,999 |
| `HzrEstnLfzsi...` | 2.59K | 461,807,999 |
| `CTDGxTK789Zv...` | 1.84K | 464,160,502 |
| `yJeahQNRHNWt...` | 700.22 | 465,263,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $83.63 |
| SOL 24h | 0.46% |
| SOL 7d | -12.44% |
| SOL 30d | -20.83% |
| Market cap | $49.47B |
| Spot volume 24h | $2.13B |
| Circulating supply | 591.46M SOL |
| Circulating share | 92.79% |
| DeFi TVL | $5.05B |
| TVL 24h | -0.02% |
| TVL 7d | -6.20% |
| Stablecoin supply | $13.91B |
| DEX volume 24h | $1.37B |
| DEX volume 7d | $8.96B |
| Chain fees 24h (REV proxy) | $8.71M |

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
