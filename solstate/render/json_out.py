"""Machine-readable output.

Deliberately stable and boring: sorted keys, no trailing whitespace, UTF-8, a
``schema_version`` at the top level. Anything consuming this file should be able
to diff two runs and see only what actually changed.
"""
from __future__ import annotations

import json
from typing import Any, Dict


def render(report: Dict[str, Any], compact: bool = False) -> str:
    if compact:
        return json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
    return json.dumps(report, indent=2, sort_keys=True, default=str) + "\n"
