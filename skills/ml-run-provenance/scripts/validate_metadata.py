#!/usr/bin/env python3
"""Read-only shape/consistency validation of a version-1 provenance JSON record."""
import argparse
import datetime as dt
import json
import pathlib
import sys

TEXT_FIELDS = {"phase", "variant", "modality", "dataset", "reason", "repo_url",
               "branch", "commit", "commit_url", "code_snapshot", "config", "data"}
NULLABLE = TEXT_FIELDS | {"seed", "dirty", "created_at"}
REQUIRED = NULLABLE | {"schema_version", "run_id", "recorded_at", "metadata_origin",
                       "notes", "tags", "missing"}
STRICT = {"created_at", "phase", "variant", "modality", "dataset", "reason",
          "commit", "dirty", "seed", "config", "data"}


def _timestamp(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp needs a timezone")
    return parsed


def validate(record, strict=False):
    """Return field-only errors and warnings; never echo potentially private values."""
    errors, warnings = [], []
    if not isinstance(record, dict):
        return ["record must be an object"], warnings
    absent = REQUIRED - record.keys()
    if absent:
        errors.append("missing required keys: " + ", ".join(sorted(absent)))
    if type(record.get("schema_version")) is not int or record.get("schema_version") != 1:
        errors.append("schema_version must be integer 1")
    for key in TEXT_FIELDS | {"run_id"}:
        value = record.get(key)
        if value is None and key in NULLABLE:
            continue
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{key} must be a nonempty string" + (" or null" if key in NULLABLE else ""))
    if not isinstance(record.get("notes"), str):
        errors.append("notes must be a string")
    for key, kind in (("seed", int), ("dirty", bool)):
        if record.get(key) is not None and type(record[key]) is not kind:
            errors.append(f"{key} has invalid type")
    origin = record.get("metadata_origin")
    if origin not in ("birth", "backfill"):
        errors.append("metadata_origin must be birth or backfill")
    parsed = {}
    for key in ("created_at", "recorded_at"):
        value = record.get(key)
        if key == "created_at" and value is None:
            if origin == "birth":
                errors.append("birth requires created_at")
            continue
        try:
            parsed[key] = _timestamp(value)
        except (ValueError, TypeError, OverflowError):
            errors.append(f"{key} must be a timezone-aware ISO 8601 timestamp")
    if len(parsed) == 2 and parsed["created_at"] > parsed["recorded_at"]:
        errors.append("created_at cannot be after recorded_at")
    for key in ("tags", "missing"):
        value = record.get(key)
        if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
            errors.append(f"{key} must be an array of nonempty strings")
        elif len(value) != len(set(value)):
            errors.append(f"{key} must not contain duplicates")
    missing = record.get("missing")
    null_keys = {key for key in NULLABLE if key in record and record[key] is None}
    if isinstance(missing, list) and all(isinstance(v, str) for v in missing):
        if set(missing) != null_keys:
            errors.append("missing must list exactly the null required fields")
    if null_keys:
        warnings.append("explicit gaps: " + ", ".join(sorted(null_keys)))
    if record.get("dirty") is True and record.get("code_snapshot") is None:
        warnings.append("dirty code lacks code_snapshot identity")
        if strict:
            errors.append("strict mode requires code_snapshot for dirty code")
    if strict:
        incomplete = {key for key in STRICT if record.get(key) is None}
        if incomplete:
            errors.append("strict mode requires: " + ", ".join(sorted(incomplete)))
    return errors, warnings


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=pathlib.Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    try:
        with args.record.open(encoding="utf-8") as stream:
            record = json.load(stream, object_pairs_hook=_unique_object,
                               parse_constant=lambda _: (_ for _ in ()).throw(ValueError("nonfinite JSON")))
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"Cannot read a valid JSON record ({type(exc).__name__}).", file=sys.stderr)
        return 2
    errors, warnings = validate(record, args.strict)
    for warning in warnings:
        print("WARNING: " + warning, file=sys.stderr)
    for error in errors:
        print("ERROR: " + error, file=sys.stderr)
    if errors:
        return 1
    print("Metadata structure valid; factual provenance and tracker persistence are not verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
