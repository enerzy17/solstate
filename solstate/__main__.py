"""Command line entry point:  python -m solstate

    python -m solstate                    one run, writes out/{report.json,report.md,index.html}
    python -m solstate --watch            keep running every --interval seconds
    python -m solstate --interval 900     refresh every 15 minutes
    python -m solstate --serve 8080       run, then serve out/ over HTTP

No arguments are required. There is nothing to configure before the first run.
"""
from __future__ import annotations

import argparse
import os
import sys
import time

from .config import Config
from .history import History
from .report import build
from .render import html as r_html, json_out as r_json, markdown as r_md


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="solstate",
        description="Auto-updating report and dashboard on the state of the Solana ecosystem. "
                    "Standard library only, no API keys.")
    p.add_argument("--out", default=None, help="output directory (default: out)")
    p.add_argument("--interval", type=int, default=None,
                   help="seconds between refreshes in --watch mode (default 1800)")
    p.add_argument("--watch", action="store_true", help="refresh forever on --interval")
    p.add_argument("--once", action="store_true", help="single run (the default)")
    p.add_argument("--serve", type=int, metavar="PORT", default=None,
                   help="after the run, serve the output directory on PORT")
    p.add_argument("--rpc", action="append", default=None, metavar="URL",
                   help="override Solana RPC endpoint; repeatable")
    p.add_argument("--dune-key", default=None, help="optional Dune API key")
    p.add_argument("--dune-query", action="append", type=int, default=None,
                   help="Dune query id to pull; repeatable")
    p.add_argument("--validators", type=int, default=None,
                   help="how many top validators to tabulate (default 25)")
    p.add_argument("--no-history", action="store_true",
                   help="skip the sqlite store (disables statistical anomaly detection)")
    p.add_argument("--compact-json", action="store_true", help="minify report.json")
    p.add_argument("--quiet", action="store_true", help="only print errors")
    return p.parse_args(argv)


def make_config(args: argparse.Namespace) -> Config:
    cfg = Config.from_env()
    if args.out:
        cfg.out_dir = args.out
        cfg.db_path = os.path.join(args.out, "history.db")
    if args.interval:
        cfg.interval = args.interval
    if args.rpc:
        cfg.rpcs = args.rpc
    if args.dune_key:
        cfg.dune_api_key = args.dune_key
    if args.dune_query:
        cfg.dune_query_ids = args.dune_query
    if args.validators:
        cfg.validator_sample = args.validators
    if not cfg.dune_api_key:
        cfg.dune_api_key = os.environ.get("SOLSTATE_DUNE_API_KEY", "")
    return cfg


def run_once(cfg: Config, args: argparse.Namespace) -> dict:
    os.makedirs(cfg.out_dir, exist_ok=True)
    history = None if args.no_history else History(cfg.db_path, cfg.history_days)
    try:
        report = build(cfg, history)
    finally:
        if history is not None:
            history.close()

    writes = {
        "report.json": r_json.render(report, args.compact_json),
        "report.md": r_md.render(report),
        "index.html": r_html.render(report),
    }
    for name, text in writes.items():
        path = os.path.join(cfg.out_dir, name)
        # Write to a temp file then replace, so a reader (or GitHub Pages) never
        # sees a half-written dashboard.
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        os.replace(tmp, path)

    if not args.quiet:
        c = report["collection"]
        s = report["anomaly_summary"]
        print(f"[solstate] {report['generated_at_iso']}  "
              f"{c['probes_ok']}/{c['probes_total']} probes ok ({c['completeness_pct']}%)  "
              f"{c['http_calls']} calls  {report['duration_ms'] / 1000:.1f}s  "
              f"anomalies: {s['critical']}C/{s['warning']}W/{s['info']}I")
        for name in writes:
            print(f"           wrote {os.path.join(cfg.out_dir, name)}")
        for an in report["anomalies"][:5]:
            print(f"           ! {an['severity']:8} {an['metric']}: {an['message']}")
    return report


def serve(directory: str, port: int) -> None:
    import functools
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
    handler = functools.partial(SimpleHTTPRequestHandler, directory=directory)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
    print(f"[solstate] serving {directory} at http://127.0.0.1:{port}/  (ctrl-c to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[solstate] stopped")


def main(argv=None) -> int:
    args = parse_args(argv)
    cfg = make_config(args)

    try:
        run_once(cfg, args)
    except KeyboardInterrupt:
        return 130

    if args.watch:
        print(f"[solstate] watching, refresh every {cfg.interval}s. Ctrl-C to stop.")
        try:
            while True:
                time.sleep(cfg.interval)
                try:
                    run_once(cfg, args)
                except Exception as e:                      # noqa: BLE001
                    # A refresh failing must never kill the loop; the next one
                    # may well succeed, and the dashboard keeps the last good copy.
                    print(f"[solstate] refresh failed: {type(e).__name__}: {e}", file=sys.stderr)
        except KeyboardInterrupt:
            print("\n[solstate] stopped")
            return 0

    if args.serve:
        serve(cfg.out_dir, args.serve)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
