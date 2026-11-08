# Solana Ecosystem State Report

Generated **2026-11-08T09:06:03Z** in 37.3s across 19 HTTP calls.

> **Status:** **1 critical** anomaly open. Data completeness 85.7% (12/14 probes returned data). History depth: 121 prior runs.

## Anomalies

- [CRITICAL] **tps** (rule) - TPS 908 is 65% below the trailing median of 2621.

## Network performance

| Metric | Value |
| --- | --- |
| Health | ok |
| Epoch | 1,080 |
| Epoch progress | 69.04% |
| Epoch time remaining (est.) | 14h 51m |
| Absolute slot | 466,858,261 |
| Block height | 444,876,627 |
| TPS (all) | 908.47 |
| TPS (non-vote) | 908.47 |
| TPS (30-sample mean) | 971.92 |
| Slot time | 212.00 ms |
| Block lag vs wall clock | 0s |
| Lifetime transactions | 565,753,376,659 |

## Validators

| Metric | Value |
| --- | --- |
| Active | 662 |
| Delinquent | 35 |
| Delinquent share of stake | 0.16% |
| Total active stake | 434.78M SOL |
| Nakamoto coefficient | 18 |
| Stake in top 10 | 24.63% |
| Stake in top 20 | 36.05% |
| Stake in top 50 | 55.97% |
| Median commission | 5.00% |
| Validators at 0% commission | 222 |
| Validators at 100% commission | 63 |

### Largest validators by active stake

| # | Node | Stake (SOL) | Share | Commission |
| --- | --- | --- | --- | --- |
| 1 | `Fd7btgySsrju...` | 17.04M | 3.92% | 7.00% |
| 2 | `HEL1USMZKAL2...` | 16.73M | 3.85% | 0.00% |
| 3 | `DRpbCBMxVnDK...` | 13.02M | 2.99% | 0.00% |
| 4 | `E1r4Psq84tHf...` | 10.28M | 2.36% | 0.00% |
| 5 | `JUPiTERkf97e...` | 9.56M | 2.20% | 5.00% |
| 6 | `7jtWrBuj9k2E...` | 9.52M | 2.19% | 10.00% |
| 7 | `C8Bey3LKVJHV...` | 9.24M | 2.13% | 7.00% |
| 8 | `EvnRmnMrd69k...` | 7.75M | 1.78% | 7.00% |
| 9 | `9eGrDohdNTAo...` | 6.98M | 1.61% | 5.00% |
| 10 | `Awes4Tr6TX8J...` | 6.97M | 1.60% | 0.00% |
| 11 | `JD549HsbJHeE...` | 6.29M | 1.45% | 0.00% |
| 12 | `5pPRHniefFjk...` | 6.04M | 1.39% | 5.00% |
| 13 | `5Cchr1XGEg7d...` | 5.76M | 1.33% | 100.00% |
| 14 | `GnC339vkyXRm...` | 5.39M | 1.24% | 7.00% |
| 15 | `Fc6NNdS2j3Em...` | 4.80M | 1.10% | 5.00% |

### Largest delinquent validators

| Node | Stake (SOL) | Last vote |
| --- | --- | --- |
| `7cVfgArCheMR...` | 217.56K | 462,239,999 |
| `97jbhVBYcSmw...` | 140.40K | 465,663,873 |
| `BULKzVM41WAy...` | 134.48K | 466,294,271 |
| `7nzTzRZzezmu...` | 70.73K | 465,263,999 |
| `2dfgsiSaZ51Q...` | 60.11K | 462,239,999 |
| `DiFeTctQSaNc...` | 48.37K | 466,816,251 |
| `HzrEstnLfzsi...` | 2.60K | 461,807,999 |
| `CTDGxTK789Zv...` | 1.84K | 464,160,502 |
| `yJeahQNRHNWt...` | 700.23 | 465,263,999 |
| `BXAxLMMMUNYf...` | 527.30 | 462,239,999 |

## Economic indicators

| Metric | Value |
| --- | --- |
| SOL price | $89.18 |
| SOL 24h | -1.10% |
| SOL 7d | -6.91% |
| SOL 30d | -19.34% |
| Market cap | $52.71B |
| Spot volume 24h | $847.71M |
| Circulating supply | 591.04M SOL |
| Circulating share | 92.76% |
| DeFi TVL | $5.18B |
| TVL 24h | -0.92% |
| TVL 7d | -4.29% |
| Stablecoin supply | $14.66B |
| DEX volume 24h | $1.30B |
| DEX volume 7d | $11.17B |
| Chain fees 24h (REV proxy) | $7.98M |

_REV basis: DeFiLlama chain fees (24h). Proxy, not an official REV series._

## Upgrades and proposals

- **Alpenglow** - Consensus replacement (Votor + Rotor) targeting ~150ms finality, retiring the current TowerBFT vote-by-transaction design.
- **SIMD-0525** - Referenced in the brief as an upcoming change; tracked live from the solana-improvement-documents repository feed.
- **Firedancer** - Independent validator client from Jump; matters for client diversity and therefore for liveness risk.

SIMDs referenced in the last feed window: SIMD-0504, SIMD-0123

## Ecosystem news

- [Release v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0)
- [Release v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1)
- [Release v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0)
- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4)
- [v4.5.0-alpha.3: Bump version to 4.5.0-alpha.3 (#16402)](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.3)
- [v4.4.0-rc.0: Bump version to 4.4.0-rc.0 (#16364)](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0)
- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1)
- [Release v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2)

## Not collected

Listing these explicitly is deliberate: a gap that is named is a gap a reader can reason about, and no number in this report is a guess standing in for one.

- **daily_active_addresses** - No key-free public endpoint. Available via Dune; enable with --dune-key.
- **tokenized_equity_volume** - Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API.
- **mev_tips** - Jito tip data needs the Jito API; excluded to keep the run key-free.
- **ecosystem/https://solana.com/news/rss.xml** - probe failed: HTTP 429
- **ecosystem/https://github.com/solana-foundation/solana-improvement-documents/commits/main.atom** - probe failed: HTTP 504

---

Produced by solstate. Every figure above comes from a public endpoint that needs no API key. Source and freshness for each probe is in `report.json` under `collection.probes`.
