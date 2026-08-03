"""Assemble one report: collect every source, score freshness, detect anomalies.

The output of :func:`build` is the single canonical object. The JSON, Markdown
and HTML renderers are all pure functions of it, so the three outputs can never
disagree with each other -- a failure mode that is easy to ship and hard to
notice.
"""
from __future__ import annotations

import time
from typing import Any, Dict, List

from .anomaly import detect
from .config import Config
from .history import History
from .net import JsonClient
from .sources.chain import collect_network, collect_supply, collect_validators
from .sources.dune import collect_dune
from .sources.ecosystem import collect_ecosystem
from .sources.market import collect_defi, collect_market, UNAVAILABLE_WITHOUT_KEY

SCHEMA_VERSION = "1.0"


def _flatten_meta(section: Dict[str, Any], prefix: str, into: List[Dict[str, Any]]) -> None:
    for key, m in (section.get("meta") or {}).items():
        if isinstance(m, dict) and "status" in m:
            into.append({"section": prefix, "probe": key, **m})


def build(cfg: Config, history: History | None = None) -> Dict[str, Any]:
    t0 = time.time()
    client = JsonClient(cfg.timeout, cfg.retries, cfg.user_agent)

    sections = {
        "network": collect_network(client, cfg),
        "supply": collect_supply(client, cfg),
        "validators": collect_validators(client, cfg),
        "market": collect_market(client, cfg),
        "defi": collect_defi(client, cfg),
        "ecosystem": collect_ecosystem(client, cfg),
        "dune": collect_dune(client, cfg),
    }

    # One flat namespace of scalars, which is what history and anomaly work on.
    metrics: Dict[str, Any] = {}
    for name, sec in sections.items():
        for k, v in (sec.get("metrics") or {}).items():
            if isinstance(v, (int, float, str)) or v is None:
                metrics[k] = v

    probes: List[Dict[str, Any]] = []
    for name, sec in sections.items():
        _flatten_meta(sec, name, probes)
    ok_probes = sum(1 for p in probes if p.get("status") == "ok")
    failures = len(probes) - ok_probes

    hist: Dict[str, List[float]] = {}
    runs = 0
    if history is not None:
        runs = history.run_count()
        for name in history.names():
            vals = history.values(name, 500)
            if vals:
                hist[name] = vals

    anomalies = detect(metrics, hist, cfg.thresholds)

    duration_ms = int((time.time() - t0) * 1000)
    report: Dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": int(time.time()),
        "generated_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "duration_ms": duration_ms,
        "collection": {
            "probes_total": len(probes),
            "probes_ok": ok_probes,
            "probes_failed": failures,
            "http_calls": client.calls,
            # An explicit completeness number keeps a half-broken run from
            # looking like a healthy one at a glance.
            "completeness_pct": round(100.0 * ok_probes / len(probes), 1) if probes else 0.0,
            "history_runs": runs,
            "probes": probes,
        },
        "metrics": metrics,
        "sections": sections,
        "anomalies": [a.to_dict() for a in anomalies],
        "anomaly_summary": {
            "critical": sum(1 for a in anomalies if a.severity == "critical"),
            "warning": sum(1 for a in anomalies if a.severity == "warning"),
            "info": sum(1 for a in anomalies if a.severity == "info"),
        },
        "not_collected": UNAVAILABLE_WITHOUT_KEY if not cfg.dune_api_key else [],
        "config": cfg.to_dict(),
    }

    if history is not None:
        history.record(metrics, report["generated_at"])
        history.record_run(failures == 0, len(probes), failures, duration_ms,
                           report["generated_at"])
        history.prune()
        # Attach short series for the sparklines the HTML renderer draws.
        report["series"] = {
            name: history.series(name, 120)
            for name in ("tps", "tps_non_vote", "slot_time_ms", "sol_price_usd",
                         "tvl_usd", "validators_active", "delinquent_pct_by_stake",
                         "stablecoin_supply_usd", "dex_volume_24h_usd")
            if history.series(name, 2)
        }
    else:
        report["series"] = {}

    return report
