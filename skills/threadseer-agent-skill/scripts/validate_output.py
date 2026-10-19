#!/usr/bin/env python3
"""Validate Threadseer Markdown or JSON output contracts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

PROFILE_HEADINGS = {
    "full": [
        "Executive Brief",
        "Decisions & Commitments",
        "Ranked Action Plan",
        "Open Questions & Gaps",
        "Risks, Misalignments & Assumptions",
        "Insights & Learnings",
        "Opportunities",
        "Institutional Memory",
    ],
    "team": ["Executive Brief", "Decisions & Commitments", "Ranked Action Plan", "Shareable Team Report"],
    "insights": [
        "Insights & Learnings",
        "Risks, Misalignments & Assumptions",
        "Open Questions & Gaps",
        "Opportunities",
    ],
    "next": ["Recommendation", "Why This", "Ranked Action Plan", "Validation Plan"],
    "memory": ["Decision Register", "Commitment Register", "Assumptions & Unknowns", "Durable Context"],
    "custom": [],
}

PROFILE_JSON_KEYS = {
    "full": {"meta", "executive_brief", "evidence", "decisions", "commitments", "actions"},
    "team": {"meta", "executive_brief", "decisions", "commitments", "actions", "shareable_report"},
    "insights": {"meta", "evidence", "risks", "insights", "opportunities"},
    "next": {"meta", "evidence", "recommendations", "actions", "validation_plan"},
    "memory": {"meta", "evidence", "decisions", "commitments", "institutional_memory"},
    "custom": {"meta"},
}

ACTION_COLUMNS = {
    "action",
    "owner",
    "priority",
    "feasibility",
    "impact",
    "effort",
    "dependencies",
    "risks",
    "next step",
    "evidence",
}

LABEL_PATTERN = re.compile(
    r"\[(Explicit|Strong inference|Tentative inference|Recommendation|Unknown|Contested)\]",
    re.IGNORECASE,
)
LOCATOR_PATTERN = re.compile(
    r"(?:\bL\d+(?:\s*[-–]\s*L?\d+)?\b|\b\d{1,2}:\d{2}(?::\d{2})?\b|\bE\d{2,}\b)",
    re.IGNORECASE,
)


def read_source(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).expanduser().read_text(encoding="utf-8")


def normalize_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().rstrip("#").strip()).casefold()


def markdown_headings(text: str) -> set[str]:
    return {
        normalize_heading(match.group(1))
        for match in re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    }


def action_table_columns(text: str) -> set[str] | None:
    lines = text.splitlines()
    in_action_section = False
    for line in lines:
        if line.startswith("## "):
            in_action_section = normalize_heading(line[3:]) == normalize_heading("Ranked Action Plan")
            continue
        if in_action_section and line.strip().startswith("|"):
            columns = [column.strip().casefold() for column in line.strip().strip("|").split("|")]
            return set(columns)
    return None


def validate_markdown(text: str, profile: str, require_sources: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    headings = markdown_headings(text)

    for required in PROFILE_HEADINGS[profile]:
        if normalize_heading(required) not in headings:
            errors.append(f"missing required heading: ## {required}")

    if "Ranked Action Plan" in PROFILE_HEADINGS[profile]:
        columns = action_table_columns(text)
        if columns is None:
            errors.append("missing Markdown table under ## Ranked Action Plan")
        else:
            missing_columns = sorted(ACTION_COLUMNS - columns)
            if missing_columns:
                errors.append(f"action table missing columns: {', '.join(missing_columns)}")

    if not LABEL_PATTERN.search(text):
        warnings.append("no epistemic labels found")
    if require_sources and not LOCATOR_PATTERN.search(text):
        errors.append("no source locator found (expected lines, timestamp, or evidence ID)")
    elif not LOCATOR_PATTERN.search(text):
        warnings.append("no source locator found")

    if re.search(r"\b(?:obviously|definitely|guaranteed)\b", text, flags=re.IGNORECASE):
        warnings.append("absolute language found; confirm that the evidence supports it")
    return errors, warnings


def validate_action(action: Any, index: int, evidence_ids: set[str], errors: list[str]) -> None:
    if not isinstance(action, dict):
        errors.append(f"actions[{index}] must be an object")
        return
    required = {
        "action",
        "owner",
        "priority",
        "feasibility",
        "impact",
        "effort",
        "dependencies",
        "risks",
        "next_step",
        "evidence_ids",
    }
    missing = sorted(required - action.keys())
    if missing:
        errors.append(f"actions[{index}] missing keys: {', '.join(missing)}")
    for field in ("action", "owner", "next_step"):
        require_text(action.get(field), f"actions[{index}].{field}", errors)
    for field in ("dependencies", "risks"):
        require_text_array(action.get(field), f"actions[{index}].{field}", errors)
    allowed = {
        "priority": {"P0", "P1", "P2"},
        "feasibility": {"Easy", "Medium", "Hard"},
        "impact": {"Low", "Medium", "High"},
        "effort": {"S", "M", "L"},
    }
    for field, values in allowed.items():
        if field in action and (not isinstance(action[field], str) or action[field] not in values):
            errors.append(f"actions[{index}].{field} must be one of: {', '.join(sorted(values))}")
    references = action.get("evidence_ids", [])
    if not isinstance(references, list) or not all(isinstance(ref, str) and ref for ref in references):
        errors.append(f"actions[{index}].evidence_ids must be an array of non-empty strings")
    else:
        missing_references = sorted(set(references) - evidence_ids)
        if missing_references:
            errors.append(f"actions[{index}] references unknown evidence IDs: {', '.join(missing_references)}")


def require_text(value: Any, field: str, errors: list[str], allow_empty: bool = False) -> None:
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        errors.append(f"{field} must be a {'string' if allow_empty else 'non-empty string'}")


def require_text_array(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"{field} must be an array of non-empty strings")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError("non-finite JSON value")


def validate_json(text: str, profile: str, require_sources: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        payload = json.loads(text, object_pairs_hook=unique_object, parse_constant=reject_constant)
    except ValueError as exc:
        return [f"invalid JSON: {exc}"], warnings
    if not isinstance(payload, dict):
        return ["top-level JSON value must be an object"], warnings

    missing = sorted(PROFILE_JSON_KEYS[profile] - payload.keys())
    if missing:
        errors.append(f"missing top-level keys: {', '.join(missing)}")

    array_fields = {"decisions", "commitments", "open_questions", "validation_plan", "risks", "insights", "opportunities", "nonlinear_potential", "institutional_memory"}
    for field in sorted(array_fields):
        if field in payload and not isinstance(payload[field], list):
            errors.append(f"{field} must be an array")
    for field in ("executive_brief", "shareable_report", "follow_up_draft"):
        if field in payload:
            require_text(payload[field], field, errors, allow_empty=True)

    meta = payload.get("meta")
    if not isinstance(meta, dict):
        errors.append("meta must be an object")
    else:
        for field in ("profile", "purpose", "audience"):
            if field in meta:
                require_text(meta[field], f"meta.{field}", errors)
        if "limitations" in meta:
            require_text_array(meta["limitations"], "meta.limitations", errors)
        if "source_hash" in meta and meta["source_hash"] is not None:
            require_text(meta["source_hash"], "meta.source_hash", errors)
        if meta.get("profile") != profile and profile != "custom":
            warnings.append("meta.profile does not match the selected profile")

    evidence = payload.get("evidence", [])
    evidence_ids: set[str] = set()
    if not isinstance(evidence, list):
        errors.append("evidence must be an array")
    elif require_sources and not evidence:
        errors.append("evidence must not be empty when --require-sources is used")
    else:
        for index, item in enumerate(evidence):
            if not isinstance(item, dict):
                errors.append(f"evidence[{index}] must be an object")
                continue
            required = {"id", "type", "claim", "speaker", "locator", "status", "sensitivity"}
            item_missing = sorted(required - item.keys())
            if item_missing:
                errors.append(f"evidence[{index}] missing keys: {', '.join(item_missing)}")
            for field in ("claim", "speaker", "locator"):
                require_text(item.get(field), f"evidence[{index}].{field}", errors,
                             allow_empty=field == "locator" and not require_sources)
            if "conditions" in item:
                require_text_array(item["conditions"], f"evidence[{index}].conditions", errors)
            item_id = item.get("id")
            if isinstance(item_id, str) and item_id.strip():
                if item_id in evidence_ids:
                    errors.append(f"duplicate evidence ID: {item_id}")
                evidence_ids.add(item_id)
            else:
                errors.append(f"evidence[{index}].id must be a non-empty string")
            allowed_values = {
                "type": {"fact", "proposal", "decision", "commitment", "concern", "hypothesis", "disagreement", "unknown"},
                "status": {"explicit", "strong_inference", "tentative_inference", "contested", "unknown"},
                "sensitivity": {"private", "internal", "shareable", "unknown"},
            }
            for field, values in allowed_values.items():
                if field in item and (not isinstance(item[field], str) or item[field] not in values):
                    errors.append(
                        f"evidence[{index}].{field} must be one of: {', '.join(sorted(values))}"
                    )

    actions = payload.get("actions", [])
    if not isinstance(actions, list):
        errors.append("actions must be an array")
    else:
        for index, action in enumerate(actions):
            validate_action(action, index, evidence_ids, errors)

    recommendations = payload.get("recommendations", [])
    if not isinstance(recommendations, list):
        errors.append("recommendations must be an array")
    else:
        required = {
            "recommendation",
            "status",
            "rationale",
            "evidence_ids",
            "strongest_alternative",
            "change_conditions",
        }
        for index, recommendation in enumerate(recommendations):
            if not isinstance(recommendation, dict):
                errors.append(f"recommendations[{index}] must be an object")
                continue
            missing_fields = sorted(required - recommendation.keys())
            if missing_fields:
                errors.append(f"recommendations[{index}] missing keys: {', '.join(missing_fields)}")
            for field in ("recommendation", "rationale", "strongest_alternative"):
                require_text(recommendation.get(field), f"recommendations[{index}].{field}", errors)
            require_text_array(recommendation.get("change_conditions"), f"recommendations[{index}].change_conditions", errors)
            if recommendation.get("status") != "recommendation":
                errors.append(f"recommendations[{index}].status must be 'recommendation'")
            references = recommendation.get("evidence_ids", [])
            if not isinstance(references, list) or not all(isinstance(ref, str) and ref for ref in references):
                errors.append(f"recommendations[{index}].evidence_ids must be an array of non-empty strings")
            else:
                missing_references = sorted(set(references) - evidence_ids)
                if missing_references:
                    errors.append(
                        f"recommendations[{index}] references unknown evidence IDs: {', '.join(missing_references)}"
                    )
    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default="-", help="Output file or - for stdin")
    parser.add_argument("--profile", choices=tuple(PROFILE_HEADINGS), default="full")
    parser.add_argument("--format", choices=("auto", "markdown", "json"), default="auto")
    parser.add_argument("--require-sources", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        text = read_source(args.source)
    except (OSError, UnicodeError) as exc:
        print(f"error: unable to read source: {exc}", file=sys.stderr)
        return 2

    output_format = args.format
    if output_format == "auto":
        output_format = "json" if args.source != "-" and Path(args.source).suffix.casefold() == ".json" else "markdown"

    if output_format == "json":
        errors, warnings = validate_json(text, args.profile, args.require_sources)
    else:
        errors, warnings = validate_markdown(text, args.profile, args.require_sources)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
