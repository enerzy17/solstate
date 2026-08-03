"""Ecosystem and community signal: releases, SIMDs, news.

Feeds are parsed with ``xml.etree`` from the standard library. RSS 2.0 and Atom
have different element names for the same three things, so both shapes are
handled rather than assuming one.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List
from xml.etree import ElementTree

from ..config import Config
from ..net import JsonClient

_ATOM = "{http://www.w3.org/2005/Atom}"

# Named upgrades the brief calls out, plus the mechanism to track any SIMD.
# 'status' is derived from the live SIMD feed where possible; the static text is
# a description of what the proposal is, never a claim about whether it shipped.
TRACKED_UPGRADES: List[Dict[str, str]] = [
    {"id": "Alpenglow",
     "what": "Consensus replacement (Votor + Rotor) targeting ~150ms finality, "
             "retiring the current TowerBFT vote-by-transaction design."},
    {"id": "SIMD-0525",
     "what": "Referenced in the brief as an upcoming change; tracked live from "
             "the solana-improvement-documents repository feed."},
    {"id": "Firedancer",
     "what": "Independent validator client from Jump; matters for client "
             "diversity and therefore for liveness risk."},
]


def _text(node, *names) -> str:
    for n in names:
        el = node.find(n)
        if el is not None and (el.text or "").strip():
            return (el.text or "").strip()
        # Atom <link href="..."/> carries its value in an attribute.
        if el is not None and el.get("href"):
            return el.get("href", "")
    return ""


def _strip_html(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def collect_ecosystem(client: JsonClient, cfg: Config) -> Dict[str, Any]:
    out: Dict[str, Any] = {"meta": {}, "news": [], "upgrades": list(TRACKED_UPGRADES),
                           "metrics": {}}
    simd_hits: List[str] = []

    for url in cfg.news_feeds:
        f = client.get_bytes(url, f"feed:{url}")
        out["meta"][url] = f.to_dict()
        if not f.ok:
            continue
        try:
            root = ElementTree.fromstring(f.value)
        except ElementTree.ParseError as e:
            out["meta"][url]["status"] = "unavailable"
            out["meta"][url]["error"] = f"XML parse: {e}"
            continue

        items = root.findall(".//item") or root.findall(f".//{_ATOM}entry")
        for it in items[:12]:
            title = _text(it, "title", f"{_ATOM}title")
            link = _text(it, "link", f"{_ATOM}link")
            date = _text(it, "pubDate", f"{_ATOM}updated", f"{_ATOM}published")
            summary = _strip_html(_text(it, "description", f"{_ATOM}summary",
                                        f"{_ATOM}content"))[:280]
            if not title:
                continue
            out["news"].append({"title": _strip_html(title), "link": link,
                                "published": date, "summary": summary,
                                "feed": url})
            simd_hits += re.findall(r"SIMD[- ]?0*(\d{1,4})", f"{title} {summary}", re.I)

    out["news"].sort(key=lambda n: n.get("published", ""), reverse=True)
    out["news"] = out["news"][:30]

    seen: List[str] = []
    for n in simd_hits:
        tag = f"SIMD-{int(n):04d}"
        if tag not in seen:
            seen.append(tag)
    out["metrics"]["simds_mentioned_recently"] = seen
    out["metrics"]["news_items"] = len(out["news"])
    out["metrics"]["feeds_ok"] = sum(1 for m in out["meta"].values() if m.get("status") == "ok")
    out["metrics"]["feeds_total"] = len(cfg.news_feeds)
    return out
