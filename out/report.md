# Solana Ecosystem State Report

Generated **2026-11-02T01:33:44Z** in 17.1s across 17 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 92.9% (13/14 probes returned data). History depth: 124 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 1500 is 66% below the trailing median of 4359.
- [WARNING] **delinquent_pct_by_stake** (statistical) - delinquent_pct_by_stake is 28.6 robust deviations from its 124-point median of 0.02635, a 3884.4% move.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,074 |
| Epoch progress | 79.60% |
| Epoch time remaining (est.) | 9h 47m |
| Absolute slot | 464,311,884 |
| Block height | 442,333,315 |
| TPS (all) | 1,499.55 |
| TPS (non-vote) | 1,499.55 |
| TPS (30-sample mean) | 1,905.28 |
| Slot time | 213.50 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 564,795,281,807 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 662 |
| Delinquent | 34 |
| Delinquent share of stake | 1.05% |
| Total active stake | 433.94M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.69% |
| Stake in top 20 | 35.87% |
| Stake in top 50 | 55.60% |
| Median commission | 5.00% |
| Validators at 0% commission | 223 |
| Validators at 100% commission | 65 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.03M | 3.92% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.70M | 3.85% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 12.94M | 2.98% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.43M | 2.40% | 0.00% |
| 5 | `JUPiTERrZqgf...` | 9.58M | 2.21% | 5.00% |
| 6 | `CAo1dCGYrB6N...` | 9.45M | 2.18% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.23M | 2.13% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.79M | 1.80% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 7.00M | 1.61% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.98M | 1.61% | 5.00% |
| 11 | `JD549HsbJHeE...` | 6.06M | 1.40% | 0.00% |
| 12 | `5pPRHniefFjk...` | 5.98M | 1.38% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.72M | 1.32% | 100.00% |
| 14 | `GnC339vkyXRm...` | 4.83M | 1.11% | 7.00% |
| 15 | `9rkJMARqK6VB...` | 4.72M | 1.09% | 8.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7qGNnXKW1e3D...` | 1.84M | 463,967,999 |
| `722RdWmHC5TG...` | 1.35M | 462,239,999 |
| `BXAxLMMMUNYf...` | 794.23K | 462,239,999 |
| `7cVfgArCheMR...` | 250.45K | 462,239,999 |
| `RAuSNo4DRjo8...` | 145.76K | 463,535,999 |
| `uEhHSnCXvWgt...` | 96.62K | 463,967,999 |
| `2dfgsiSaZ51Q...` | 62.32K | 462,239,999 |
| `LandXx5ebB8B...` | 16.59K | 463,967,999 |
| `CTDGxTK789Zv...` | 2.69K | 464,160,502 |
| `HzrEstnLfzsi...` | 2.60K | 461,807,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $95.04 |
| SOL 24h | -0.67% |
| SOL 7d | -6.28% |
| SOL 30d | -20.12% |
| Market cap | $56.09B |
| Spot volume 24h | $1.73B |
| Circulating supply | 590.15M SOL |
| Circulating share | 92.67% |
| DeFi TVL | $5.44B |
| TVL 24h | 1.35% |
| TVL 7d | -4.37% |
| Stablecoin supply | $15.17B |
| DEX volume 24h | $831.89M |
| DEX volume 7d | $11.18B |
| Chain fees 24h (REV proxy) | $8.43M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0123, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550, SIMD-0607, SIMD-0690, SIMD-0670, SIMD-0683, SIMD-0648, SIMD-0565

## Ecosystem news

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
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp…](https://github.com/solana-foundation/solana-improvement-documents/commit/51dbb649da0233481cc40f5640f33fe74d6dbffe)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
