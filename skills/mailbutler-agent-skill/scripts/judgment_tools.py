#!/usr/bin/env python3
"""Validate Mailbutler judgments and print the owner-facing lede."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ACTIONS = {"reply", "seeAndReply", "see", "nothing"}
REPLY_ACTIONS = {"reply", "seeAndReply"}
REQUIRED = {"surface", "score", "reasons", "recommendedAction", "needMoreContext"}


def validate_judgment(value: Any, index: int) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"judgment {index}: expected an object")
    if set(value) != REQUIRED:
        missing = sorted(REQUIRED - set(value))
        extra = sorted(set(value) - REQUIRED)
        raise ValueError(f"judgment {index}: missing={missing}, extra={extra}")
    if type(value["surface"]) is not bool:
        raise ValueError(f"judgment {index}: surface must be boolean")
    if type(value["needMoreContext"]) is not bool:
        raise ValueError(f"judgment {index}: needMoreContext must be boolean")
    if type(value["score"]) is not int or not 0 <= value["score"] <= 100:
        raise ValueError(f"judgment {index}: score must be an integer from 0 to 100")
    if value["recommendedAction"] not in ACTIONS:
        raise ValueError(f"judgment {index}: invalid recommendedAction")
    reasons = value["reasons"]
    if not isinstance(reasons, list) or not 1 <= len(reasons) <= 3:
        raise ValueError(f"judgment {index}: reasons must contain 1 to 3 strings")
    if any(not isinstance(reason, str) or not reason.strip() for reason in reasons):
        raise ValueError(f"judgment {index}: reasons must be non-empty strings")
    if not value["surface"] and value["recommendedAction"] != "nothing":
        raise ValueError(f"judgment {index}: suppressed mail must recommend nothing")
    return value


def plural(count: int, singular: str, plural_form: str | None = None) -> str:
    return f"{count} {singular if count == 1 else (plural_form or singular + 's')}"


def lede(judgments: list[dict[str, Any]]) -> str:
    surfaced = [item for item in judgments if item["surface"]]
    replies = [item for item in surfaced if item["recommendedAction"] in REPLY_ACTIONS]
    quiet = len(judgments) - len(surfaced)
    quiet_phrase = f"{quiet} handled quietly"
    if not surfaced:
        return f"Nothing needs you right now — {quiet_phrase}."
    surfaced_phrase = plural(len(surfaced), "email") + " worth your time"
    if not replies:
        return f"{surfaced_phrase} — {quiet_phrase}."
    reply_phrase = plural(len(replies), "suggested reply")
    return f"{surfaced_phrase}, {reply_phrase} — {quiet_phrase}."


def load(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("top level must be a list of judgments")
    return [validate_judgment(value, index) for index, value in enumerate(payload, start=1)]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: judgment_tools.py <judgments.json>", file=sys.stderr)
        return 2
    try:
        judgments = load(Path(argv[1]))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"invalid judgments: {exc}", file=sys.stderr)
        return 1
    print(lede(judgments))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
