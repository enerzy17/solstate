"""Renderers. Each is a pure function of the report dict built by solstate.report."""
from . import html, json_out, markdown       # noqa: F401

__all__ = ["html", "json_out", "markdown"]
