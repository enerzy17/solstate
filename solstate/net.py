"""HTTP plumbing built on urllib, so the whole project stays pip-install-free.

Two things here matter more than they look:

1. **Endpoint rotation.** Public Solana RPCs rate-limit hard. A report that
   pins one URL works on the author's laptop and silently dies a week later.
   :func:`JsonClient.rpc` walks the configured endpoint list.

2. **Failures are values, not exceptions.** Every fetch returns a
   :class:`Fetched` that carries ``ok``, ``error`` and ``source``. Nothing in
   this project is allowed to substitute a plausible number for a missing one;
   a source that is down is rendered as "unavailable" in all three outputs.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse


@dataclass
class Fetched:
    """The result of one attempt to get data from one place."""
    ok: bool
    value: Any = None
    source: str = ""
    error: str = ""
    latency_ms: int = 0
    fetched_at: float = field(default_factory=time.time)

    @property
    def status(self) -> str:
        return "ok" if self.ok else "unavailable"

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "source": self.source,
            "fetched_at": int(self.fetched_at),
            "latency_ms": self.latency_ms,
            **({"error": self.error} if self.error else {}),
        }


class JsonClient:
    def __init__(self, timeout: int = 25, retries: int = 3, user_agent: str = "solstate/1.0"):
        self.timeout = timeout
        self.retries = retries
        self.user_agent = user_agent
        self.calls = 0

    # -- low level ---------------------------------------------------------------
    def _once(self, url: str, payload: Optional[dict], headers: Optional[Dict[str, str]]) -> Any:
        body = json.dumps(payload).encode() if payload is not None else None
        h = {"accept": "application/json", "user-agent": self.user_agent}
        if body is not None:
            h["content-type"] = "application/json"
        if headers:
            h.update(headers)
        req = urllib.request.Request(url, data=body, headers=h)
        self.calls += 1
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            raw = resp.read()
        if not raw:
            return None
        return json.loads(raw.decode("utf-8", "replace"))

    def get(self, url: str, source: str = "", headers: Optional[Dict[str, str]] = None) -> Fetched:
        """GET one URL, with retries and exponential backoff."""
        source = source or url
        last = ""
        t0 = time.time()
        for attempt in range(self.retries):
            try:
                val = self._once(url, None, headers)
                return Fetched(True, val, source, "", int((time.time() - t0) * 1000))
            except urllib.error.HTTPError as e:
                last = f"HTTP {e.code}"
                # 4xx other than 429 will not fix themselves; stop early.
                if e.code != 429 and 400 <= e.code < 500:
                    break
            except Exception as e:                      # noqa: BLE001 - report, never raise
                last = f"{type(e).__name__}: {e}"
            time.sleep(min(2 ** attempt, 8))
        return Fetched(False, None, source, last, int((time.time() - t0) * 1000))

    def get_bytes(self, url: str, source: str = "") -> Fetched:
        """GET a URL as raw bytes, with no JSON parsing.

        Feeds are XML. Routing them through :meth:`get` would make every feed
        look like a network failure when it is really a content-type mismatch,
        which is a much more misleading thing to put in a probe log.
        """
        source = source or url
        last = ""
        t0 = time.time()
        for attempt in range(self.retries):
            try:
                req = urllib.request.Request(
                    url, headers={"user-agent": self.user_agent,
                                  "accept": "application/rss+xml, application/atom+xml, "
                                            "application/xml, text/xml, */*"})
                self.calls += 1
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    raw = resp.read()
                return Fetched(True, raw, source, "", int((time.time() - t0) * 1000))
            except urllib.error.HTTPError as e:
                last = f"HTTP {e.code}"
                if e.code != 429 and 400 <= e.code < 500:
                    break
            except Exception as e:                      # noqa: BLE001
                last = f"{type(e).__name__}: {e}"
            time.sleep(min(2 ** attempt, 8))
        return Fetched(False, None, source, last, int((time.time() - t0) * 1000))

    def rpc(self, endpoints: List[str], method: str, params: Optional[list] = None) -> Fetched:
        """Call a Solana JSON-RPC method, rotating across endpoints on failure."""
        payload = {"jsonrpc": "2.0", "id": 1, "method": method}
        if params is not None:
            payload["params"] = params
        last = "no endpoints configured"
        t0 = time.time()
        for url in endpoints:
            for attempt in range(self.retries):
                try:
                    doc = self._once(url, payload, None)
                    if isinstance(doc, dict) and "error" in doc:
                        last = f"rpc error {doc['error'].get('code')}: {doc['error'].get('message')}"
                        break                            # a bad method will fail everywhere
                    return Fetched(True, (doc or {}).get("result"), f"{method}@{_host(url)}",
                                   "", int((time.time() - t0) * 1000))
                except urllib.error.HTTPError as e:
                    last = f"HTTP {e.code}"
                    if e.code in (429, 503):
                        time.sleep(min(2 ** attempt, 8))
                        continue
                    break                                # rotate to the next endpoint
                except Exception as e:                   # noqa: BLE001
                    last = f"{type(e).__name__}: {e}"
                    time.sleep(min(2 ** attempt, 4))
        return Fetched(False, None, f"{method}@none", last, int((time.time() - t0) * 1000))


def _host(url: str) -> str:
    return urlparse(url).hostname or url
