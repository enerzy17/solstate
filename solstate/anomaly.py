"""Anomaly detection: rules for the things we already know are bad, statistics
for the things we do not.

The statistical half uses the **median absolute deviation**, not the mean and
standard deviation. Chain metrics are spiky and heavy-tailed; a single outage
inflates a standard deviation enough to hide the next three outages. MAD has a
breakdown point of 50%, so half the history can be garbage and the estimate
still holds.

    robust_z = 0.6745 * (x - median) / MAD

0.6745 is the 75th percentile of the standard normal, which rescales MAD so the
cutoff is comparable to a normal z-score.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Sequence

MIN_HISTORY = 8          # below this, a "baseline" is noise pretending to be one
SCALE = 0.6745

# Metrics that trend by construction. A robust z-score is meaningless for these:
# a counter that only ever goes up is *always* far from its own trailing median,
# so z-scoring them emits a critical finding on every single run. That is alert
# fatigue, which is worse than no detector at all -- an operator who learns to
# ignore the panel will also ignore the one finding that mattered.
#
# They are not dropped, they are monitored differently: see STALL/REGRESSION
# below, where the meaningful failure for a counter is that it stopped advancing
# or went backwards, not that it is large.
MONOTONIC = {
    "absolute_slot", "block_height", "block_time_unix", "transaction_count", "epoch",
    "sol_ath_usd",
}
# Sawtooth within an epoch: climbs to 100% then resets. Same problem, same fix.
CYCLIC = {
    "epoch_progress_pct", "epoch_remaining_seconds_est", "slot_index", "slots_in_epoch",
}
NO_STATS = MONOTONIC | CYCLIC


@dataclass
class Anomaly:
    metric: str
    severity: str            # info | warning | critical
    kind: str                # rule | statistical
    value: float
    message: str
    baseline: Optional[float] = None
    robust_z: Optional[float] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v is not None}


def median(xs: Sequence[float]) -> float:
    s = sorted(xs)
    n = len(s)
    if not n:
        return 0.0
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def mad(xs: Sequence[float], med: Optional[float] = None) -> float:
    if not xs:
        return 0.0
    m = median(xs) if med is None else med
    return median([abs(x - m) for x in xs])


def robust_z(x: float, history: Sequence[float]) -> Optional[float]:
    """Return the MAD-based z-score of ``x`` against ``history``, or None.

    Returns None when MAD is zero. A flat history carries no dispersion
    information, so there is no honest z-score to report -- any non-zero
    difference would divide by zero and any substitute constant would be
    invented. Practical significance is handled separately by
    :data:`min_rel_change`; see :func:`detect`.
    """
    if len(history) < MIN_HISTORY:
        return None
    m = median(history)
    d = mad(history, m)
    if d == 0:
        return None
    return SCALE * (x - m) / d


def rel_change(x: float, baseline: float) -> float:
    """Absolute fractional change of ``x`` from ``baseline``, as a percentage."""
    if baseline == 0:
        return 0.0 if x == 0 else float("inf")
    return abs(x - baseline) / abs(baseline) * 100.0


def detect(metrics: Dict[str, object], history: Dict[str, List[float]],
           thresholds: Dict[str, float]) -> List[Anomaly]:
    """Run both halves of detection and return findings, worst first."""
    found: List[Anomaly] = []

    def num(key) -> Optional[float]:
        v = metrics.get(key)
        return float(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else None

    # ---- rules ---------------------------------------------------------------
    health = metrics.get("health")
    if health is not None and health != "ok":
        found.append(Anomaly("health", "critical", "rule", 0.0,
                             f"getHealth returned {health!r} rather than 'ok'."))

    tps = num("tps")
    tps_hist = history.get("tps", [])
    if tps is not None and len(tps_hist) >= MIN_HISTORY:
        base = median(tps_hist)
        if base:
            change = (tps - base) / base * 100.0
            if change <= -thresholds["tps_drop_pct"]:
                found.append(Anomaly("tps", "critical", "rule", tps,
                                     f"TPS {tps:.0f} is {abs(change):.0f}% below the "
                                     f"trailing median of {base:.0f}.", base))
            elif change >= thresholds["tps_spike_pct"]:
                found.append(Anomaly("tps", "info", "rule", tps,
                                     f"TPS {tps:.0f} is {change:.0f}% above the "
                                     f"trailing median of {base:.0f}.", base))

    slot_ms = num("slot_time_ms")
    if slot_ms is not None and slot_ms > thresholds["slot_time_ms_max"]:
        found.append(Anomaly("slot_time_ms", "warning", "rule", slot_ms,
                             f"Slot time {slot_ms:.0f}ms exceeds "
                             f"{thresholds['slot_time_ms_max']:.0f}ms; the network target is 400ms."))

    delq = num("delinquent_pct_by_stake")
    if delq is not None and delq > thresholds["delinquent_stake_pct_max"]:
        sev = "critical" if delq > 2 * thresholds["delinquent_stake_pct_max"] else "warning"
        found.append(Anomaly("delinquent_pct_by_stake", sev, "rule", delq,
                             f"{delq:.2f}% of active stake is delinquent, above the "
                             f"{thresholds['delinquent_stake_pct_max']:.0f}% limit."))

    lag = num("block_lag_seconds")
    if lag is not None and lag > 60:
        found.append(Anomaly("block_lag_seconds", "warning", "rule", lag,
                             f"Latest block is {lag:.0f}s behind wall clock."))

    for key, label, limit_key in (
        ("tvl_change_24h_pct", "TVL", "tvl_change_pct"),
        ("sol_change_24h_pct", "SOL price", "sol_price_change_pct"),
    ):
        v = num(key)
        if v is not None and abs(v) >= thresholds[limit_key]:
            found.append(Anomaly(key, "warning", "rule", v,
                                 f"{label} moved {v:+.1f}% in 24h, beyond the "
                                 f"{thresholds[limit_key]:.0f}% band."))

    # A validator set that suddenly loses members is worth surfacing even when
    # delinquency percentages still look fine.
    for key in ("validators_active", "nakamoto_coefficient"):
        v, hist = num(key), history.get(key, [])
        if v is not None and len(hist) >= MIN_HISTORY:
            base = median(hist)
            if base and (v - base) / base * 100 <= -10:
                found.append(Anomaly(key, "warning", "rule", v,
                                     f"{key} fell to {v:.0f} from a median of {base:.0f}.", base))

    # ---- counters: the failure is a stall or a regression, not a magnitude ----
    for name in MONOTONIC:
        v, hist = num(name), history.get(name, [])
        if v is None or not hist:
            continue
        prev = hist[-1]
        if v < prev:
            # A chain counter going backwards means the RPC served stale or
            # forked data. Worth knowing, and invisible to any z-score.
            found.append(Anomaly(name, "critical", "rule", v,
                                 f"{name} went backwards, {prev:.0f} -> {v:.0f}. The endpoint "
                                 f"served stale or forked data.", prev))
        elif v == prev and name in ("absolute_slot", "block_height"):
            found.append(Anomaly(name, "critical", "rule", v,
                                 f"{name} has not advanced since the previous run "
                                 f"(still {v:.0f}). The cluster or the endpoint is stalled.", prev))

    # ---- statistics ----------------------------------------------------------
    ruled = {a.metric for a in found}
    for name, hist in history.items():
        if name in ruled or name in NO_STATS:
            continue                       # a rule already said it better
        v = num(name)
        if v is None:
            continue
        z = robust_z(v, hist)
        if z is None or abs(z) < thresholds["mad_z"]:
            continue
        base = median(hist)
        # Statistical significance is not practical significance. A very stable
        # metric sampled often has a near-zero MAD, so a 0.001% move can score
        # z=95 and mean nothing. Requiring a floor on the *relative* move is what
        # stops the panel filling with arithmetically-true noise. This was found
        # by running the collector against mainnet, not by reasoning about it.
        change = rel_change(v, base)
        if change < thresholds["min_rel_change"]:
            continue
        # Statistical findings never escalate past "warning". A z-score knows
        # that something is unusual against its own history; it does not know
        # that anything is wrong. "Critical" implies act now, and only the rules
        # -- which encode actual domain knowledge about what bad looks like --
        # have earned the right to say that. Solana TPS genuinely swings 40%+
        # between samples; that is worth a glance, not an alarm.
        found.append(Anomaly(
            name, "warning",
            "statistical", v,
            f"{name} is {abs(z):.1f} robust deviations from its {len(hist)}-point median "
            f"of {base:.4g}, a {change:.1f}% move.",
            base, round(z, 2)))

    order = {"critical": 0, "warning": 1, "info": 2}
    found.sort(key=lambda a: (order.get(a.severity, 3), a.metric))
    return found
