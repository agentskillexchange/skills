# Claude Code and Codex session formats

Use this reference only to repair or extend `scripts/agent_sync.py`.

## Claude Code

Default root: `~/.claude/projects/**/*.jsonl`.

Relevant records:

- Session metadata is distributed across records through `sessionId`, `cwd`, and `timestamp`.
- Visible messages use top-level `type: "user"` or `"assistant"`.
- Text may be a string in `message.content` or text blocks inside a content array.

Exclude:

- `subagents/` by default;
- tool-use and tool-result blocks;
- queue operations, attachments, system records, and file-history snapshots;
- synthetic wrappers such as `<task-notification>` and `<system-reminder>`.

## Codex

Default roots:

- `~/.codex/sessions/**/*.jsonl`
- `~/.codex/archived_sessions/**/*.jsonl`

Relevant records:

- `type: "session_meta"` contains `payload.id`, `payload.cwd`, and the session timestamp.
- Visible messages use `type: "response_item"`, `payload.type: "message"`, and role `user` or `assistant`.
- Text blocks use `input_text` or `output_text`.

Exclude:

- encrypted or summarized reasoning records;
- function calls and function outputs;
- event-message duplicates;
- injected user-role context blocks beginning with plugin lists, AGENTS instructions, or environment context.

## Shared ledger

Project-local store:

```text
.agent-sync/
├── .gitignore
├── events.jsonl
├── PROGRESS.md
└── imports/        # local-only raw excerpts
```

`events.jsonl` is append-only and contains curated deltas. `PROGRESS.md` is a deterministic rendering. Raw session files and import packets are never canonical project state.
