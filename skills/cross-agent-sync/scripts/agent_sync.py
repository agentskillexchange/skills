#!/usr/bin/env python3
"""Cross-harness project context import and curated progress synchronization."""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any, Iterable, Iterator, Sequence


SCHEMA_VERSION = 1
GENERATED_START = "<!-- agent-sync:generated:start -->"
GENERATED_END = "<!-- agent-sync:generated:end -->"
NOISE_PREFIXES = (
    "<recommended_plugins>",
    "# agents.md instructions",
    "<environment_context>",
    "<task-notification>",
    "<system-reminder>",
    "<local-command-caveat>",
    "base directory for this skill:",
)
CLAUDE_NON_HUMAN_PREFIXES = (
    "<task-notification>",
    "<system-reminder>",
    "<local-command",
)


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_utc(value: dt.datetime | None = None) -> str:
    current = value or utc_now()
    return current.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_timestamp(value: Any) -> dt.datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def infer_project_root(raw: str | None) -> Path:
    start = Path(raw).expanduser().resolve() if raw else Path.cwd().resolve()
    try:
        result = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            check=True,
            text=True,
            capture_output=True,
        )
        return Path(result.stdout.strip()).resolve()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return start


def is_within(path: str | None, root: Path) -> bool:
    if not path:
        return False
    try:
        Path(path).expanduser().resolve().relative_to(root)
        return True
    except (OSError, ValueError):
        return False


def compact(text: str, limit: int = 120) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    return value if len(value) <= limit else value[: limit - 1] + "…"


def truncate(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n[…truncated…]"


def text_blocks(content: Any, allowed_types: set[str] | None = None) -> list[str]:
    if isinstance(content, str):
        return [content]
    if not isinstance(content, list):
        return []
    values: list[str] = []
    for block in content:
        if not isinstance(block, dict):
            continue
        block_type = str(block.get("type", ""))
        if allowed_types is not None and block_type not in allowed_types:
            continue
        value = block.get("text")
        if isinstance(value, str) and value.strip():
            values.append(value)
    return values


def is_noise(text: str, source: str, role: str) -> bool:
    lowered = text.lstrip().lower()
    if any(lowered.startswith(prefix) for prefix in NOISE_PREFIXES):
        return True
    if source == "claude" and role == "user":
        if any(lowered.startswith(prefix) for prefix in CLAUDE_NON_HUMAN_PREFIXES):
            return True
    return not text.strip()


def iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                try:
                    value = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(value, dict):
                    yield value
    except OSError:
        return


def message_from_record(record: dict[str, Any], source: str) -> tuple[str, str] | None:
    if source == "claude":
        record_type = record.get("type")
        if record_type not in {"user", "assistant"}:
            return None
        message = record.get("message")
        if not isinstance(message, dict):
            return None
        role = str(message.get("role") or record_type)
        if role not in {"user", "assistant"}:
            return None
        texts = text_blocks(message.get("content"), {"text"})
        if isinstance(message.get("content"), str):
            texts = [message["content"]]
    else:
        if record.get("type") != "response_item":
            return None
        payload = record.get("payload")
        if not isinstance(payload, dict) or payload.get("type") != "message":
            return None
        role = str(payload.get("role", ""))
        if role not in {"user", "assistant"}:
            return None
        texts = text_blocks(payload.get("content"), {"input_text", "output_text"})

    clean = [value.strip() for value in texts if not is_noise(value, source, role)]
    if not clean:
        return None
    return role, "\n\n".join(clean)


def metadata_from_record(record: dict[str, Any], source: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    if source == "codex" and record.get("type") == "session_meta":
        payload = record.get("payload")
        if isinstance(payload, dict):
            metadata["session_id"] = str(payload.get("id") or payload.get("session_id") or "")
            metadata["cwd"] = str(payload.get("cwd") or "")
            metadata["started_at"] = str(payload.get("timestamp") or record.get("timestamp") or "")
    elif source == "claude":
        session_id = record.get("sessionId")
        cwd = record.get("cwd")
        if session_id:
            metadata["session_id"] = str(session_id)
        if cwd:
            metadata["cwd"] = str(cwd)
        timestamp = record.get("timestamp")
        if timestamp:
            metadata.setdefault("started_at", str(timestamp))
    return metadata


def parse_session(
    path: Path,
    source: str,
    queries: Sequence[str],
    message_limit: int,
    max_message_chars: int,
) -> dict[str, Any]:
    messages: collections.deque[dict[str, str]] = collections.deque(maxlen=max(message_limit, 1))
    metadata: dict[str, str] = {"session_id": path.stem, "cwd": "", "started_at": ""}
    last_timestamp: dt.datetime | None = None
    first_user = ""
    relevance = 0
    query_lower = [query.lower() for query in queries if query.strip()]
    previous_key: tuple[str, str] | None = None

    for record in iter_jsonl(path):
        for key, value in metadata_from_record(record, source).items():
            if value and (not metadata.get(key) or key == "cwd"):
                metadata[key] = value
        timestamp = parse_timestamp(record.get("timestamp"))
        if timestamp and (last_timestamp is None or timestamp > last_timestamp):
            last_timestamp = timestamp
        message = message_from_record(record, source)
        if message is None:
            continue
        role, text = message
        normalized = re.sub(r"\s+", " ", text).strip()
        key = (role, normalized)
        if key == previous_key:
            continue
        previous_key = key
        if role == "user" and not first_user:
            first_user = compact(text, 160)
        lowered = text.lower()
        if query_lower:
            relevance += sum(lowered.count(query) for query in query_lower)
        messages.append(
            {
                "timestamp": str(record.get("timestamp") or ""),
                "role": role,
                "text": truncate(text, max_message_chars),
            }
        )

    started = parse_timestamp(metadata.get("started_at"))
    file_time = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.timezone.utc)
    effective_last = last_timestamp or started or file_time
    return {
        "source": source,
        "session_id": metadata.get("session_id") or path.stem,
        "cwd": metadata.get("cwd") or "",
        "started_at": iso_utc(started) if started else "",
        "updated_at": iso_utc(effective_last),
        "path": str(path),
        "title": first_user or path.stem,
        "relevance": relevance,
        "messages": list(messages),
    }


def session_roots() -> dict[str, list[Path]]:
    claude_base = Path(os.environ.get("CLAUDE_CONFIG_DIR", str(Path.home() / ".claude"))).expanduser()
    codex_base = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
    return {
        "claude": [claude_base / "projects"],
        "codex": [codex_base / "sessions", codex_base / "archived_sessions"],
    }


def source_paths(agent: str, include_subagents: bool) -> list[tuple[str, Path]]:
    selected = ["claude", "codex"] if agent == "both" else [agent]
    result: list[tuple[str, Path]] = []
    for source in selected:
        for root in session_roots()[source]:
            if not root.exists():
                continue
            for path in root.rglob("*.jsonl"):
                if source == "claude" and not include_subagents and "subagents" in path.parts:
                    continue
                result.append((source, path))
    return result


def rg_matching_paths(paths: list[Path], queries: Sequence[str]) -> set[Path] | None:
    if not queries or shutil.which("rg") is None or not paths:
        return None
    current = paths
    for query in queries:
        command = ["rg", "-l", "-i", "-F", "--", query, *[str(path) for path in current]]
        try:
            result = subprocess.run(command, text=True, capture_output=True)
        except OSError:
            return None
        if result.returncode not in {0, 1}:
            return None
        matched = {Path(line) for line in result.stdout.splitlines() if line.strip()}
        current = [path for path in current if path in matched]
        if not current:
            break
    return set(current)


def discover_sessions(args: argparse.Namespace) -> list[dict[str, Any]]:
    project = infer_project_root(args.project)
    cutoff = utc_now() - dt.timedelta(days=args.days)
    pairs = []
    for source, path in source_paths(args.agent, args.include_subagents):
        try:
            modified = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.timezone.utc)
        except OSError:
            continue
        if modified >= cutoff:
            pairs.append((source, path, modified))

    by_source: dict[str, list[tuple[Path, dt.datetime]]] = {"claude": [], "codex": []}
    for source, path, modified in pairs:
        by_source[source].append((path, modified))

    sessions: list[dict[str, Any]] = []
    for source, candidates in by_source.items():
        if not candidates:
            continue
        candidates.sort(key=lambda item: item[1], reverse=True)
        paths = [item[0] for item in candidates]
        matched = rg_matching_paths(paths, args.query)
        if matched is not None:
            paths = [path for path in paths if path in matched]
        paths = paths[: args.scan_limit]
        for path in paths:
            session = parse_session(path, source, args.query, args.messages, args.max_message_chars)
            query_match = not args.query or session["relevance"] >= len(args.query)
            project_match = is_within(session.get("cwd"), project)
            if args.query:
                if not query_match:
                    continue
            elif not project_match:
                continue
            session["project_match"] = project_match
            sessions.append(session)

    sessions.sort(
        key=lambda item: (
            item["updated_at"],
            item["relevance"],
        ),
        reverse=True,
    )
    return sessions[: args.sessions]


def markdown_sessions(sessions: Sequence[dict[str, Any]]) -> str:
    if not sessions:
        return "_No matching visible sessions found._\n"
    lines: list[str] = []
    for session in sessions:
        lines.extend(
            [
                f"## {session['source'].title()} · {session['session_id']}",
                "",
                f"- Updated: {session['updated_at']}",
                f"- CWD: `{session['cwd'] or 'unknown'}`",
                f"- Source: `{session['path']}`",
                f"- Match score: {session['relevance']}",
                "",
            ]
        )
        for message in session["messages"]:
            stamp = message["timestamp"] or "unknown-time"
            lines.extend(
                [
                    f"### {stamp} · {message['role']}",
                    "",
                    message["text"],
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def git_snapshot(project: Path) -> str:
    def run_git(*values: str) -> str:
        try:
            result = subprocess.run(
                ["git", "-C", str(project), *values],
                check=True,
                text=True,
                capture_output=True,
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ""

    branch = run_git("branch", "--show-current") or "(detached or not a Git repository)"
    status = run_git("status", "--short")
    commits = run_git("log", "-5", "--pretty=format:%h %ad %s", "--date=short")
    status_block = status if status else "(clean)"
    commits_block = commits if commits else "(none)"
    return (
        f"- Root: `{project}`\n"
        f"- Branch: `{branch}`\n\n"
        "### Working tree\n\n"
        f"```text\n{status_block}\n```\n\n"
        "### Recent commits\n\n"
        f"```text\n{commits_block}\n```\n"
    )


def store_paths(project: Path) -> dict[str, Path]:
    base = project / ".agent-sync"
    return {
        "base": base,
        "events": base / "events.jsonl",
        "progress": base / "PROGRESS.md",
        "imports": base / "imports",
        "ignore": base / ".gitignore",
        "lock": base / ".events.lock",
    }


def ensure_store(project: Path) -> dict[str, Path]:
    paths = store_paths(project)
    paths["imports"].mkdir(parents=True, exist_ok=True)
    required_ignores = ("imports/", "*.lock")
    existing_ignores = (
        paths["ignore"].read_text(encoding="utf-8").splitlines()
        if paths["ignore"].exists()
        else []
    )
    missing_ignores = [value for value in required_ignores if value not in existing_ignores]
    if missing_ignores:
        updated_ignores = [*existing_ignores, *missing_ignores]
        atomic_write(paths["ignore"], "\n".join(updated_ignores).rstrip() + "\n")
    if not paths["events"].exists():
        paths["events"].touch()
    return paths


def load_events(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    if not path.exists():
        return events
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise RuntimeError(f"Could not read curated ledger {path}: {error}") from error
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(
                f"Refusing to render {path}: invalid JSON on line {line_number}."
            ) from error
        if not isinstance(record, dict):
            raise RuntimeError(
                f"Refusing to render {path}: line {line_number} is not an object."
            )
        if record.get("version") != SCHEMA_VERSION or not record.get("id"):
            raise RuntimeError(
                f"Refusing to render {path}: unsupported event on line {line_number}."
            )
        events.append(record)
    return events


def bullet_section(title: str, values: Iterable[tuple[str, str]]) -> list[str]:
    collected = list(values)
    if not collected:
        return []
    lines = [f"## {title}", ""]
    for stamp, value in collected:
        lines.append(f"- {value}")
        lines.append(f"  _{stamp}_")
    lines.append("")
    return lines


def render_progress(
    project: Path,
    events: Sequence[dict[str, Any]],
    rendered_at: str | None = None,
) -> str:
    stable_rendered_at = rendered_at or (
        str(events[-1].get("timestamp") or "")
        if events
        else "1970-01-01T00:00:00Z"
    )
    lines = [
        "# Cross-agent project progress",
        "",
        "> Curated shared state for Claude Code and Codex. Raw transcript imports are local-only.",
        "",
        f"- Project: `{project.name}`",
        f"- Rendered: {stable_rendered_at}",
        f"- Events: {len(events)}",
        "",
    ]
    if not events:
        lines.extend(
            [
                "No curated progress has been recorded yet.",
                "",
                "Run `agent_sync.py update` after importing and verifying the project context.",
                "",
            ]
        )
        return "\n".join(lines)

    latest = events[-1]
    lines.extend(
        [
            "## Latest shared handoff",
            "",
            f"**{latest['timestamp']} · {latest['source']}**",
            "",
            latest["summary"],
            "",
        ]
    )
    latest_fields = (
        ("Decisions", "decisions"),
        ("Evidence", "evidence"),
        ("Completed", "completed"),
        ("Next actions", "next_actions"),
        ("Blockers", "blockers"),
        ("Artifacts", "artifacts"),
        ("Notes", "notes"),
    )
    for label, key in latest_fields:
        values = latest.get(key) or []
        if values:
            lines.extend([f"### {label}", ""])
            lines.extend(f"- {value}" for value in values)
            lines.append("")

    category_fields = (
        ("Decision ledger", "decisions"),
        ("Evidence ledger", "evidence"),
        ("Completed-work ledger", "completed"),
        ("Recorded next actions", "next_actions"),
        ("Recorded blockers", "blockers"),
        ("Artifact index", "artifacts"),
    )
    for title, key in category_fields:
        values: list[tuple[str, str]] = []
        seen: set[str] = set()
        for event in reversed(events):
            for value in reversed(event.get(key) or []):
                normalized = re.sub(r"\s+", " ", value).strip().lower()
                if not normalized or normalized in seen:
                    continue
                seen.add(normalized)
                values.append((f"{event['timestamp']} · {event['source']}", value))
        lines.extend(bullet_section(title, values[:50]))

    lines.extend(["## Timeline", ""])
    for event in reversed(events[-25:]):
        lines.extend(
            [
                f"### {event['timestamp']} · {event['source']}",
                "",
                event["summary"],
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def rendered_at_from_progress(content: str) -> str | None:
    """Return the timestamp embedded in a rendered progress view."""
    match = re.search(r"^- Rendered: (.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else None


def progress_extras(
    path: Path,
    project: Path,
    events: Sequence[dict[str, Any]],
) -> tuple[str, str]:
    """Return content outside the generated view without losing manual text.

    Raises:
        RuntimeError: If existing content cannot be separated safely from the
            generated view.
    """
    if not path.exists():
        return "", "\n"

    existing = path.read_text(encoding="utf-8")
    if not existing:
        return "", "\n"

    start_count = existing.count(GENERATED_START)
    end_count = existing.count(GENERATED_END)

    if start_count or end_count:
        if start_count != 1 or end_count != 1:
            raise RuntimeError(
                f"Refusing to overwrite {path}: malformed generated markers."
            )
        prefix, marked = existing.split(GENERATED_START, 1)
        generated, suffix = marked.split(GENERATED_END, 1)
        if generated.startswith("\n"):
            generated = generated[1:]
        rendered_at = rendered_at_from_progress(generated)
        if rendered_at is None:
            raise RuntimeError(
                f"Refusing to overwrite {path}: generated timestamp is missing."
            )
        expected = render_progress(
            project,
            events,
            rendered_at=rendered_at,
        )
        if generated != expected:
            raise RuntimeError(
                f"Refusing to overwrite {path}: the generated view contains "
                "untracked edits."
            )
        return prefix, suffix

    rendered_at = rendered_at_from_progress(existing)
    if rendered_at is None:
        raise RuntimeError(
            f"Refusing to overwrite {path}: existing content is not a "
            "recognized generated view."
        )
    expected = render_progress(
        project,
        events,
        rendered_at=rendered_at,
    )
    if existing == expected:
        return "", "\n"
    if existing.startswith(expected):
        return "", existing[len(expected) :]
    raise RuntimeError(
        f"Refusing to overwrite {path}: existing content differs inside the "
        "generated view."
    )


def progress_with_extras(
    generated: str,
    prefix: str,
    suffix: str,
) -> str:
    """Wrap a generated view while preserving content outside it."""
    return (
        f"{prefix}{GENERATED_START}\n"
        f"{generated}"
        f"{GENERATED_END}{suffix}"
    )


def render_store(project: Path) -> Path:
    paths = ensure_store(project)
    events = load_events(paths["events"])
    prefix, suffix = progress_extras(
        paths["progress"],
        project,
        events,
    )
    atomic_write(
        paths["progress"],
        progress_with_extras(
            render_progress(project, events),
            prefix,
            suffix,
        ),
    )
    return paths["progress"]


def normalized_list(value: Any) -> list[str]:
    if value is None:
        return []
    values = value if isinstance(value, list) else [value]
    return [str(item).strip() for item in values if str(item).strip()]


def build_event(args: argparse.Namespace) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    if args.from_json:
        try:
            payload = json.loads(Path(args.from_json).expanduser().read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise SystemExit(f"Could not read update JSON: {error}") from error
        if not isinstance(payload, dict):
            raise SystemExit("Update JSON must contain one object.")

    def select(cli_value: Any, json_key: str, default: Any = None) -> Any:
        return cli_value if cli_value not in (None, [], "") else payload.get(json_key, default)

    summary = str(select(args.summary, "summary", "")).strip()
    if not summary:
        raise SystemExit("An update requires --summary or a JSON summary.")
    event: dict[str, Any] = {
        "version": SCHEMA_VERSION,
        "timestamp": iso_utc(),
        "source": str(select(args.source, "source", "agent")).strip().lower(),
        "session_id": str(select(args.session_id, "session_id", "")).strip(),
        "summary": summary,
        "decisions": normalized_list(select(args.decision, "decisions", [])),
        "evidence": normalized_list(select(args.evidence, "evidence", [])),
        "completed": normalized_list(select(args.completed, "completed", [])),
        "next_actions": normalized_list(select(args.next_action, "next_actions", [])),
        "blockers": normalized_list(select(args.blocker, "blockers", [])),
        "artifacts": normalized_list(select(args.artifact, "artifacts", [])),
        "notes": normalized_list(select(args.note, "notes", [])),
    }
    semantic_event = {key: value for key, value in event.items() if key != "timestamp"}
    digest_payload = json.dumps(semantic_event, sort_keys=True, separators=(",", ":")).encode("utf-8")
    event["id"] = hashlib.sha256(digest_payload).hexdigest()[:20]
    return event


def append_event(project: Path, event: dict[str, Any]) -> tuple[Path, bool]:
    paths = ensure_store(project)
    with paths["lock"].open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        events = load_events(paths["events"])
        prefix, suffix = progress_extras(
            paths["progress"],
            project,
            events,
        )
        duplicate = any(existing.get("id") == event["id"] for existing in events)
        if not duplicate:
            with paths["events"].open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
            events.append(event)
        atomic_write(
            paths["progress"],
            progress_with_extras(
                render_progress(project, events),
                prefix,
                suffix,
            ),
        )
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return paths["progress"], not duplicate


def import_packet(project: Path, sessions: Sequence[dict[str, Any]]) -> str:
    paths = store_paths(project)
    progress = (
        paths["progress"].read_text(encoding="utf-8")
        if paths["progress"].exists()
        else "_No curated shared progress exists yet._\n"
    )
    return (
        "# Cross-agent import packet\n\n"
        "> Local evidence packet. Do not commit; verify before updating shared progress.\n\n"
        f"- Generated: {iso_utc()}\n"
        f"- Project: `{project}`\n\n"
        "## Repository snapshot\n\n"
        f"{git_snapshot(project)}\n"
        "## Curated shared progress\n\n"
        f"{progress.rstrip()}\n\n"
        "## Recent visible session entries\n\n"
        f"{markdown_sessions(sessions)}"
    )


def add_discovery_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project", help="Project/repository root; defaults to the current Git root.")
    parser.add_argument("--agent", choices=["claude", "codex", "both"], default="both")
    parser.add_argument("--query", action="append", default=[], help="Case-insensitive term required in visible messages; repeatable.")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--sessions", type=int, default=6)
    parser.add_argument("--messages", type=int, default=16, help="Recent visible messages retained per session.")
    parser.add_argument("--max-message-chars", type=int, default=4000)
    parser.add_argument("--scan-limit", type=int, default=200, help="Maximum candidate files parsed per harness.")
    parser.add_argument("--include-subagents", action="store_true")


def command_list(args: argparse.Namespace) -> int:
    sessions = discover_sessions(args)
    if args.json:
        concise = [{key: value for key, value in session.items() if key != "messages"} for session in sessions]
        print(json.dumps(concise, indent=2, ensure_ascii=False))
    else:
        if not sessions:
            print("No matching sessions found.")
            return 0
        for session in sessions:
            print(
                f"{session['updated_at']}  {session['source']:6}  "
                f"{session['session_id']}  score={session['relevance']}  "
                f"cwd={session['cwd'] or 'unknown'}  {compact(session['title'], 80)}"
            )
    return 0


def command_recent(args: argparse.Namespace) -> int:
    sessions = discover_sessions(args)
    if args.json:
        print(json.dumps(sessions, indent=2, ensure_ascii=False))
    else:
        print(markdown_sessions(sessions), end="")
    return 0


def command_import(args: argparse.Namespace) -> int:
    project = infer_project_root(args.project)
    sessions = discover_sessions(args)
    packet = import_packet(project, sessions)
    if args.write:
        paths = ensure_store(project)
        stamp = utc_now().strftime("%Y%m%dT%H%M%SZ")
        destination = (
            Path(args.output).expanduser().resolve()
            if args.output
            else paths["imports"] / f"import-{stamp}.md"
        )
        if not is_within(str(destination), paths["imports"]):
            raise SystemExit(
                "Import packets may only be written under .agent-sync/imports/."
            )
        atomic_write(destination, packet)
        print(destination)
    else:
        print(packet, end="")
    return 0


def command_sync(args: argparse.Namespace) -> int:
    project = infer_project_root(args.project)
    progress = render_store(project)
    sessions = discover_sessions(args)
    paths = ensure_store(project)
    stamp = utc_now().strftime("%Y%m%dT%H%M%SZ")
    destination = paths["imports"] / f"import-{stamp}.md"
    atomic_write(destination, import_packet(project, sessions))
    print(f"progress={progress}")
    print(f"import={destination}")
    print(f"sessions={len(sessions)}")
    return 0


def command_update(args: argparse.Namespace) -> int:
    project = infer_project_root(args.project)
    event = build_event(args)
    progress, appended = append_event(project, event)
    print(f"{'appended' if appended else 'duplicate'}={event['id']}")
    print(f"progress={progress}")
    return 0


def command_render(args: argparse.Namespace) -> int:
    project = infer_project_root(args.project)
    print(render_store(project))
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    project = infer_project_root(args.project)
    roots = session_roots()
    report: dict[str, Any] = {
        "project": str(project),
        "git": (project / ".git").exists(),
        "store": str(store_paths(project)["base"]),
        "claude_roots": [str(path) for path in roots["claude"]],
        "codex_roots": [str(path) for path in roots["codex"]],
        "claude_logs": sum(1 for root in roots["claude"] if root.exists() for _ in root.rglob("*.jsonl")),
        "codex_logs": sum(1 for root in roots["codex"] if root.exists() for _ in root.rglob("*.jsonl")),
        "ripgrep": bool(shutil.which("rg")),
    }
    print(json.dumps(report, indent=2))
    return 0 if report["claude_logs"] and report["codex_logs"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Import recent Claude/Codex context and maintain a shared curated project ledger."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List relevant sessions.")
    add_discovery_args(list_parser)
    list_parser.add_argument("--json", action="store_true")
    list_parser.set_defaults(func=command_list)

    recent_parser = subparsers.add_parser("recent", help="Print bounded visible session entries.")
    add_discovery_args(recent_parser)
    recent_parser.add_argument("--json", action="store_true")
    recent_parser.set_defaults(func=command_recent)

    import_parser = subparsers.add_parser("import", help="Build a project/session import packet.")
    add_discovery_args(import_parser)
    import_parser.add_argument("--write", action="store_true", help="Write under .agent-sync/imports instead of stdout.")
    import_parser.add_argument(
        "--output",
        help="Explicit destination under .agent-sync/imports/, used with --write.",
    )
    import_parser.set_defaults(func=command_import)

    sync_parser = subparsers.add_parser("sync", help="Render shared progress and write a fresh local import packet.")
    add_discovery_args(sync_parser)
    sync_parser.set_defaults(func=command_sync)

    update_parser = subparsers.add_parser("update", help="Append one curated progress delta.")
    update_parser.add_argument("--project")
    update_parser.add_argument("--from-json")
    update_parser.add_argument("--source")
    update_parser.add_argument("--session-id")
    update_parser.add_argument("--summary")
    update_parser.add_argument("--decision", action="append")
    update_parser.add_argument("--evidence", action="append")
    update_parser.add_argument("--completed", action="append")
    update_parser.add_argument("--next", dest="next_action", action="append")
    update_parser.add_argument("--blocker", action="append")
    update_parser.add_argument("--artifact", action="append")
    update_parser.add_argument("--note", action="append")
    update_parser.set_defaults(func=command_update)

    render_parser = subparsers.add_parser("render", help="Regenerate PROGRESS.md from events.jsonl.")
    render_parser.add_argument("--project")
    render_parser.set_defaults(func=command_render)

    doctor_parser = subparsers.add_parser("doctor", help="Verify both harness stores and the target project.")
    doctor_parser.add_argument("--project")
    doctor_parser.set_defaults(func=command_doctor)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "days") and args.days < 1:
        parser.error("--days must be positive.")
    if hasattr(args, "sessions") and args.sessions < 1:
        parser.error("--sessions must be positive.")
    if hasattr(args, "messages") and args.messages < 1:
        parser.error("--messages must be positive.")
    if hasattr(args, "max_message_chars") and args.max_message_chars < 1:
        parser.error("--max-message-chars must be positive.")
    if hasattr(args, "scan_limit") and args.scan_limit < 1:
        parser.error("--scan-limit must be positive.")
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
