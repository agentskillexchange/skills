#!/usr/bin/env python3
"""Validate a proposed Back to the Chronicle manifest."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys


CLASSES = {"WITNESSED", "ARTIFACT-MEASURED", "INFERRED INTENT"}
VERBS = {"note", "decision", "experiment", "abandoned", "correct"}
KEY = re.compile(r"^[a-z0-9][a-z0-9-]*$")
CAVEAT = "INFERRED - NOT WITNESSED - MAY BE WRONG"


def require_string(entry: dict[str, object], field: str) -> str:
    value = entry.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"entry {entry.get('key', '?')}: {field} must be a non-empty string")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest must be an object")
    if type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        raise ValueError("schema_version must be integer 1")
    if not isinstance(data.get("project"), str) or not data["project"].strip():
        raise ValueError("project must be a non-empty string")
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("entries must be a non-empty list")

    keys: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("each entry must be an object")
        key = require_string(entry, "key")
        if not KEY.fullmatch(key) or key in keys:
            raise ValueError(f"invalid or duplicate key: {key}")
        keys.add(key)
        require_string(entry, "title")
        require_string(entry, "claim")
        occurred = require_string(entry, "occurred_at")
        parsed = datetime.fromisoformat(occurred.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError(f"entry {key}: occurred_at must include a UTC offset")
        evidence_class = require_string(entry, "evidence_class")
        if evidence_class not in CLASSES:
            raise ValueError(f"entry {key}: unsupported evidence_class {evidence_class}")
        verb = require_string(entry, "chronicle_verb")
        if verb not in VERBS:
            raise ValueError(f"entry {key}: unsupported chronicle_verb {verb}")
        anchors = entry.get("anchors")
        if not isinstance(anchors, list) or not anchors or not all(
            isinstance(anchor, str) and anchor.strip() for anchor in anchors
        ):
            raise ValueError(f"entry {key}: anchors must contain non-empty strings")
        inferred = entry.get("inferred")
        if inferred is not (evidence_class == "INFERRED INTENT"):
            raise ValueError(f"entry {key}: inferred must agree with evidence_class")
        if inferred and not require_string(entry, "caveat").strip().upper().startswith(CAVEAT):
            raise ValueError(f"entry {key}: caveat must start with {CAVEAT}")
        if verb == "decision" and evidence_class != "WITNESSED":
            raise ValueError(f"entry {key}: retrospective decisions require witnessed intent")
        if verb in {"experiment", "abandoned"} and evidence_class == "INFERRED INTENT":
            raise ValueError(f"entry {key}: experiments cannot be established by inferred intent")
        if verb == "correct":
            require_string(entry, "corrects")
    print(json.dumps({"valid": True, "project": data["project"], "entries": len(entries)}))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(f"Invalid manifest ({type(exc).__name__}): {exc}", file=sys.stderr)
        raise SystemExit(1)
