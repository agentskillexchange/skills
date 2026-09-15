#!/usr/bin/env python3
"""Validate one transition event against a project collaboration policy."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

POLICY_KEYS = {
    "actors",
    "decision_classes",
    "event_id_pattern",
    "event_types",
    "states",
    "version",
}
REQUIRED_EVENT_KEYS = {
    "actor",
    "claim_or_action",
    "config_diff",
    "cost",
    "decision_class",
    "evidence_mode",
    "evidence_refs",
    "holds",
    "id",
    "next",
    "owner",
    "resource",
    "state",
    "ts",
    "type",
    "uncertainty",
    "verifier",
}
NONEMPTY_STRING_KEYS = {
    "claim_or_action",
    "evidence_mode",
    "next",
    "owner",
    "resource",
    "uncertainty",
    "verifier",
}
UTC_TIMESTAMP_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z\Z"
)


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Validate one event before journal append."
    )
    parser.add_argument(
        "--policy",
        required=True,
        help="JSON collaboration policy defining IDs and enums.",
    )
    parser.add_argument(
        "event",
        nargs="?",
        default="-",
        help="Candidate JSON event, or '-' for standard input.",
    )
    return parser.parse_args()


def _load_json(source: str) -> Any:
    """Load one JSON value from a file or standard input."""
    if source == "-":
        return json.load(sys.stdin)

    with Path(source).open(encoding="utf-8") as json_file:
        return json.load(json_file)


def _validate_enum_list(policy: dict[str, Any], key: str) -> list[str]:
    """Validate one non-empty, unique list of enum strings."""
    values = policy.get(key)
    if (
        not isinstance(values, list)
        or not values
        or not all(
            isinstance(value, str) and value.strip() for value in values
        )
    ):
        return [f"policy {key} must be a non-empty list of strings"]

    if len(values) != len(set(values)):
        return [f"policy {key} must not contain duplicates"]

    return []


def validate_policy(policy: Any) -> list[str]:
    """Return all collaboration-policy violations."""
    if not isinstance(policy, dict):
        return ["policy must be one JSON object"]

    errors = []
    actual_keys = set(policy)
    missing = POLICY_KEYS - actual_keys
    unknown = actual_keys - POLICY_KEYS

    if missing:
        errors.append(f"policy missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"policy unknown keys: {', '.join(sorted(unknown))}")
    if policy.get("version") != 1:
        errors.append("policy version must equal 1")

    for key in ("actors", "decision_classes", "event_types", "states"):
        errors.extend(_validate_enum_list(policy, key))

    pattern = policy.get("event_id_pattern")
    if not isinstance(pattern, str) or not pattern or len(pattern) > 256:
        errors.append(
            "policy event_id_pattern must be a string of 1-256 characters"
        )
    else:
        try:
            re.compile(pattern)
        except re.error as error:
            errors.append(f"policy event_id_pattern is invalid: {error}")

    return errors


def _validate_utc_timestamp(value: Any) -> str | None:
    """Return an error when a timestamp lacks a UTC date and time."""
    if not isinstance(value, str) or not UTC_TIMESTAMP_PATTERN.fullmatch(
        value
    ):
        return "ts must include an ISO-8601 date and time ending in 'Z'"

    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return "ts must be a valid ISO-8601 UTC timestamp"

    return None


def validate_event(
    event: Any,
    policy: dict[str, Any],
) -> list[str]:
    """Return all event violations under a valid policy."""
    if not isinstance(event, dict):
        return ["event must be one JSON object"]

    errors = []
    actual_keys = set(event)
    missing = REQUIRED_EVENT_KEYS - actual_keys
    unknown = actual_keys - REQUIRED_EVENT_KEYS

    if missing:
        errors.append(f"missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"unknown keys: {', '.join(sorted(unknown))}")

    event_id = event.get("id")
    id_pattern = policy.get("event_id_pattern", r"(?!x)x")
    if (
        not isinstance(event_id, str)
        or re.fullmatch(id_pattern, event_id) is None
    ):
        errors.append("id does not match policy event_id_pattern")

    timestamp_error = _validate_utc_timestamp(event.get("ts"))
    if timestamp_error:
        errors.append(timestamp_error)

    enum_fields = {
        "actor": policy.get("actors", []),
        "decision_class": policy.get("decision_classes", []),
        "state": policy.get("states", []),
        "type": policy.get("event_types", []),
    }
    for key, allowed in enum_fields.items():
        if event.get(key) not in allowed:
            errors.append(
                f"{key} must be one of: {', '.join(sorted(allowed))}"
            )

    for key in sorted(NONEMPTY_STRING_KEYS):
        value = event.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{key} must be a non-empty string")

    for key in ("config_diff", "cost"):
        value = event.get(key)
        if value is not None and not isinstance(value, str):
            errors.append(f"{key} must be a string or null")

    evidence_refs = event.get("evidence_refs")
    if (
        not isinstance(evidence_refs, list)
        or not evidence_refs
        or not all(
            isinstance(item, str) and item.strip() for item in evidence_refs
        )
    ):
        errors.append(
            "evidence_refs must be a non-empty list of non-empty strings"
        )

    holds = event.get("holds")
    if not isinstance(holds, list) or not all(
        isinstance(item, str) and item.strip() for item in holds
    ):
        errors.append("holds must be a list of non-empty strings")

    return errors


def main() -> int:
    """Validate a policy and candidate event."""
    args = _parse_args()

    try:
        policy = _load_json(args.policy)
        event = _load_json(args.event)
    except (OSError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 2

    policy_errors = validate_policy(policy)
    if policy_errors:
        for error in policy_errors:
            print(f"FAIL policy: {error}", file=sys.stderr)
        return 2

    event_errors = validate_event(event, policy)
    if event_errors:
        for error in event_errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("PASS: valid collaboration transition event")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
