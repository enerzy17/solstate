# Solana Ecosystem State Report

Generated **2026-11-28T13:10:49Z** in 16.6s across 17 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 92.9% (13/14 probes returned data). History depth: 94 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 964 is 42% below the trailing median of 1675.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,099 |
| Epoch progress | 45.60% |
| Epoch time remaining (est.) | 26h 6m |
| Absolute slot | 474,964,976 |
| Block height | 452,977,413 |
| TPS (all) | 964.12 |
| TPS (non-vote) | 964.12 |
| TPS (30-sample mean) | 996.41 |
| Slot time | 210.50 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 568,747,253,818 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 655 |
| Delinquent | 10 |
| Delinquent share of stake | 0.03% |
| Total active stake | 423.55M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.94% |
| Stake in top 20 | 36.10% |
| Stake in top 50 | 56.39% |
| Median commission | 5.00% |
| Validators at 0% commission | 217 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `HEL1USMZKAL2...` | 16.82M | 3.97% | 0.00% |
| 2 | `Fd7btgySsrju...` | 15.94M | 3.76% | 7.00% |
| 3 | `DRpbCBMxVnDK...` | 12.43M | 2.93% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.24M | 2.42% | 0.00% |
| 5 | `7jtWrBuj9k2E...` | 9.92M | 2.34% | 10.00% |
| 6 | `JUPiTERkf97e...` | 9.63M | 2.27% | 5.00% |
| 7 | `C8Bey3LKVJHV...` | 9.30M | 2.20% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 8.05M | 1.90% | 7.00% |
| 9 | `Awes4Tr6TX8J...` | 6.97M | 1.65% | 0.00% |
| 10 | `9eGrDohdNTAo...` | 6.35M | 1.50% | 5.00% |
| 11 | `5pPRHniefFjk...` | 6.27M | 1.48% | 5.00% |
| 12 | `5Cchr1XGEg7d...` | 5.95M | 1.40% | 10.00% |
| 13 | `GnC339vkyXRm...` | 4.87M | 1.15% | 7.00% |
| 14 | `9rkJMARqK6VB...` | 4.71M | 1.11% | 8.00% |
| 15 | `9jxgosAfHgHz...` | 4.48M | 1.06% | 100.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `BbCQMWnfxo4e...` | 35.47K | 474,335,999 |
| `DaRKu4L3qAgX...` | 30.40K | 473,471,999 |
| `5tfcGyf3NQFc...` | 29.24K | 474,288,935 |
| `9Wmaz9VPpEnH...` | 12.90K | 474,335,999 |
| `GZ4U21pYmFkC...` | 3.09K | 473,903,999 |
| `ByszyWdqC3rV...` | 2.29K | 473,749,295 |
| `omeg2wsojzB7...` | 124.75 | 472,608,648 |
| `5d9Mdc2Zk8as...` | 46.25 | 472,988,210 |
| `722RdWmHC5TG...` | 14.42 | 462,239,999 |
| `Bdy6qjtdL4DG...` | 1.00 | 0 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $70.76 |
| SOL 24h | -3.09% |
| SOL 7d | 2.35% |
| SOL 30d | -29.55% |
| Market cap | $41.92B |
| Spot volume 24h | $2.25B |
| Circulating supply | 592.43M SOL |
| Circulating share | 92.81% |
| DeFi TVL | $4.57B |
| TVL 24h | -1.23% |
| TVL 7d | 0.46% |
| Stablecoin supply | $12.99B |
| DEX volume 24h | $1.03B |
| DEX volume 7d | $9.00B |
| Chain fees 24h (REV proxy) | $5.58M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0005, SIMD-0504, SIMD-0579, SIMD-0506, SIMD-0706, SIMD-0701, SIMD-0602, SIMD-0685, SIMD-0529, SIMD-0567, SIMD-0650, SIMD-0550

## Ecosystem news

- [Release v4.5.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.1)
- [Release v4.4.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.2)
- [SIMD-0579: Keccak-p1600 syscall (#579)](https://github.com/solana-foundation/solana-improvement-documents/commit/7a56bc9241056930caa2312bf0c8790a6799bccf)
- [Release v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0)
- [Release v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0)
- [Withdraw SIMD-0506 (#738)](https://github.com/solana-foundation/solana-improvement-documents/commit/1536c3eceda1779de191453246f939e53d8d7c94)
- [100M CUs Pt2 (#698)](https://github.com/solana-foundation/solana-improvement-documents/commit/e4d2b0e1c035385a65a96b3875e5b92af5df868e)
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` (#706)](https://github.com/solana-foundation/solana-improvement-documents/commit/44a4406237de1597ce56c1d106161dda950cbc68)
- [Amend 0529: charge a flat cu first before execution (#707)](https://github.com/solana-foundation/solana-improvement-documents/commit/6cf17cb7138d3fac03f5b637c1fde91a00fb48fc)
- [Release v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1)
- [SIMD-0701: Vote Account v5 (#701)](https://github.com/solana-foundation/solana-improvement-documents/commit/ae7b00f3287a614c5aa5d0a7ceb7bad0cdc4e022)
- [SIMD-0602: Disallow Nonce Account as Program ID (#602)](https://github.com/solana-foundation/solana-improvement-documents/commit/809a97a0b0e0f2190fa5d494bcc5856a06907969)
- [Release v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1)
- [SIMD-0685: Loader V3: Remove ExtendProgram (#685)](https://github.com/solana-foundation/solana-improvement-documents/commit/540f6ab4b9b71b584eae4f00c156194308d6650e)
- [rekey simd-0529 big int mod exp (#715)](https://github.com/solana-foundation/solana-improvement-documents/commit/0434aab3b2c6b596f607194bee44e94088ff2591)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
