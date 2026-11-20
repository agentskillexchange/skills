#!/usr/bin/env python3
"""Build a deterministic local voice-evidence context pack."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


TOKEN_RE = re.compile(r"[a-z0-9']+")
SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
LOCAL_OUTPUT_RE = re.compile(
    r"^voice-context(?:\.[a-z0-9][a-z0-9_-]*)?\.local\.md$"
)
ROOT_KEYS = {"version", "subject", "sources"}
SUBJECT_KEYS = {"label", "consent_confirmed", "consent_scope", "final_ratifier"}
SOURCE_KEYS = {"id", "path", "authorship", "sha256", "registers"}


class ManifestError(ValueError):
    """Raised when consent or provenance validation fails."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ManifestError(f"Could not read manifest: {exc}") from exc
    validate_manifest(data)
    return data


def validate_manifest(data: dict[str, Any]) -> None:
    if not isinstance(data, dict) or data.get("version") != 1:
        raise ManifestError("Manifest version must be 1")
    if set(data) != ROOT_KEYS:
        raise ManifestError("Manifest contains missing or unsupported top-level fields")

    subject = data.get("subject")
    if not isinstance(subject, dict):
        raise ManifestError("Manifest must include a subject object")
    if set(subject) != SUBJECT_KEYS:
        raise ManifestError("Subject contains missing or unsupported fields")
    if subject.get("consent_confirmed") is not True:
        raise ManifestError("Subject consent must be explicitly confirmed")
    if subject.get("final_ratifier") != "subject":
        raise ManifestError("The subject must be the final ratifier")
    for key in ("label", "consent_scope"):
        if not isinstance(subject.get(key), str) or not subject[key].strip():
            raise ManifestError(f"subject.{key} must be a non-empty string")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ManifestError("Manifest must include at least one source")

    seen_ids: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            raise ManifestError(f"Source {index} must be an object")
        if set(source) != SOURCE_KEYS:
            raise ManifestError(f"Source {index} contains missing or unsupported fields")
        source_id = source.get("id")
        if not isinstance(source_id, str) or not SOURCE_ID_RE.fullmatch(source_id):
            raise ManifestError(f"Source {index} has an invalid id")
        if source_id in seen_ids:
            raise ManifestError(f"Duplicate source id: {source_id}")
        seen_ids.add(source_id)
        if source.get("authorship") != "subject":
            raise ManifestError(f"Source {source_id} is not subject-authored")
        if not isinstance(source.get("path"), str) or not source["path"].strip():
            raise ManifestError(f"Source {source_id} has no path")
        if not isinstance(source.get("sha256"), str) or not SHA256_RE.fullmatch(source["sha256"]):
            raise ManifestError(f"Source {source_id} needs a lowercase SHA-256 digest")
        registers = source.get("registers")
        if (
            not isinstance(registers, list)
            or not registers
            or any(not isinstance(item, str) or not item.strip() for item in registers)
            or len(registers) != len(set(registers))
        ):
            raise ManifestError(f"Source {source_id} needs one or more registers")


def _tokens(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def _paragraphs(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", part).strip() for part in re.split(r"\n\s*\n", text) if part.strip()]


def build_context(
    manifest_path: Path,
    *,
    task: str,
    audience: str,
    register: str,
    max_chars: int,
) -> str:
    if max_chars < 1000:
        raise ManifestError("max_chars must be at least 1000")
    manifest = load_manifest(manifest_path)
    base = manifest_path.resolve().parent
    query_tokens = _tokens(f"{task} {audience} {register}")
    ranked: list[tuple[int, str, int, str, str]] = []

    for source in manifest["sources"]:
        source_path = (base / source["path"]).resolve()
        if not source_path.is_file():
            raise ManifestError(f"Source {source['id']} does not exist")
        actual_digest = sha256_file(source_path)
        if actual_digest != source["sha256"]:
            raise ManifestError(f"Source {source['id']} hash does not match the manifest")

        registers = set(source["registers"])
        register_bonus = 4 if register in registers else 1 if "general" in registers else 0
        if register_bonus == 0:
            continue
        text = source_path.read_text(encoding="utf-8")
        for paragraph_index, paragraph in enumerate(_paragraphs(text), start=1):
            overlap = len(query_tokens & _tokens(paragraph))
            ranked.append((overlap + register_bonus, source["id"], paragraph_index, actual_digest, paragraph))

    if not ranked:
        raise ManifestError(f"No source matches register: {register}")

    ranked.sort(key=lambda item: (-item[0], item[1], item[2]))
    lines = [
        "# LOCAL VOICE EVIDENCE — NOT PUBLISHABLE PROSE",
        "",
        "> DRAFT INPUT ONLY. The subject must ratify the exact final artefact.",
        "",
        f"- Subject label: {manifest['subject']['label']}",
        f"- Consent scope: {manifest['subject']['consent_scope']}",
        f"- Task: {task}",
        f"- Audience: {audience}",
        f"- Register: {register}",
        "",
        "## Ranked subject-authored excerpts",
        "",
    ]
    used: set[str] = set()
    for score, source_id, paragraph_index, digest, paragraph in ranked:
        normalized = paragraph.casefold()
        if normalized in used:
            continue
        block = [
            f"### {source_id} · paragraph {paragraph_index} · relevance {score}",
            f"SHA-256: `{digest}`",
            "",
            paragraph,
            "",
        ]
        candidate = "\n".join(lines + block).rstrip() + "\n"
        if len(candidate) > max_chars:
            continue
        lines.extend(block)
        used.add(normalized)

    if not used:
        raise ManifestError("max_chars is too small for any excerpt")
    return "\n".join(lines).rstrip() + "\n"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hash", type=Path, help="Print the SHA-256 of one local source and exit")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--task")
    parser.add_argument("--audience")
    parser.add_argument("--register", default="general")
    parser.add_argument("--max-chars", type=int, default=12000)
    parser.add_argument("--output", type=Path)
    return parser


def safe_local_output_name(path: Path) -> bool:
    """Return whether the basename is covered by the shipped Git ignore rules."""
    return LOCAL_OUTPUT_RE.fullmatch(path.name) is not None


def main() -> int:
    args = _parser().parse_args()
    if args.hash:
        if any((args.manifest, args.task, args.audience, args.output)):
            raise SystemExit("--hash cannot be combined with context-building arguments")
        print(sha256_file(args.hash.resolve()))
        return 0
    missing = [name for name in ("manifest", "task", "audience", "output") if getattr(args, name) is None]
    if missing:
        raise SystemExit(f"Missing required arguments: {', '.join('--' + item for item in missing)}")
    if not safe_local_output_name(args.output):
        raise SystemExit(
            "--output must be voice-context.local.md or "
            "voice-context.<label>.local.md so the shipped Git ignore rule applies"
        )
    try:
        context = build_context(
            args.manifest,
            task=args.task,
            audience=args.audience,
            register=args.register,
            max_chars=args.max_chars,
        )
    except ManifestError as exc:
        raise SystemExit(f"doppel: {exc}") from exc
    args.output.write_text(context, encoding="utf-8")
    print(f"Wrote local context pack: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
