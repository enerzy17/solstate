# Solana Ecosystem State Report

Generated **2026-11-23T02:53:06Z** in 17.8s across 17 HTTP calls.

> **Status:** No anomalies above threshold. Data completeness 92.9% (13/14 probes returned data). History depth: 103 prior runs.

## Anomalies

Nothing outside the configured thresholds or the statistical baseline.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,094 |
| Epoch progress | 40.28% |
| Epoch time remaining (est.) | 28h 39m |
| Absolute slot | 472,782,012 |
| Block height | 450,795,592 |
| TPS (all) | 1,820.62 |
| TPS (non-vote) | 1,820.62 |
| TPS (30-sample mean) | 1,623.78 |
| Slot time | 216.60 ms |
| Block lag vs wall clock | 1s |
| Lifetime transactions | 567,943,016,285 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 661 |
| Delinquent | 24 |
| Delinquent share of stake | 0.03% |
| Total active stake | 425.69M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.99% |
| Stake in top 20 | 36.03% |
| Stake in top 50 | 56.41% |
| Median commission | 5.00% |
| Validators at 0% commission | 220 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 16.92M | 3.97% | 0.00% |
| 2 | `Fd7btgySsrju...` | 16.35M | 3.84% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 12.40M | 2.91% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.24M | 2.41% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.84M | 2.31% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.61M | 2.26% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.27M | 2.18% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 8.00M | 1.88% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.99M | 1.64% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.78M | 1.59% | 5.00% |
| 11 | `5pPRHniefFjk...` | 6.24M | 1.46% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.91M | 1.39% | 10.00% |
| 13 | `GnC339vkyXRm...` | 4.88M | 1.15% | 7.00% |
| 14 | `9rkJMARqK6VB...` | 4.70M | 1.10% | 8.00% |
| 15 | `9jxgosAfHgHz...` | 4.48M | 1.05% | 100.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `SA1LFXr4os2P...` | 77.38K | 472,781,490 |
| `omeg2wsojzB7...` | 37.69K | 472,608,648 |
| `BkZtKQkM2NFb...` | 12.77K | 471,311,999 |
| `722RdWmHC5TG...` | 10.07 | 462,239,999 |
| `EUcJwf7jXskR...` | 9.10 | 470,879,999 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `e1STgSzsMaxT...` | 2.03 | 470,447,999 |
| `7cVfgArCheMR...` | 2.00 | 462,239,999 |
| `BaDhUB1eWfun...` | 1.00 | 464,520,717 |
| `CTDGxTK789Zv...` | 1.00 | 464,160,502 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $69.87 |
| SOL 24h | 0.53% |
| SOL 7d | -2.06% |
| SOL 30d | -31.84% |
| Market cap | $41.36B |
| Spot volume 24h | $1.85B |
| Circulating supply | 592.02M SOL |
| Circulating share | 92.79% |
| DeFi TVL | $4.62B |
| TVL 24h | 0.49% |
| TVL 7d | -1.25% |
| Stablecoin supply | $13.14B |
| DEX volume 24h | $1.19B |
| DEX volume 7d | $10.37B |
| Chain fees 24h (REV proxy) | $6.01M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0005, SIMD-0504, SIMD-0123, SIMD-0701, SIMD-0602, SIMD-0685, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550, SIMD-0607, SIMD-0690, SIMD-0670

## Ecosystem news

- [Amend 0529: charge a flat cu first before execution (#707)](https://github.com/solana-foundation/solana-improvement-documents/commit/6cf17cb7138d3fac03f5b637c1fde91a00fb48fc)
- [Release v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1)
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

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
