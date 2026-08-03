"""Single-file interactive HTML dashboard.

Constraints this renderer holds itself to:

* **One file.** No CDN, no external stylesheet, no webfont, no image request.
  It opens from ``file://``, from GitHub Pages, or from an air-gapped box, and
  looks identical in all three.
* **No build step.** The CSS and JS are written by hand and inlined. There is
  nothing to compile, so there is nothing to break in six months.
* **Sparklines are SVG generated from real history**, not decoration. If there
  is no history for a metric, no sparkline is drawn -- an empty chart that
  implies data is worse than no chart.
"""
from __future__ import annotations

import html
import json
from typing import Any, Dict, List, Optional, Sequence

from .markdown import _human

CSS = """
:root{
  --bg:#0a0c10; --panel:#12161d; --panel2:#171c25; --line:#232a35;
  --fg:#e6edf3; --dim:#8b98a9; --accent:#14f195; --accent2:#9945ff;
  --crit:#ff5c5c; --warn:#ffb84d; --info:#58a6ff;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
  font:14px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1240px;margin:0 auto;padding:28px 20px 80px}
header{display:flex;flex-wrap:wrap;gap:16px;align-items:baseline;justify-content:space-between;
  border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:22px}
h1{margin:0;font-size:22px;letter-spacing:-.2px}
h1 span{background:linear-gradient(90deg,var(--accent),var(--accent2));
  -webkit-background-clip:text;background-clip:text;color:transparent}
h2{font-size:15px;margin:30px 0 12px;color:var(--dim);text-transform:uppercase;
  letter-spacing:.09em;font-weight:600}
.meta{color:var(--dim);font-size:12.5px;text-align:right}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(212px,1fr))}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 15px;
  position:relative;overflow:hidden}
.card .k{color:var(--dim);font-size:11.5px;text-transform:uppercase;letter-spacing:.06em}
.card .v{font-size:23px;font-weight:640;margin-top:5px;font-variant-numeric:tabular-nums;
  letter-spacing:-.4px}
.card .s{font-size:12px;margin-top:3px;color:var(--dim)}
.card.na .v{color:var(--dim);font-size:15px;font-weight:500}
.up{color:var(--accent)} .down{color:var(--crit)}
.spark{display:block;margin-top:9px;width:100%;height:30px}
.bar{height:5px;border-radius:3px;background:var(--panel2);margin-top:9px;overflow:hidden}
.bar>i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2))}
/* Wide tables scroll inside their own box. The page body must never scroll
   sideways -- on a phone that turns the whole dashboard into a swipe puzzle. */
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;border-radius:10px;margin-bottom:6px}
table{width:100%;min-width:540px;border-collapse:collapse;font-size:13px;
  background:var(--panel);border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{padding:8px 11px;text-align:left;border-bottom:1px solid var(--line)}
th{color:var(--dim);font-weight:600;font-size:11.5px;text-transform:uppercase;
  letter-spacing:.05em;cursor:pointer;user-select:none;white-space:nowrap}
th:hover{color:var(--fg)}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:var(--panel2)}
td.num{text-align:right;font-variant-numeric:tabular-nums}
code{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-size:12px;color:var(--dim)}
.anom{border-left:3px solid var(--line);background:var(--panel);border-radius:0 8px 8px 0;
  padding:11px 14px;margin-bottom:8px}
.anom.critical{border-left-color:var(--crit)}
.anom.warning{border-left-color:var(--warn)}
.anom.info{border-left-color:var(--info)}
.anom b{font-family:ui-monospace,Menlo,Consolas,monospace}
.tag{display:inline-block;padding:1px 7px;border-radius:20px;font-size:10.5px;font-weight:700;
  text-transform:uppercase;letter-spacing:.05em;vertical-align:1px}
.tag.critical{background:rgba(255,92,92,.16);color:var(--crit)}
.tag.warning{background:rgba(255,184,77,.16);color:var(--warn)}
.tag.info{background:rgba(88,166,255,.16);color:var(--info)}
.tag.ok{background:rgba(20,241,149,.14);color:var(--accent)}
.ctl{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin:14px 0}
input[type=search],select{background:var(--panel);border:1px solid var(--line);color:var(--fg);
  border-radius:7px;padding:7px 11px;font:inherit;font-size:13px;outline:none}
input[type=search]:focus,select:focus{border-color:var(--accent)}
button{background:var(--panel);border:1px solid var(--line);color:var(--dim);border-radius:7px;
  padding:7px 13px;font:inherit;font-size:13px;cursor:pointer}
button:hover{color:var(--fg);border-color:var(--accent)}
button.on{background:var(--accent);color:#04120c;border-color:var(--accent);font-weight:600}
.news{list-style:none;padding:0;margin:0}
.news li{padding:9px 0;border-bottom:1px solid var(--line)}
.news li:last-child{border-bottom:none}
.news .src{color:var(--dim);font-size:11.5px}
.note{color:var(--dim);font-size:12.5px;background:var(--panel);border:1px solid var(--line);
  border-left:3px solid var(--accent2);border-radius:0 8px 8px 0;padding:11px 14px;margin:10px 0}
footer{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);
  color:var(--dim);font-size:12px}
.hidden{display:none}
@media(max-width:640px){.grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
  .meta{text-align:left}h1{font-size:19px}}
"""

JS = """
// Sortable tables. Click a header; numeric columns sort numerically.
document.querySelectorAll('table.sortable').forEach(function(t){
  t.querySelectorAll('th').forEach(function(th,i){
    th.addEventListener('click',function(){
      var body=t.tBodies[0], rows=[].slice.call(body.rows);
      var dir=th.dataset.dir==='asc'?-1:1;
      t.querySelectorAll('th').forEach(function(o){delete o.dataset.dir;});
      th.dataset.dir=dir===1?'asc':'desc';
      rows.sort(function(a,b){
        var x=a.cells[i], y=b.cells[i];
        var xv=x.dataset.sort!==undefined?parseFloat(x.dataset.sort):x.textContent.trim();
        var yv=y.dataset.sort!==undefined?parseFloat(y.dataset.sort):y.textContent.trim();
        if(typeof xv==='number'&&typeof yv==='number') return (xv-yv)*dir;
        return String(xv).localeCompare(String(yv))*dir;
      });
      rows.forEach(function(r){body.appendChild(r);});
    });
  });
});
// Filter the validator table.
var vf=document.getElementById('vfilter');
if(vf) vf.addEventListener('input',function(){
  var q=this.value.toLowerCase();
  document.querySelectorAll('#vtable tbody tr').forEach(function(r){
    r.classList.toggle('hidden', q && r.textContent.toLowerCase().indexOf(q)<0);
  });
});
// Severity filter for anomalies.
document.querySelectorAll('[data-sev]').forEach(function(b){
  b.addEventListener('click',function(){
    document.querySelectorAll('[data-sev]').forEach(function(o){o.classList.remove('on');});
    b.classList.add('on');
    var s=b.dataset.sev;
    document.querySelectorAll('.anom').forEach(function(a){
      a.classList.toggle('hidden', s!=='all' && !a.classList.contains(s));
    });
  });
});
// Relative age of the report, updated live so a stale tab is obvious.
(function(){
  var el=document.getElementById('age'); if(!el) return;
  var t=parseInt(el.dataset.ts,10)*1000;
  function tick(){
    var s=Math.max(0,Math.floor((Date.now()-t)/1000));
    var txt = s<60? s+'s ago' : s<3600? Math.floor(s/60)+'m ago'
            : s<86400? Math.floor(s/3600)+'h ago' : Math.floor(s/86400)+'d ago';
    el.textContent=txt;
    el.style.color = s>7200 ? 'var(--warn)' : '';
  }
  tick(); setInterval(tick,1000);
})();
"""


def _esc(s: Any) -> str:
    return html.escape(str(s), quote=True)


def _sparkline(points: Sequence[float], w: int = 200, h: int = 30) -> str:
    """An SVG polyline scaled to the data. Returns '' when there is nothing real to draw."""
    vals = [v for v in points if isinstance(v, (int, float))]
    if len(vals) < 3:
        return ""
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1.0
    step = w / (len(vals) - 1)
    pts = " ".join(f"{i * step:.1f},{h - 2 - ((v - lo) / span) * (h - 4):.1f}"
                   for i, v in enumerate(vals))
    rising = vals[-1] >= vals[0]
    colour = "var(--accent)" if rising else "var(--crit)"
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" preserveAspectRatio="none" '
            f'aria-hidden="true"><polyline points="{pts}" fill="none" stroke="{colour}" '
            f'stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/></svg>')


def _card(label: str, value: Any, sub: str = "", unit: str = "",
          series: Optional[Sequence[float]] = None, pct_bar: Optional[float] = None) -> str:
    if value is None:
        return (f'<div class="card na"><div class="k">{_esc(label)}</div>'
                f'<div class="v">unavailable</div>'
                f'{f"<div class=s>{_esc(sub)}</div>" if sub else ""}</div>')
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if unit == "usd":
            shown = "$" + _human(value)
        elif unit == "pct":
            shown = f"{value:,.2f}%"
        elif unit == "sol":
            shown = _human(value) + " SOL"
        elif isinstance(value, int):
            shown = f"{value:,}"
        else:
            shown = f"{value:,.2f}"
    else:
        shown = str(value)
    cls = ""
    if sub.startswith("+"):
        cls = " up"
    elif sub.startswith("-"):
        cls = " down"
    bar = (f'<div class="bar"><i style="width:{max(0, min(100, pct_bar)):.1f}%"></i></div>'
           if pct_bar is not None else "")
    return (f'<div class="card"><div class="k">{_esc(label)}</div>'
            f'<div class="v">{_esc(shown)}</div>'
            f'{f"<div class=\'s{cls}\'>{_esc(sub)}</div>" if sub else ""}'
            f'{bar}{_sparkline(series or [])}</div>')


def _chg(v: Optional[float], window: str) -> str:
    return "" if v is None else f"{v:+.2f}% {window}"


def render(report: Dict[str, Any]) -> str:
    m: Dict[str, Any] = report.get("metrics", {})
    col = report.get("collection", {})
    ser: Dict[str, List] = report.get("series", {}) or {}

    def sv(name: str) -> List[float]:
        return [p[1] for p in ser.get(name, [])]

    out: List[str] = []
    a = out.append

    a("<!doctype html><html lang=en><head><meta charset=utf-8>")
    a('<meta name="viewport" content="width=device-width,initial-scale=1">')
    a("<title>Solana Ecosystem State Report</title>")
    a(f"<style>{CSS}</style></head><body><div class=wrap>")

    sm = report.get("anomaly_summary", {})
    if sm.get("critical"):
        badge = f'<span class="tag critical">{sm["critical"]} critical</span>'
    elif sm.get("warning"):
        badge = f'<span class="tag warning">{sm["warning"]} warning</span>'
    else:
        badge = '<span class="tag ok">nominal</span>'

    a("<header><div>")
    a("<h1><span>Solana</span> Ecosystem State Report</h1>")
    a(f'<div class=meta style="text-align:left;margin-top:6px">{badge} &nbsp;'
      f'{col.get("completeness_pct", 0)}% data completeness &middot; '
      f'{col.get("probes_ok", 0)}/{col.get("probes_total", 0)} probes &middot; '
      f'{col.get("history_runs", 0)} runs stored</div>')
    a("</div><div class=meta>")
    a(f'generated <b id=age data-ts="{report.get("generated_at", 0)}">just now</b><br>')
    a(f'{_esc(report.get("generated_at_iso"))}<br>')
    a(f'{report.get("duration_ms", 0) / 1000:.1f}s &middot; {col.get("http_calls", 0)} HTTP calls')
    a("</div></header>")

    # ---- anomalies -----------------------------------------------------------
    anomalies = report.get("anomalies") or []
    a("<h2>Anomalies</h2>")
    if anomalies:
        a('<div class=ctl><button class=on data-sev=all>All</button>'
          '<button data-sev=critical>Critical</button>'
          '<button data-sev=warning>Warning</button>'
          '<button data-sev=info>Info</button></div>')
        for an in anomalies:
            sev = _esc(an.get("severity", "info"))
            z = an.get("robust_z")
            extra = f' <code>z={z}</code>' if z is not None else ""
            a(f'<div class="anom {sev}"><span class="tag {sev}">{sev}</span> '
              f'<b>{_esc(an.get("metric"))}</b> '
              f'<code>{_esc(an.get("kind"))}</code>{extra}<br>{_esc(an.get("message"))}</div>')
    else:
        a('<div class=note>Nothing outside the configured thresholds or the statistical '
          'baseline.'
          + ("  Fewer than 8 prior runs are stored, so statistical detection is not active yet; "
             "rule-based checks are." if col.get("history_runs", 0) < 8 else "") +
          "</div>")

    # ---- network -------------------------------------------------------------
    a("<h2>Network performance</h2><div class=grid>")
    health = m.get("health")
    a(_card("Cluster health", health if health else None,
            "getHealth" if health == "ok" else "not ok"))
    a(_card("TPS (non-vote)", m.get("tps_non_vote"), "excludes consensus votes",
            series=sv("tps_non_vote")))
    a(_card("TPS (all)", m.get("tps"), "latest 60s sample", series=sv("tps")))
    a(_card("Slot time", m.get("slot_time_ms"), "target 400ms", series=sv("slot_time_ms")))
    a(_card("Epoch", m.get("epoch"),
            f'{m.get("epoch_progress_pct", 0):.1f}% complete' if m.get("epoch_progress_pct") else "",
            pct_bar=m.get("epoch_progress_pct")))
    a(_card("Block height", m.get("block_height")))
    a(_card("Absolute slot", m.get("absolute_slot")))
    a(_card("Block lag", m.get("block_lag_seconds"), "seconds behind wall clock"))
    a("</div>")

    # ---- validators ----------------------------------------------------------
    a("<h2>Validators</h2><div class=grid>")
    a(_card("Active", m.get("validators_active"), series=sv("validators_active")))
    a(_card("Delinquent", m.get("validators_delinquent"),
            f'{m.get("delinquent_pct_by_stake", 0):.2f}% of stake'))
    a(_card("Delinquent stake", m.get("delinquent_pct_by_stake"), unit="pct",
            series=sv("delinquent_pct_by_stake")))
    a(_card("Nakamoto coefficient", m.get("nakamoto_coefficient"),
            "validators to halt the chain"))
    a(_card("Total active stake", m.get("total_active_stake_sol"), unit="sol"))
    a(_card("Stake in top 10", m.get("stake_top_10_pct"), unit="pct",
            pct_bar=m.get("stake_top_10_pct")))
    a(_card("Stake in top 20", m.get("stake_top_20_pct"), unit="pct",
            pct_bar=m.get("stake_top_20_pct")))
    a(_card("Median commission", m.get("commission_median_pct"), unit="pct"))
    a("</div>")

    top = (report.get("sections", {}).get("validators", {}) or {}).get("top") or []
    if top:
        a('<div class=ctl><input type=search id=vfilter placeholder="Filter validators by pubkey">'
          '<span class=meta style="text-align:left">click a column to sort</span></div>')
        a('<div class=tw><table class=sortable id=vtable><thead><tr><th>#</th><th>Node</th>'
          '<th>Stake (SOL)</th><th>Share</th><th>Commission</th><th>Last vote</th>'
          '</tr></thead><tbody>')
        for v in top:
            last = v.get("last_vote")
            last_cell = (f'<td class=num data-sort="{last}">{last:,}</td>'
                         if isinstance(last, int) else '<td class=num data-sort="0">-</td>')
            comm = v.get("commission_pct")
            comm_cell = (f'<td class=num data-sort="{comm}">{comm}%</td>'
                         if isinstance(comm, (int, float)) else '<td class=num>-</td>')
            a(f'<tr><td class=num data-sort="{v.get("rank")}">{v.get("rank")}</td>'
              f'<td><code>{_esc((v.get("node_pubkey") or "")[:20])}...</code></td>'
              f'<td class=num data-sort="{v.get("stake_sol") or 0}">'
              f'{_human(v.get("stake_sol") or 0)}</td>'
              f'<td class=num data-sort="{v.get("stake_pct") or 0}">'
              f'{(v.get("stake_pct") or 0):.3f}%</td>'
              f'{comm_cell}{last_cell}</tr>')
        a("</tbody></table></div>")

    # ---- economics -----------------------------------------------------------
    a("<h2>Economic indicators</h2><div class=grid>")
    a(_card("SOL price", m.get("sol_price_usd"), _chg(m.get("sol_change_24h_pct"), "24h"),
            "usd", sv("sol_price_usd")))
    a(_card("Market cap", m.get("sol_market_cap_usd"), unit="usd"))
    a(_card("Spot volume 24h", m.get("sol_volume_24h_usd"), unit="usd"))
    a(_card("DeFi TVL", m.get("tvl_usd"), _chg(m.get("tvl_change_24h_pct"), "24h"),
            "usd", sv("tvl_usd")))
    a(_card("Stablecoin supply", m.get("stablecoin_supply_usd"), unit="usd",
            series=sv("stablecoin_supply_usd")))
    a(_card("DEX volume 24h", m.get("dex_volume_24h_usd"),
            _chg(m.get("dex_volume_change_24h_pct"), "24h"), "usd", sv("dex_volume_24h_usd")))
    a(_card("Chain fees 24h", m.get("chain_fees_24h_usd"), "REV proxy", "usd"))
    a(_card("Circulating SOL", m.get("sol_circulating"),
            f'{m.get("sol_circulating_pct", 0):.1f}% of total', "sol",
            pct_bar=m.get("sol_circulating_pct")))
    a("</div>")

    stb = m.get("stablecoin_breakdown") or {}
    if isinstance(stb, dict) and stb:
        a('<div class=tw><table class=sortable><thead><tr><th>Peg type</th><th>Circulating (USD)</th></tr>'
          "</thead><tbody>")
        for k, v in sorted(stb.items(), key=lambda kv: -(kv[1] or 0)):
            a(f'<tr><td>{_esc(k)}</td><td class=num data-sort="{v or 0}">${_human(v or 0)}</td></tr>')
        a("</tbody></table></div>")

    # ---- upgrades and news ---------------------------------------------------
    eco = report.get("sections", {}).get("ecosystem", {}) or {}
    a("<h2>Upgrades and proposals</h2>")
    for u in eco.get("upgrades", []):
        a(f'<div class=note><b>{_esc(u["id"])}</b> &mdash; {_esc(u["what"])}</div>')
    simds = (eco.get("metrics") or {}).get("simds_mentioned_recently") or []
    if simds:
        a(f'<div class=note>SIMDs referenced in the current feed window: '
          f'{" ".join("<code>" + _esc(s) + "</code>" for s in simds)}</div>')

    news = eco.get("news") or []
    if news:
        a("<h2>Ecosystem news</h2><ul class=news>")
        for n in news[:20]:
            link = n.get("link") or ""
            title = _esc(n.get("title", ""))
            a("<li>" + (f'<a href="{_esc(link)}" rel="noopener noreferrer" target=_blank>{title}</a>'
                        if link else title) +
              f'<div class=src>{_esc(n.get("published", ""))}</div></li>')
        a("</ul>")

    # ---- transparency --------------------------------------------------------
    missing = report.get("not_collected") or []
    failed = [p for p in col.get("probes", []) if p.get("status") != "ok"]
    if missing or failed:
        a("<h2>Not collected</h2>")
        a('<div class=note>Named gaps, not silent ones. No value in this dashboard is a '
          'guess standing in for a missing measurement.</div>')
        for x in missing:
            a(f'<div class=anom><b>{_esc(x["metric"])}</b><br>{_esc(x["reason"])}</div>')
        for p in failed:
            a(f'<div class="anom warning"><b>{_esc(p.get("section"))}/{_esc(p.get("probe"))}</b>'
              f'<br>probe failed: {_esc(p.get("error", "unknown"))}</div>')

    a("<h2>Probe log</h2>")
    a('<div class=tw><table class=sortable><thead><tr><th>Section</th><th>Probe</th><th>Status</th>'
      "<th>Source</th><th>Latency</th></tr></thead><tbody>")
    for p in col.get("probes", []):
        ok = p.get("status") == "ok"
        a(f'<tr><td>{_esc(p.get("section"))}</td><td><code>{_esc(p.get("probe"))}</code></td>'
          f'<td><span class="tag {"ok" if ok else "critical"}">{_esc(p.get("status"))}</span></td>'
          f'<td><code>{_esc(p.get("source", ""))[:46]}</code></td>'
          f'<td class=num data-sort="{p.get("latency_ms", 0)}">{p.get("latency_ms", 0)} ms</td></tr>')
    a("</tbody></table></div>")

    a("<footer>Produced by <b>solstate</b>. Every figure comes from a public endpoint that "
      "needs no API key; the probe log above names the source and latency for each one. "
      "Machine-readable equivalent: <code>report.json</code>. "
      f"Schema {_esc(report.get('schema_version'))}.</footer>")
    a(f"</div><script>{JS}</script></body></html>")
    return "\n".join(out)
