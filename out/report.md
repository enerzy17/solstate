# Solana Ecosystem State Report

Generated **2026-11-10T20:52:41Z** in 29.5s across 17 HTTP calls.

> **Status:** 1 warning-level anomaly. Data completeness 92.9% (13/14 probes returned data). History depth: 121 prior runs.

## Anomalies

- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 7.1 robust deviations from its 121-point median of 0.1234, a 1020.1% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,083 |
| Epoch progress | 1.30% |
| Epoch time remaining (est.) | 47h 22m |
| Absolute slot | 467,861,617 |
| Block height | 445,878,548 |
| TPS (all) | 1,954.60 |
| TPS (non-vote) | 1,954.60 |
| TPS (30-sample mean) | 2,088.64 |
| Slot time | 212.00 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 566,090,193,742 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 657 |
| Delinquent | 42 |
| Delinquent share of stake | 1.38% |
| Total active stake | 433.42M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.56% |
| Stake in top 20 | 35.84% |
| Stake in top 50 | 55.50% |
| Median commission | 5.00% |
| Validators at 0% commission | 221 |
| Validators at 100% commission | 60 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 16.76M | 3.87% | 0.00% |
| 2 | `Fd7btgySsrju...` | 16.56M | 3.82% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 13.03M | 3.01% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.12M | 2.33% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.64M | 2.23% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.57M | 2.21% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.23M | 2.13% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.81M | 1.80% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.99M | 1.61% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.73M | 1.55% | 5.00% |
| 11 | `JD549HsbJHeE...` | 6.30M | 1.45% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.08M | 1.40% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.77M | 1.33% | 10.00% |
| 14 | `GnC339vkyXRm...` | 5.40M | 1.24% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.68M | 1.08% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `Fc6NNdS2j3Em...` | 4.99M | 467,845,929 |
| `7cVfgArCheMR...` | 217.28K | 462,239,999 |
| `BULKzVM41WAy...` | 130.79K | 466,294,271 |
| `tkmaiSoZ3F8M...` | 114.35K | 467,356,299 |
| `2jS8AX38m8F9...` | 103.55K | 467,423,999 |
| `pitch9cMruwj...` | 101.02K | 467,356,334 |
| `97jbhVBYcSmw...` | 99.94K | 465,663,873 |
| `sfvTq7ojrEc5...` | 80.22K | 467,855,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `ark1hdnnfmus...` | 42.48K | 467,423,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $83.37 |
| SOL 24h | -3.77% |
| SOL 7d | -10.53% |
| SOL 30d | -25.07% |
| Market cap | $49.25B |
| Spot volume 24h | $2.98B |
| Circulating supply | 591.20M SOL |
| Circulating share | 92.76% |
| DeFi TVL | $5.00B |
| TVL 24h | -1.88% |
| TVL 7d | -7.49% |
| Stablecoin supply | $14.63B |
| DEX volume 24h | $1.49B |
| DEX volume 7d | $11.39B |
| Chain fees 24h (REV proxy) | $9.38M |

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
