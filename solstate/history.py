"""A tiny time-series store on sqlite3, which ships with Python.

Anomaly detection needs a baseline, and a baseline needs history. Rather than
adding a database or a vendor, every run appends its scalar metrics to a local
sqlite file. That file is also what makes the sparklines in the dashboard real
rather than decorative.
"""
from __future__ import annotations

import os
import sqlite3
import time
from typing import Dict, List, Optional, Tuple

SCHEMA = """
CREATE TABLE IF NOT EXISTS metrics (
    ts     INTEGER NOT NULL,
    name   TEXT    NOT NULL,
    value  REAL    NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_metrics_name_ts ON metrics(name, ts);
CREATE TABLE IF NOT EXISTS runs (
    ts        INTEGER PRIMARY KEY,
    ok        INTEGER NOT NULL,
    sources   INTEGER NOT NULL,
    failures  INTEGER NOT NULL,
    duration_ms INTEGER NOT NULL
);
"""


class History:
    def __init__(self, path: str, retain_days: int = 30):
        parent = os.path.dirname(os.path.abspath(path))
        if parent:
            os.makedirs(parent, exist_ok=True)
        self.path = path
        self.retain_days = retain_days
        self.conn = sqlite3.connect(path)
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def record(self, metrics: Dict[str, object], ts: Optional[int] = None) -> int:
        """Persist every numeric, non-boolean scalar. Returns how many were kept."""
        ts = int(ts or time.time())
        rows: List[Tuple[int, str, float]] = []
        for k, v in metrics.items():
            # bool is a subclass of int; a flag is not a time series.
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                continue
            rows.append((ts, k, float(v)))
        if rows:
            self.conn.executemany("INSERT INTO metrics(ts, name, value) VALUES (?,?,?)", rows)
            self.conn.commit()
        return len(rows)

    def record_run(self, ok: bool, sources: int, failures: int, duration_ms: int,
                   ts: Optional[int] = None) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO runs(ts, ok, sources, failures, duration_ms) VALUES (?,?,?,?,?)",
            (int(ts or time.time()), 1 if ok else 0, sources, failures, duration_ms))
        self.conn.commit()

    def series(self, name: str, limit: int = 500) -> List[Tuple[int, float]]:
        cur = self.conn.execute(
            "SELECT ts, value FROM metrics WHERE name=? ORDER BY ts DESC LIMIT ?", (name, limit))
        return list(reversed(cur.fetchall()))

    def values(self, name: str, limit: int = 500) -> List[float]:
        return [v for _, v in self.series(name, limit)]

    def names(self) -> List[str]:
        return [r[0] for r in self.conn.execute("SELECT DISTINCT name FROM metrics ORDER BY name")]

    def run_count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM runs").fetchone()[0]

    def prune(self) -> int:
        cutoff = int(time.time()) - self.retain_days * 86400
        cur = self.conn.execute("DELETE FROM metrics WHERE ts < ?", (cutoff,))
        self.conn.execute("DELETE FROM runs WHERE ts < ?", (cutoff,))
        self.conn.commit()
        return cur.rowcount

    def close(self) -> None:
        self.conn.close()
