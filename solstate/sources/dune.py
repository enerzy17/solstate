"""Optional Dune Analytics source.

The brief lists Dune first among data sources, and also says solutions with no
API keys are preferred. Both are satisfied by making Dune strictly additive:
with no key the report is complete and honest about what is missing; with a key
the Dune-only metrics fill in.

Uses the Dune "query results" endpoint, which returns the last cached execution
of a public query -- no execution credits are spent.
"""
from __future__ import annotations

from typing import Any, Dict

from ..config import Config
from ..net import JsonClient

BASE = "https://api.dune.com/api/v1"


def collect_dune(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    out: Dict[str, Any] = {"enabled": bool(cfg.dune_api_key), "queries": {}, "meta": {}}
    if not cfg.dune_api_key:
        out["note"] = ("No Dune key configured, so Dune-sourced metrics are omitted. "
                       "Everything else in this report is key-free. "
                       "Set SOLSTATE_DUNE_API_KEY and --dune-query to enable.")
        return out
    if not cfg.dune_query_ids:
        out["note"] = "A Dune key is set but no query ids were given (--dune-query ID)."
        return out

    headers = {"X-Dune-API-Key": cfg.dune_api_key}
    for qid in cfg.dune_query_ids:
        f = client.get(f"{BASE}/query/{qid}/results?limit=100", f"dune:query/{qid}", headers)
        out["meta"][str(qid)] = f.to_dict()
        if f.ok and isinstance(f.value, dict):
            result = (f.value.get("result") or {})
            out["queries"][str(qid)] = {
                "rows": result.get("rows", [])[:100],
                "columns": result.get("metadata", {}).get("column_names", []),
                "executed_at": f.value.get("execution_ended_at"),
            }
    return out
