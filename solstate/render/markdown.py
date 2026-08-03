"""Human-readable Markdown rendering."""
from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

SEV_ICON = {"critical": "[CRITICAL]", "warning": "[WARNING]", "info": "[INFO]"}


def _fmt(v: Any, unit: str = "", nd: int = 2) -> str:
    if v is None:
        return "unavailable"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, float)):
        if unit == "usd":
            return f"${_human(v)}"
        if unit == "pct":
            return f"{v:,.2f}%"
        if unit == "sol":
            return f"{_human(v)} SOL"
        if isinstance(v, int):
            return f"{v:,}"
        return f"{v:,.{nd}f}"
    return str(v)


def _human(v: float) -> str:
    a = abs(v)
    for cut, suf in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if a >= cut:
            return f"{v / cut:,.2f}{suf}"
    return f"{v:,.2f}"


def _row(label: str, value: str) -> str:
    return f"| {label} | {value} |"


def _table(rows: List[str], head: str = "Metric", val: str = "Value") -> str:
    if not rows:
        return "_No data collected for this section._\n"
    return "\n".join([f"| {head} | {val} |", "| --- | --- |", *rows]) + "\n"


def render(report: Dict[str, Any]) -> str:
    m: Dict[str, Any] = report.get("metrics", {})
    col = report.get("collection", {})
    out: List[str] = []
    a = out.append

    a("# Solana Ecosystem State Report\n")
    a(f"Generated **{report.get('generated_at_iso')}** in {report.get('duration_ms', 0) / 1000:.1f}s "
      f"across {col.get('http_calls', 0)} HTTP calls.\n")

    # ---- headline health -----------------------------------------------------
    s = report.get("anomaly_summary", {})
    if s.get("critical"):
        verdict = f"**{s['critical']} critical** anomal{'y' if s['critical'] == 1 else 'ies'} open"
    elif s.get("warning"):
        verdict = f"{s['warning']} warning-level anomal{'y' if s['warning'] == 1 else 'ies'}"
    else:
        verdict = "No anomalies above threshold"
    a(f"> **Status:** {verdict}. "
      f"Data completeness {col.get('completeness_pct', 0)}% "
      f"({col.get('probes_ok', 0)}/{col.get('probes_total', 0)} probes returned data). "
      f"History depth: {col.get('history_runs', 0)} prior runs.\n")

    # ---- anomalies -----------------------------------------------------------
    a("## Anomalies\n")
    anomalies = report.get("anomalies") or []
    if not anomalies:
        a("Nothing outside the configured thresholds or the statistical baseline.\n")
        if col.get("history_runs", 0) < 8:
            a("\n_Note: fewer than 8 prior runs are stored, so statistical detection is not "
              "active yet. Rule-based checks are._\n")
    else:
        for an in anomalies:
            icon = SEV_ICON.get(an.get("severity", ""), "[?]")
            a(f"- {icon} **{an.get('metric')}** ({an.get('kind')}) - {an.get('message')}")
        a("")

    # ---- network -------------------------------------------------------------
    a("## Network performance\n")
    a(_table([
        _row("Health", _fmt(m.get("health"))),
        _row("Epoch", _fmt(m.get("epoch"))),
        _row("Epoch progress", _fmt(m.get("epoch_progress_pct"), "pct")),
        _row("Epoch time remaining (est.)", _dur(m.get("epoch_remaining_seconds_est"))),
        _row("Absolute slot", _fmt(m.get("absolute_slot"))),
        _row("Block height", _fmt(m.get("block_height"))),
        _row("TPS (all)", _fmt(m.get("tps"))),
        _row("TPS (non-vote)", _fmt(m.get("tps_non_vote"))),
        _row("TPS (30-sample mean)", _fmt(m.get("tps_avg_30_samples"))),
        _row("Slot time", f"{_fmt(m.get('slot_time_ms'))} ms" if m.get("slot_time_ms") else "unavailable"),
        _row("Block lag vs wall clock", _dur(m.get("block_lag_seconds"))),
        _row("Lifetime transactions", _fmt(m.get("transaction_count"))),
    ]))

    # ---- validators ----------------------------------------------------------
    a("## Validators\n")
    a(_table([
        _row("Active", _fmt(m.get("validators_active"))),
        _row("Delinquent", _fmt(m.get("validators_delinquent"))),
        _row("Delinquent share of stake", _fmt(m.get("delinquent_pct_by_stake"), "pct")),
        _row("Total active stake", _fmt(m.get("total_active_stake_sol"), "sol")),
        _row("Nakamoto coefficient", _fmt(m.get("nakamoto_coefficient"))),
        _row("Stake in top 10", _fmt(m.get("stake_top_10_pct"), "pct")),
        _row("Stake in top 20", _fmt(m.get("stake_top_20_pct"), "pct")),
        _row("Stake in top 50", _fmt(m.get("stake_top_50_pct"), "pct")),
        _row("Median commission", _fmt(m.get("commission_median_pct"), "pct")),
        _row("Validators at 0% commission", _fmt(m.get("commission_zero_count"))),
        _row("Validators at 100% commission", _fmt(m.get("commission_hundred_count"))),
    ]))

    top = (report.get("sections", {}).get("validators", {}) or {}).get("top") or []
    if top:
        a("### Largest validators by active stake\n")
        a("| # | Node | Stake (SOL) | Share | Commission |")
        a("| --- | --- | --- | --- | --- |")
        for v in top[:15]:
            node = (v.get("node_pubkey") or "")[:12] + "..."
            a(f"| {v.get('rank')} | `{node}` | {_human(v.get('stake_sol') or 0)} | "
              f"{_fmt(v.get('stake_pct'), 'pct')} | {_fmt(v.get('commission_pct'), 'pct')} |")
        a("")

    delq = (report.get("sections", {}).get("validators", {}) or {}).get("delinquent_sample") or []
    if delq:
        a("### Largest delinquent validators\n")
        a("| Node | Stake (SOL) | Last vote |")
        a("| --- | --- | --- |")
        for v in delq:
            node = (v.get("node_pubkey") or "")[:12] + "..."
            a(f"| `{node}` | {_human(v.get('stake_sol') or 0)} | {_fmt(v.get('last_vote'))} |")
        a("")

    # ---- economics -----------------------------------------------------------
    a("## Economic indicators\n")
    a(_table([
        _row("SOL price", _fmt(m.get("sol_price_usd"), "usd")),
        _row("SOL 24h", _fmt(m.get("sol_change_24h_pct"), "pct")),
        _row("SOL 7d", _fmt(m.get("sol_change_7d_pct"), "pct")),
        _row("SOL 30d", _fmt(m.get("sol_change_30d_pct"), "pct")),
        _row("Market cap", _fmt(m.get("sol_market_cap_usd"), "usd")),
        _row("Spot volume 24h", _fmt(m.get("sol_volume_24h_usd"), "usd")),
        _row("Circulating supply", _fmt(m.get("sol_circulating"), "sol")),
        _row("Circulating share", _fmt(m.get("sol_circulating_pct"), "pct")),
        _row("DeFi TVL", _fmt(m.get("tvl_usd"), "usd")),
        _row("TVL 24h", _fmt(m.get("tvl_change_24h_pct"), "pct")),
        _row("TVL 7d", _fmt(m.get("tvl_change_7d_pct"), "pct")),
        _row("Stablecoin supply", _fmt(m.get("stablecoin_supply_usd"), "usd")),
        _row("DEX volume 24h", _fmt(m.get("dex_volume_24h_usd"), "usd")),
        _row("DEX volume 7d", _fmt(m.get("dex_volume_7d_usd"), "usd")),
        _row("Chain fees 24h (REV proxy)", _fmt(m.get("chain_fees_24h_usd"), "usd")),
    ]))
    if m.get("rev_proxy_basis"):
        a(f"_REV basis: {m['rev_proxy_basis']}_\n")

    # ---- ecosystem -----------------------------------------------------------
    eco = report.get("sections", {}).get("ecosystem", {}) or {}
    a("## Upgrades and proposals\n")
    for u in eco.get("upgrades", []):
        a(f"- **{u['id']}** - {u['what']}")
    if eco.get("metrics", {}).get("simds_mentioned_recently"):
        a(f"\nSIMDs referenced in the last feed window: "
          f"{', '.join(eco['metrics']['simds_mentioned_recently'])}\n")
    else:
        a("")

    news = eco.get("news") or []
    if news:
        a("## Ecosystem news\n")
        for n in news[:15]:
            title = n.get("title", "").replace("|", "-")
            link = n.get("link") or ""
            a(f"- [{title}]({link})" if link else f"- {title}")
        a("")

    # ---- what is missing -----------------------------------------------------
    missing = report.get("not_collected") or []
    failed = [p for p in col.get("probes", []) if p.get("status") != "ok"]
    if missing or failed:
        a("## Not collected\n")
        a("Listing these explicitly is deliberate: a gap that is named is a gap a reader "
          "can reason about, and no number in this report is a guess standing in for one.\n")
        for x in missing:
            a(f"- **{x['metric']}** - {x['reason']}")
        for p in failed:
            a(f"- **{p.get('section')}/{p.get('probe')}** - probe failed: {p.get('error', 'unknown')}")
        a("")

    a("---\n")
    a(f"Produced by solstate. Every figure above comes from a public endpoint that needs no API "
      f"key. Source and freshness for each probe is in `report.json` under `collection.probes`.\n")
    return "\n".join(out)


def _dur(seconds: Optional[float]) -> str:
    if seconds is None:
        return "unavailable"
    seconds = int(seconds)
    if abs(seconds) < 60:
        return f"{seconds}s"
    if abs(seconds) < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    return f"{seconds // 3600}h {(seconds % 3600) // 60}m"
