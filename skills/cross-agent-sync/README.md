# Cross-Agent Sync

**Let the next agent pick up the work without starting the conversation over.**

You investigate a problem in Claude Code, implement part of the fix in Codex, and return
later in a fresh session. The files are shared, but the reasoning, unfinished work, and
verification results are scattered across conversations. An agent that only sees the
checkout can repeat a failed approach, mistake a draft for a finished change, or assume
that a local test proves a deployment.

Cross-Agent Sync gives those sessions a small, inspectable shared handoff. It helps an
agent find relevant local conversations, check their claims against current artifacts,
and record the verified delta where either harness can read it. The useful output is a
current account of **decisions, evidence, completed work, blockers, and next actions**—not
a dump of somebody else's chat history.

This repository contains an [Agent Skill](SKILL.md) for doing that reconciliation and a
Python transport for discovery, bounded imports, and deterministic ledger updates. The
transport does not understand or adjudicate the conversations; the human or agent reading
the evidence supplies the judgment.

It reads local JSONL logs, creates a bounded local-only evidence packet, and maintains two project files:

```text
.agent-sync/
├── .gitignore
├── events.jsonl       # append-only curated deltas
├── PROGRESS.md        # deterministic human-readable view
└── imports/           # raw excerpts; always ignored by Git
```

## Why this boundary

Raw agent logs mix useful context with personal text, local paths, tool output, and instructions that were valid only in one session. Cross-Agent Sync treats those logs as evidence to inspect, not authority to act. Only a concise human- or agent-curated delta belongs in version control.

The script does not call a model, upload data, or contact a service. It reads files on the local machine and writes only inside the selected project.

## What a handoff looks like

For example, one agent reports that a migration passed tests; another says the release is
still blocked. Those statements may both be true: the tests passed locally, but deployment
has not happened. A useful handoff preserves that distinction:

1. Find the relevant sessions and import a bounded evidence packet locally.
2. Inspect the cited test result, commit, or release artifact. Surface conflicts instead
   of silently choosing the more confident account.
3. Append a concise delta: what is verified, what remains blocked, and the next step.
4. The next session reads `PROGRESS.md`, then follows evidence links when it needs detail.

That loop is especially useful when switching harnesses, recovering after an interruption,
or coordinating sessions that share a repository but not a context window. It is not a
live message bus: an agent or scheduled workflow must invoke it, and a ledger entry does
not notify or control another running agent.

## Quick start

Requirements: Python 3.10+, Git, and macOS or Linux. `rg` is optional but speeds up query filtering.

Install the skill:

```bash
npx skills add AntreasAntoniou/cross-agent-sync
```

The commands below use paths relative to this repository. Run them from its installed
skill directory, or clone it first:

```bash
git clone https://github.com/AntreasAntoniou/cross-agent-sync.git
cd cross-agent-sync
```

Then run the local transport:

```bash
python3 scripts/agent_sync.py doctor --project /path/to/project
python3 scripts/agent_sync.py sync --project /path/to/project --query project-name --days 14
```

Then inspect `.agent-sync/PROGRESS.md` and the new file under `.agent-sync/imports/`.

These paths are inside the selected target project, not necessarily your current directory.
`sync` creates the packet and refreshes the view; it does **not** automatically summarize
the packet into a new verified event. The `update` step below is deliberate.

Record only a verified summary:

```bash
python3 scripts/agent_sync.py update \
  --project /path/to/project \
  --source codex \
  --summary "Verified the migration against the current repository." \
  --evidence "Tests passed at commit abc1234." \
  --next "Review the remote deployment."
```

The commit and result above are illustrative placeholders: supply actual evidence from
your project, not those example claims.

See [SKILL.md](SKILL.md) for the complete operating contract and [session-formats.md](references/session-formats.md) for the supported log records.

## Privacy model

- Session discovery is local-only.
- Imported packets may contain transcript text and absolute paths. They are forced under `.agent-sync/imports/` and ignored by Git.
- The committed progress view uses the project directory name, not its absolute path.
- The tool excludes reasoning, tool calls/results, system material, generated instructions, and known notification wrappers.
- It cannot identify every secret in free-form human text. Review the curated delta before committing it.
- An import never grants authority for an external action.

## Determinism and failure behavior

- Event IDs are derived from semantic content, so retries are idempotent.
- Event JSON uses stable key ordering; progress sections have stable ordering and bounded history.
- The rendered timestamp is the latest event timestamp, so unchanged input renders byte-for-byte identically.
- Source JSONL is best-effort: malformed lines are skipped.
- Curated JSONL is canonical: malformed or unsupported events stop rendering rather than disappearing silently.
- Edits inside generated markers fail closed. Text outside the markers is preserved.
- Concurrent ledger appends use a POSIX advisory lock and an atomic replace for rendered output.

## Platform limits

The current implementation uses `fcntl.flock`, so Windows is not supported. Claude Code and Codex may change their internal log formats; use `doctor`, keep imports bounded, and update the parser when discovery stops matching. The tool supports the formats documented in this repository, not every historical or future harness build.

It does not synchronize source files, merge Git branches, transfer credentials, or clone
an agent's full memory. It also does not fetch logs from another machine. Share reviewed
ledger files through your normal repository workflow when appropriate; keep raw imports
local and private. `doctor` expects both supported session stores to contain logs, so a
machine with only one harness may report a missing store.

## How it fits with Chronicle and Argus

- **Cross-Agent Sync:** what does the next session need to know now, across harnesses?
- **[Chronicle](https://github.com/AntreasAntoniou/chronicle):** what happened in the
  project's working history, why, and which captured file versions can be recovered?
- **[Argus](https://github.com/AntreasAntoniou/argus-skill):** which lasting decisions,
  facts, or commitments belong in the canonical knowledge or task records?

Use this skill for a compact shared handoff. It does not require either companion and
does not replace their deeper history or knowledge-routing roles.

## Development

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q scripts tests
git diff --check
```

## License

MIT. See [LICENSE](LICENSE).
