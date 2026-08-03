"""Economic indicators from public, unauthenticated endpoints.

CoinGecko free tier and DeFiLlama both serve these without a key. Where a
metric genuinely is not available without a paid source (daily active
addresses, tokenized-equity volume broken out by issuer), this module records
it as ``unavailable`` with a reason instead of inventing a proxy.
"""
from __future__ import annotations

from typing import Any, Dict, List

from ..config import Config
from ..net import JsonClient


def _num(x, nd=2):
    try:
        return round(float(x), nd)
    except (TypeError, ValueError):
        return None


def collect_market(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    """SOL price and market data."""
    out: Dict[str, Any] = {"metrics": {}, "meta": {}}
    url = (f"{cfg.coingecko}/coins/solana?localization=false&tickers=false"
           f"&community_data=false&developer_data=false&sparkline=false")
    f = client.get(url, "coingecko:/coins/solana")
    out["meta"]["price"] = f.to_dict()
    if f.ok and isinstance(f.value, dict):
        md = (f.value.get("market_data") or {})

        def usd(key):
            return _num((md.get(key) or {}).get("usd"))

        out["metrics"] = {
            "sol_price_usd": usd("current_price"),
            "sol_market_cap_usd": usd("market_cap"),
            "sol_volume_24h_usd": usd("total_volume"),
            "sol_change_24h_pct": _num(md.get("price_change_percentage_24h")),
            "sol_change_7d_pct": _num(md.get("price_change_percentage_7d")),
            "sol_change_30d_pct": _num(md.get("price_change_percentage_30d")),
            "sol_ath_usd": usd("ath"),
            "sol_ath_change_pct": _num((md.get("ath_change_percentage") or {}).get("usd")),
            "sol_fdv_usd": usd("fully_diluted_valuation"),
        }
    return out


def collect_defi(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    """TVL, stablecoin supply, DEX volume and chain fees/REV."""
    out: Dict[str, Any] = {"metrics": {}, "meta": {}, "series": {}}

    # --- TVL, plus 30d of history so the dashboard can draw a real sparkline ---
    f = client.get(f"{cfg.defillama}/v2/historicalChainTvl/Solana", "defillama:historicalChainTvl")
    out["meta"]["tvl"] = f.to_dict()
    if f.ok and isinstance(f.value, list) and f.value:
        pts = f.value[-90:]
        out["series"]["tvl_usd"] = [{"date": p.get("date"), "value": _num(p.get("tvl"), 0)}
                                    for p in pts]
        latest = _num(f.value[-1].get("tvl"), 0)
        out["metrics"]["tvl_usd"] = latest
        for label, back in (("24h", 1), ("7d", 7), ("30d", 30)):
            if len(f.value) > back and latest:
                prev = _num(f.value[-1 - back].get("tvl"), 0)
                if prev:
                    out["metrics"][f"tvl_change_{label}_pct"] = _num((latest - prev) / prev * 100)

    # --- stablecoins on Solana -------------------------------------------------
    f = client.get(f"{cfg.defillama_stables}/stablecoinchains", "defillama:stablecoinchains")
    out["meta"]["stablecoins"] = f.to_dict()
    if f.ok and isinstance(f.value, list):
        for row in f.value:
            if (row.get("name") or "").lower() == "solana":
                tc = row.get("totalCirculatingUSD") or {}
                out["metrics"]["stablecoin_supply_usd"] = _num(sum(
                    v for v in tc.values() if isinstance(v, (int, float))), 0)
                out["metrics"]["stablecoin_breakdown"] = {k: _num(v, 0) for k, v in tc.items()}
                break

    # --- DEX volume ------------------------------------------------------------
    f = client.get(
        f"{cfg.defillama}/overview/dexs/solana"
        f"?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true",
        "defillama:overview/dexs/solana")
    out["meta"]["dex"] = f.to_dict()
    if f.ok and isinstance(f.value, dict):
        v = f.value
        out["metrics"].update({
            "dex_volume_24h_usd": _num(v.get("total24h"), 0),
            "dex_volume_7d_usd": _num(v.get("total7d"), 0),
            "dex_volume_change_24h_pct": _num(v.get("change_1d")),
            "dex_protocols_tracked": len(v.get("protocols") or []),
        })

    # --- fees / REV ------------------------------------------------------------
    # "Real Economic Value" has no single canonical definition. DeFiLlama's
    # chain fees series is the closest key-free public proxy, and it is labelled
    # as a proxy in every render so nobody reads it as an official REV figure.
    f = client.get(
        f"{cfg.defillama}/overview/fees/solana"
        f"?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true",
        "defillama:overview/fees/solana")
    out["meta"]["fees"] = f.to_dict()
    if f.ok and isinstance(f.value, dict):
        v = f.value
        out["metrics"].update({
            "chain_fees_24h_usd": _num(v.get("total24h"), 0),
            "chain_fees_7d_usd": _num(v.get("total7d"), 0),
            "chain_revenue_24h_usd": _num(v.get("dailyRevenue"), 0),
            "rev_proxy_24h_usd": _num(v.get("total24h"), 0),
            "rev_proxy_basis": "DeFiLlama chain fees (24h). Proxy, not an official REV series.",
        })

    return out


# Metrics the bounty brief asks for that genuinely need a keyed or paid source.
# Declaring them explicitly is the honest alternative to quietly omitting them.
UNAVAILABLE_WITHOUT_KEY: List[Dict[str, str]] = [
    {"metric": "daily_active_addresses",
     "reason": "No key-free public endpoint. Available via Dune; enable with --dune-key."},
    {"metric": "tokenized_equity_volume",
     "reason": "Issuer-level breakdown (xStocks et al.) needs Dune or a vendor API."},
    {"metric": "mev_tips",
     "reason": "Jito tip data needs the Jito API; excluded to keep the run key-free."},
]
