# Session JSONL custody

## Purpose

Use raw project-related Codex and Claude session JSONLs as a primary historical
spine without confusing recorded conversation with verified external state.

## Common stores (never implicit scan targets)

- Codex commonly stores active rollouts under
  `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl` and older rollouts under
  `~/.codex/archived_sessions/`.
- Claude commonly stores project sessions under
  `~/.claude/projects/<encoded-project-path>/*.jsonl`; nested agent traces may
  appear below the session directory.

Discover by metadata, not filename alone. Associate a session with the
canonical Git root using recorded `cwd` or project-path metadata. For a session
that spans projects, retain only claim-level events demonstrably related to the
target. When a task explicitly references another live Codex task, use the
available thread-reading tool before relying on it.

Select the smallest approved store or prepared subset explicitly. A metadata-only
inventory is not metadata-only access: the helper reads and hashes input bytes to
find associations. Existing paths and identifiers in its output remain private.
Do not treat a match anywhere in a session as permission to disclose the rest of it.

## Evidential meaning

| JSONL event | What it establishes | What it does not establish |
|---|---|---|
| User prompt | Recorded authority, request, constraint, or intent | That the requested action occurred |
| Tool call | An action was attempted with recorded arguments | Success or complete execution |
| Tool output | The tool returned the recorded observation | State beyond the output's time, scope, truncation, or exit status |
| Assistant text | The assistant made the recorded claim | Independent truth of the claim |
| Summary or compacted context | A secondary synthesis and evidence locator | A substitute for the underlying raw events |

Use the strongest relevant event rather than granting the entire file one
evidence class. Re-probe drift-prone state when cheap and safe.

## Minimum provenance

For each session-backed Chronicle claim, retain:

- harness (`codex` or `claude`);
- private source index identifier and cryptographic hash (retain the absolute path
  in that private index, not in a public derivative);
- session or thread id;
- timestamp;
- line number, event id, or another stable item locator;
- event kind and claim-specific evidence class.

If copying an excerpt into a private evidence bundle, record the source hash
and keep the raw file unchanged. Prefer an index over duplicating whole session
corpora.

## Privacy and completeness

- Treat session JSONLs as private by default. They may contain prompts, tool
  arguments, environment data, personal information, and secrets.
- The inventory script emits metadata only; inspect matching raw files locally.
- Never paste credentials or irrelevant private conversation into Chronicle.
- Record unavailable, malformed, truncated, or unassociated session files as
  coverage gaps rather than silently treating the inventory as complete.
- Hashes prove byte identity, not truth.
