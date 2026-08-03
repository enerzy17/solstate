"""Renderers must never raise on a sparse or broken report, and history must round-trip.

A dashboard that crashes when one source is down is worse than one that shows a
gap, so the renderer tests deliberately feed in near-empty reports.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solstate.history import History                                   # noqa: E402
from solstate.net import Fetched                                       # noqa: E402
from solstate.render import html as r_html, json_out as r_json, markdown as r_md  # noqa: E402

EMPTY = {
    "schema_version": "1.0", "generated_at": 1750000000,
    "generated_at_iso": "2026-08-03T00:00:00Z", "duration_ms": 10,
    "collection": {"probes_total": 0, "probes_ok": 0, "probes_failed": 0,
                   "http_calls": 0, "completeness_pct": 0.0, "history_runs": 0, "probes": []},
    "metrics": {}, "sections": {}, "anomalies": [],
    "anomaly_summary": {"critical": 0, "warning": 0, "info": 0},
    "not_collected": [], "config": {}, "series": {},
}


def _with(**over):
    r = {k: (dict(v) if isinstance(v, dict) else list(v) if isinstance(v, list) else v)
         for k, v in EMPTY.items()}
    r.update(over)
    return r


class TestRenderers(unittest.TestCase):
    def test_all_three_survive_an_empty_report(self):
        self.assertIn("Solana", r_md.render(EMPTY))
        self.assertIn("<html", r_html.render(EMPTY))
        self.assertIn('"schema_version"', r_json.render(EMPTY))

    def test_missing_values_render_as_unavailable_not_zero(self):
        md = r_md.render(_with(metrics={"tps": None, "sol_price_usd": None}))
        self.assertIn("unavailable", md)
        self.assertNotIn("| TPS (all) | 0", md)

    def test_html_escapes_hostile_content(self):
        r = _with(sections={"ecosystem": {
            "news": [{"title": "<script>alert(1)</script>", "link": "", "published": ""}],
            "upgrades": [], "metrics": {}}})
        out = r_html.render(r)
        self.assertNotIn("<script>alert(1)</script>", out)
        self.assertIn("&lt;script&gt;", out)

    def test_html_loads_no_external_resources(self):
        """The page must render identically offline.

        Outbound *links* in the news list are fine and expected -- they are
        navigation, not resource loads. What must never appear is anything the
        browser fetches on its own: scripts, stylesheets, images, fonts, frames.
        So this asserts on the loading mechanisms, and does it against a report
        that actually contains external URLs.
        """
        r = _with(sections={"ecosystem": {
            "news": [{"title": "Upgrade shipped", "link": "https://solana.com/news/x",
                      "published": "2026-08-01"}],
            "upgrades": [], "metrics": {}}})
        out = r_html.render(r)
        self.assertIn("https://solana.com/news/x", out)      # the link survived
        for forbidden in ("src=", "<link", "@import", "<img", "<iframe", "url(http",
                          "fetch(", "XMLHttpRequest"):
            self.assertNotIn(forbidden, out,
                             f"dashboard must not load anything external ({forbidden})")

    def test_every_table_sits_in_a_horizontal_scroll_container(self):
        """Wide tables must scroll inside their own box, never the page body.

        Without this the validator table drags the whole document sideways on a
        phone. Asserted structurally because it is the property that matters and
        it is cheap to regress.
        """
        r = _with(sections={"validators": {"top": [
            {"rank": 1, "node_pubkey": "abc", "stake_sol": 1.0, "stake_pct": 1.0,
             "commission_pct": 5, "last_vote": 10}], "delinquent_sample": []}},
            collection={**EMPTY["collection"],
                        "probes": [{"section": "s", "probe": "p", "status": "ok",
                                    "source": "x", "latency_ms": 1}]})
        out = r_html.render(r)
        self.assertGreater(out.count("<table"), 0)
        self.assertEqual(out.count("<table"), out.count("<div class=tw>"),
                         "every <table> needs a .tw scroll wrapper")
        self.assertEqual(out.count("<div class=tw>"), out.count("</table></div>"))
        self.assertIn("max-width:1240px", out)      # the page itself is bounded

    def test_html_external_links_are_safe(self):
        r = _with(sections={"ecosystem": {
            "news": [{"title": "T", "link": "https://example.com/a", "published": ""}],
            "upgrades": [], "metrics": {}}})
        out = r_html.render(r)
        self.assertIn('rel="noopener noreferrer"', out)

    def test_sparkline_suppressed_without_real_history(self):
        self.assertEqual(r_html._sparkline([]), "")
        self.assertEqual(r_html._sparkline([1.0, 2.0]), "")
        self.assertIn("<svg", r_html._sparkline([1.0, 2.0, 3.0, 4.0]))

    def test_anomalies_appear_in_every_output(self):
        r = _with(anomalies=[{"metric": "tps", "severity": "critical", "kind": "rule",
                              "value": 1.0, "message": "TPS collapsed"}],
                  anomaly_summary={"critical": 1, "warning": 0, "info": 0})
        self.assertIn("TPS collapsed", r_md.render(r))
        self.assertIn("TPS collapsed", r_html.render(r))
        self.assertIn("TPS collapsed", r_json.render(r))

    def test_json_is_deterministic(self):
        self.assertEqual(r_json.render(EMPTY), r_json.render(EMPTY))


class TestHistory(unittest.TestCase):
    def test_round_trip_and_type_filtering(self):
        with tempfile.TemporaryDirectory() as d:
            h = History(os.path.join(d, "h.db"), retain_days=30)
            kept = h.record({"tps": 3000, "health": "ok", "flag": True, "ratio": 1.5}, ts=1000)
            self.assertEqual(kept, 2)               # strings and bools excluded
            h.record({"tps": 3100.0}, ts=2000)
            self.assertEqual(h.values("tps"), [3000.0, 3100.0])
            self.assertIn("tps", h.names())
            h.close()

    def test_prune_drops_old_points(self):
        import time
        with tempfile.TemporaryDirectory() as d:
            h = History(os.path.join(d, "h.db"), retain_days=1)
            h.record({"tps": 1.0}, ts=int(time.time()) - 10 * 86400)
            h.record({"tps": 2.0}, ts=int(time.time()))
            self.assertEqual(h.prune(), 1)
            self.assertEqual(h.values("tps"), [2.0])
            h.close()


class TestFetched(unittest.TestCase):
    def test_status_reflects_ok(self):
        self.assertEqual(Fetched(True, 1, "s").status, "ok")
        self.assertEqual(Fetched(False, None, "s", "boom").status, "unavailable")
        self.assertIn("error", Fetched(False, None, "s", "boom").to_dict())
        self.assertNotIn("error", Fetched(True, 1, "s").to_dict())


if __name__ == "__main__":
    unittest.main()
