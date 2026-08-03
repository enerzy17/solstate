"""Configuration for solstate.

Everything is a plain dataclass with defaults that work out of the box. There is
no config file to write before the first run, and there is no API key anywhere
in this module -- that is deliberate, see README "Zero keys, zero deps".

Override any field from the CLI (``--interval 900``) or from the environment
(``SOLSTATE_INTERVAL=900``). Environment wins over defaults, CLI wins over both.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field, asdict
from typing import Dict, List

# Public Solana JSON-RPC endpoints. None of these need a key. They are tried in
# order and rotated on failure, because the free public endpoints rate-limit
# aggressively and a single hard-coded URL is the most common reason a report
# like this quietly stops updating.
DEFAULT_RPCS: List[str] = [
    "https://api.mainnet-beta.solana.com",
    "https://solana-rpc.publicnode.com",
    "https://solana.drpc.org",
    "https://api.blockeden.xyz/solana/67nCBdZQSH9z3YqDDjdm",
]

# Thresholds for the rule-based half of anomaly detection. The statistical half
# (median absolute deviation) needs no thresholds and learns from history.
DEFAULT_THRESHOLDS: Dict[str, float] = {
    "tps_drop_pct": 40.0,          # TPS below 60% of trailing median -> anomaly
    "tps_spike_pct": 80.0,         # TPS above 180% of trailing median -> anomaly
    "slot_time_ms_max": 800.0,     # healthy mainnet slot time is ~400ms
    "delinquent_stake_pct_max": 5.0,
    "tvl_change_pct": 15.0,        # 24h TVL move
    "sol_price_change_pct": 12.0,  # 24h price move
    "mad_z": 3.5,                  # robust z-score cutoff
    # A statistical hit must ALSO be a materially large move. Without this floor,
    # a metric with a near-zero MAD (anything stable, sampled often) scores a
    # huge z on a rounding-error change and fills the panel with true-but-useless
    # findings. Found by running against mainnet, not by theory.
    "min_rel_change": 5.0,         # percent from the trailing median
}


@dataclass
class Config:
    # --- where data comes from -------------------------------------------------
    rpcs: List[str] = field(default_factory=lambda: list(DEFAULT_RPCS))
    coingecko: str = "https://api.coingecko.com/api/v3"
    defillama: str = "https://api.llama.fi"
    defillama_stables: str = "https://stablecoins.llama.fi"
    # Optional. Left empty by default; when empty the Dune source is skipped and
    # the report says so rather than pretending the data is present.
    dune_api_key: str = ""
    dune_query_ids: List[int] = field(default_factory=list)
    # RSS/Atom only. No scraping, no login, no key.
    # Each of these was checked live before being added. A feed that 404s is
    # worse than no feed, because it makes the news panel look maintained when
    # it is not.
    news_feeds: List[str] = field(default_factory=lambda: [
        "https://solana.com/news/rss.xml",
        "https://github.com/anza-xyz/agave/releases.atom",
        "https://github.com/solana-foundation/solana-improvement-documents/commits/main.atom",
    ])

    # --- behaviour -------------------------------------------------------------
    interval: int = 1800           # seconds between refreshes in --watch mode
    timeout: int = 25              # per-request timeout
    retries: int = 3               # attempts per endpoint before rotating
    validator_sample: int = 25     # how many top validators to tabulate
    history_days: int = 30         # how much history to retain in sqlite
    out_dir: str = "out"
    db_path: str = "out/history.db"
    thresholds: Dict[str, float] = field(default_factory=lambda: dict(DEFAULT_THRESHOLDS))
    user_agent: str = "solstate/1.0 (+https://github.com/; Solana ecosystem report)"

    @classmethod
    def from_env(cls) -> "Config":
        c = cls()
        for name in ("interval", "timeout", "retries", "validator_sample", "history_days"):
            raw = os.environ.get(f"SOLSTATE_{name.upper()}")
            if raw:
                try:
                    setattr(c, name, int(raw))
                except ValueError:
                    pass
        for name in ("out_dir", "db_path", "dune_api_key"):
            raw = os.environ.get(f"SOLSTATE_{name.upper()}")
            if raw:
                setattr(c, name, raw)
        raw = os.environ.get("SOLSTATE_RPCS")
        if raw:
            c.rpcs = [u.strip() for u in raw.split(",") if u.strip()]
        return c

    def to_dict(self) -> dict:
        d = asdict(self)
        d["dune_api_key"] = "set" if self.dune_api_key else ""   # never serialise a secret
        return d
