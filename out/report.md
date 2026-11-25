# Solana Ecosystem State Report

Generated **2026-11-25T00:49:59Z** in 19.0s across 17 HTTP calls.

> **Status:** No anomalies above threshold. Data completeness 92.9% (13/14 probes returned data). History depth: 99 prior runs.

## Anomalies

Nothing outside the configured thresholds or the statistical baseline.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,096 |
| Epoch progress | 18.36% |
| Epoch time remaining (est.) | 39h 11m |
| Absolute slot | 473,551,306 |
| Block height | 451,564,418 |
| TPS (all) | 2,011.38 |
| TPS (non-vote) | 2,011.38 |
| TPS (30-sample mean) | 2,101.09 |
| Slot time | 216.60 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 568,249,169,563 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 660 |
| Delinquent | 27 |
| Delinquent share of stake | 0.02% |
| Total active stake | 424.79M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.99% |
| Stake in top 20 | 36.12% |
| Stake in top 50 | 56.42% |
| Median commission | 5.00% |
| Validators at 0% commission | 220 |
| Validators at 100% commission | 62 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 17.00M | 4.00% | 0.00% |
| 2 | `Fd7btgySsrju...` | 15.96M | 3.76% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 12.42M | 2.92% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.24M | 2.41% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.89M | 2.33% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.62M | 2.26% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.28M | 2.19% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 8.02M | 1.89% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.97M | 1.64% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.78M | 1.60% | 5.00% |
| 11 | `5pPRHniefFjk...` | 6.25M | 1.47% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.93M | 1.40% | 10.00% |
| 13 | `GnC339vkyXRm...` | 4.91M | 1.16% | 7.00% |
| 14 | `9rkJMARqK6VB...` | 4.70M | 1.11% | 8.00% |
| 15 | `9jxgosAfHgHz...` | 4.48M | 1.05% | 100.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `omeg2wsojzB7...` | 37.40K | 472,608,648 |
| `DaRKu4L3qAgX...` | 30.42K | 473,471,999 |
| `BkZtKQkM2NFb...` | 12.54K | 471,311,999 |
| `DzLjgYbBhDN8...` | 2.24K | 326,553,475 |
| `5d9Mdc2Zk8as...` | 46.25 | 472,988,210 |
| `722RdWmHC5TG...` | 10.07 | 462,239,999 |
| `EUcJwf7jXskR...` | 9.10 | 470,879,999 |
| `stacheBmGG5z...` | 3.00 | 429,535,683 |
| `e1STgSzsMaxT...` | 2.03 | 470,447,999 |
| `7cVfgArCheMR...` | 2.00 | 462,239,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $69.60 |
| SOL 24h | -3.40% |
| SOL 7d | -7.35% |
| SOL 30d | -31.25% |
| Market cap | $41.21B |
| Spot volume 24h | $2.47B |
| Circulating supply | 592.13M SOL |
| Circulating share | 92.79% |
| DeFi TVL | $4.53B |
| TVL 24h | 0.00% |
| TVL 7d | -5.62% |
| Stablecoin supply | $13.26B |
| DEX volume 24h | $1.65B |
| DEX volume 7d | $10.30B |
| Chain fees 24h (REV proxy) | $7.67M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0005, SIMD-0504, SIMD-0123, SIMD-0706, SIMD-0701, SIMD-0602, SIMD-0685, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550, SIMD-0607, SIMD-0690

## Ecosystem news

- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` (#706)](https://github.com/solana-foundation/solana-improvement-documents/commit/44a4406237de1597ce56c1d106161dda950cbc68)
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

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
