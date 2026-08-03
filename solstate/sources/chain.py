"""On-chain state, straight from Solana JSON-RPC. No key, no indexer, no vendor.

Every metric here is derived from a documented RPC method:
``getHealth``, ``getEpochInfo``, ``getSlot``, ``getBlockTime``,
``getRecentPerformanceSamples``, ``getVoteAccounts``, ``getSupply``.
"""
from __future__ import annotations

import time
from typing import Any, Dict, List

from ..config import Config
from ..net import Fetched, JsonClient

LAMPORTS = 1_000_000_000


def _pct(part: float, whole: float) -> float:
    return round(100.0 * part / whole, 4) if whole else 0.0


def collect_network(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    """Network performance: health, TPS, slot time, block height, epoch progress."""
    out: Dict[str, Any] = {"metrics": {}, "meta": {}}

    health = client.rpc(cfg.rpcs, "getHealth")
    out["meta"]["health"] = health.to_dict()
    out["metrics"]["health"] = health.value if health.ok else None

    epoch = client.rpc(cfg.rpcs, "getEpochInfo")
    out["meta"]["epoch"] = epoch.to_dict()
    if epoch.ok and isinstance(epoch.value, dict):
        e = epoch.value
        slots_in = e.get("slotsInEpoch") or 0
        idx = e.get("slotIndex") or 0
        # Mainnet targets 400ms slots. Remaining time is an estimate and is
        # labelled as one everywhere it is rendered.
        remaining_s = int((slots_in - idx) * 0.4) if slots_in else None
        out["metrics"].update({
            "epoch": e.get("epoch"),
            "absolute_slot": e.get("absoluteSlot"),
            "block_height": e.get("blockHeight"),
            "slot_index": idx,
            "slots_in_epoch": slots_in,
            "epoch_progress_pct": _pct(idx, slots_in),
            "epoch_remaining_seconds_est": remaining_s,
            "transaction_count": e.get("transactionCount"),
        })

    perf = client.rpc(cfg.rpcs, "getRecentPerformanceSamples", [30])
    out["meta"]["performance"] = perf.to_dict()
    if perf.ok and isinstance(perf.value, list) and perf.value:
        samples = [s for s in perf.value if s.get("samplePeriodSecs")]
        if samples:
            latest = samples[0]
            period = latest["samplePeriodSecs"]
            tps = latest.get("numTransactions", 0) / period
            # Non-vote TPS is the number people actually mean by "TPS"; vote
            # transactions are consensus overhead and dominate the raw figure.
            nv = latest.get("numNonVoteTransactions")
            slot_ms = (period / latest["numSlots"] * 1000) if latest.get("numSlots") else None
            window_tx = sum(s.get("numTransactions", 0) for s in samples)
            window_s = sum(s["samplePeriodSecs"] for s in samples)
            out["metrics"].update({
                "tps": round(tps, 2),
                "tps_non_vote": round(nv / period, 2) if nv is not None else None,
                "tps_avg_30_samples": round(window_tx / window_s, 2) if window_s else None,
                "slot_time_ms": round(slot_ms, 1) if slot_ms else None,
                "sample_period_secs": period,
            })
            out["samples"] = [
                {
                    "slot": s.get("slot"),
                    "tps": round(s.get("numTransactions", 0) / s["samplePeriodSecs"], 2),
                    "tps_non_vote": (round(s["numNonVoteTransactions"] / s["samplePeriodSecs"], 2)
                                     if s.get("numNonVoteTransactions") is not None else None),
                    "slot_time_ms": (round(s["samplePeriodSecs"] / s["numSlots"] * 1000, 1)
                                     if s.get("numSlots") else None),
                }
                for s in samples
            ]

    # Wall-clock skew between the cluster's latest block and real time is a
    # cheap, very direct liveness signal.
    slot = client.rpc(cfg.rpcs, "getSlot")
    if slot.ok and isinstance(slot.value, int):
        bt = client.rpc(cfg.rpcs, "getBlockTime", [slot.value])
        out["meta"]["block_time"] = bt.to_dict()
        if bt.ok and isinstance(bt.value, int):
            out["metrics"]["block_time_unix"] = bt.value
            out["metrics"]["block_lag_seconds"] = int(time.time()) - bt.value

    return out


def collect_supply(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    """SOL supply split. ``excludeNonCirculatingAccountsList`` keeps the payload small."""
    out: Dict[str, Any] = {"metrics": {}, "meta": {}}
    f = client.rpc(cfg.rpcs, "getSupply", [{"excludeNonCirculatingAccountsList": True}])
    out["meta"]["supply"] = f.to_dict()
    if f.ok and isinstance(f.value, dict):
        v = f.value.get("value", {})
        total = v.get("total", 0) / LAMPORTS
        circ = v.get("circulating", 0) / LAMPORTS
        out["metrics"] = {
            "sol_total_supply": round(total, 2),
            "sol_circulating": round(circ, 2),
            "sol_non_circulating": round(v.get("nonCirculating", 0) / LAMPORTS, 2),
            "sol_circulating_pct": _pct(circ, total),
        }
    return out


def collect_validators(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    """Validator set: counts, delinquency, stake concentration, commissions.

    Nakamoto coefficient here is the standard definition: the smallest number of
    validators whose combined active stake exceeds one third of the total, i.e.
    the smallest group that could halt the chain.
    """
    out: Dict[str, Any] = {"metrics": {}, "meta": {}, "top": []}
    f = client.rpc(cfg.rpcs, "getVoteAccounts")
    out["meta"]["vote_accounts"] = f.to_dict()
    if not (f.ok and isinstance(f.value, dict)):
        return out

    current: List[dict] = f.value.get("current", []) or []
    delinquent: List[dict] = f.value.get("delinquent", []) or []

    def stake(v: dict) -> float:
        return (v.get("activatedStake") or 0) / LAMPORTS

    cur_stake = sum(stake(v) for v in current)
    del_stake = sum(stake(v) for v in delinquent)
    total_stake = cur_stake + del_stake

    ranked = sorted(current, key=stake, reverse=True)
    running, nakamoto = 0.0, 0
    for i, v in enumerate(ranked, 1):
        running += stake(v)
        if total_stake and running > total_stake / 3:
            nakamoto = i
            break

    commissions = [v.get("commission") for v in current if v.get("commission") is not None]
    commissions.sort()

    def top_n_pct(n: int) -> float:
        return _pct(sum(stake(v) for v in ranked[:n]), total_stake)

    out["metrics"] = {
        "validators_active": len(current),
        "validators_delinquent": len(delinquent),
        "validators_total": len(current) + len(delinquent),
        "delinquent_pct_by_count": _pct(len(delinquent), len(current) + len(delinquent)),
        "delinquent_pct_by_stake": _pct(del_stake, total_stake),
        "total_active_stake_sol": round(total_stake, 2),
        "nakamoto_coefficient": nakamoto,
        "stake_top_10_pct": top_n_pct(10),
        "stake_top_20_pct": top_n_pct(20),
        "stake_top_50_pct": top_n_pct(50),
        "commission_median_pct": (commissions[len(commissions) // 2] if commissions else None),
        "commission_zero_count": sum(1 for c in commissions if c == 0),
        "commission_hundred_count": sum(1 for c in commissions if c == 100),
    }
    out["top"] = [
        {
            "rank": i,
            "vote_pubkey": v.get("votePubkey"),
            "node_pubkey": v.get("nodePubkey"),
            "stake_sol": round(stake(v), 2),
            "stake_pct": _pct(stake(v), total_stake),
            "commission_pct": v.get("commission"),
            "last_vote": v.get("lastVote"),
        }
        for i, v in enumerate(ranked[: cfg.validator_sample], 1)
    ]
    # Named so an operator can act on it, not just read it.
    out["delinquent_sample"] = [
        {"node_pubkey": v.get("nodePubkey"), "stake_sol": round(stake(v), 2),
         "last_vote": v.get("lastVote")}
        for v in sorted(delinquent, key=stake, reverse=True)[:10]
    ]
    return out
