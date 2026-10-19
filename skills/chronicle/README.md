# Chronicle

**A historical backbone for Git projects: the files, the work, and the reasons behind them.**

An agent returning to a project needs more than the current checkout. It needs to know
what was tried, why an approach was abandoned, whether an odd-looking state is intentional,
what happened before and after a change, and how to get back to an earlier version without
losing the context that made that version meaningful.

Chronicle keeps that history outside any one conversation. It combines an observed work
trace, captured file contents, and a first-hand narrative of decisions into a record that
humans and agents can read, search, compare, and use for recovery. Its purpose is continuity
through the life of a project—not just a log to inspect after something breaks.

The goal is to let a fresh agent reconstruct the project's working context, not merely its
latest code. The current implementation supports recovery of captured files and retrieval
of their surrounding history; it does **not** provide a one-command, complete rollback of
every file, process, database, and external service.

## Why Git alone is not the whole story

Git can version anything you deliberately put into it. Ordinary commits do not automatically
preserve every intermediate edit, command output, experiment, or reason for choosing one
direction over another. A commit message can explain a decision—but only if someone wrote
it down, and only at the granularity of that commit.

Chronicle complements Git by keeping the working history around those checkpoints:

| Question on returning to a project | What Chronicle gives you |
| --- | --- |
| What changed while another session was working? | Captured events, touched files, and Git references in the resume view |
| Why does this file look like this? | Recorded decisions and state declarations, with file-related narrative lookup |
| What came before and after the change? | Timestamped events, captured before/after contents, diffs, and a local timeline |
| Can I recover an intermediate version that never became a commit? | A file restored from the content store, if that version was captured and retained |
| Why did we stop, and what must not be repeated? | Open questions, abandoned approaches, experiment outcomes, and explicit unfinished work |

This is useful for long-running projects, agent handoffs, interrupted sessions, exploratory
refactors, and incident reconstruction. It makes the project's history retrievable instead
of requiring the next agent to guess from the final diff or reread an entire conversation.

## Two kinds of memory, kept distinct

**The trace records what was observed.** Active integrations capture supported events such
as prompts, tool calls, command output, Git state, and file reads or edits. Recognized file
editing tools can capture contents before and after the operation, including uncommitted
versions. File contents are stored by hash so repeated content can be reused.

**The narrative records what the actor meant.** The human or agent states the decision,
reason, intended outcome, verified result, and what is deliberately unfinished. A command
trace cannot tell whether an empty page is a bug or intentional staging. A short state
declaration can.

The CLI connects those layers. `chron resume` offers a bounded re-entry point; history,
search, diffs, and the canvas let you investigate further. Keeping the full record available
does not mean injecting all of it into every model context window.

## What is in this repository?

- A Python CLI (`chron`) for recording intent, reading history, and restoring captured files.
- An [Agent Skill](SKILL.md) that teaches the agent when to read back and what only it can
  record: decisions, intent, evidence, recovery plans, and handoffs.
- Optional capture hooks for supported agent, shell, and Git events.
- A local web canvas for exploring the timeline, narrative, file contents, and diffs.

Installing the skill teaches a workflow. Installing the CLI supplies the tools. Installing
and verifying hooks establishes capture. These are separate steps. The capture core and
CLI use the Python standard library; model calls are not required for either.

## Install

Python 3.10 or later on macOS or Linux (the standalone capture core also runs on 3.9):

```bash
pipx install 'git+https://github.com/AntreasAntoniou/chronicle.git'
npx skills add AntreasAntoniou/chronicle
chron --help
```

Or clone this repository and run `pip install -e '.[dev,canvas]'` in a virtual environment.
This release comes from GitHub, not the unrelated PyPI package of the same name.

## A working session

Run these commands in the project root. This illustrative sequence shows the shape of the
record; replace its claims with your own observed results:

```bash
chron resume
chron open "continue search" --state "empty results are intentional staging"
chron decision "retain src/search.py's current index" \
  --why "the replacement failed the latency target in the recorded experiment"
chron close "stopped after the index comparison" \
  --not-done "production rollout remains pending" \
  --open "does the current index meet the larger-corpus target?"
```

Use measured evidence. Correct earlier claims by appending `chron correct`, preserving the
original. Optional narration always carries an `inferred` label and cannot create an ARM
or CLOSE.

Before a destructive or bulk operation, use `chron arm` to record its intent,
reversibility class, and a verified recovery path. After an external change, use
`chron landed` to record the resource/version and evidence of its actual state. Neither
entry grants permission, performs the operation, or proves that it succeeded. See the
[skill's operating contract](SKILL.md) for those commands.

## Enable capture

Capture covers only installed, active, verified integrations. It cannot reconstruct a
version that was never captured. Excluded, oversized, or unreadable files can leave gaps.

```bash
chron install-hooks --dry-run
chron install-hooks --shell --git
chron doctor
```

The local installer adds Claude Code hooks by default. `--shell` additionally installs a
zsh hook; `--git` installs hooks in registered repositories. Configuration is merged with
backups. Make a harmless edit and inspect its event before relying on coverage. Shell
capture requires the shell hook to be sourced.

Codex hooks are experimental and version-dependent. Read
[the integration notes](references/codex.md). Chronicle never grants or renews hook trust.
Configuration alone does not prove that a hook executed.

## Read and recover

Suppose an agent replaced a useful search implementation during an experiment, then the
session ended before a commit. If the edit was captured, you can inspect its versions,
read the recorded reasoning, and recover the earlier file to a separate location:

```bash
chron history src/app.py
chron why src/app.py
chron show src/app.py --at 2h
chron diff src/app.py --from 2h --to now
chron restore src/app.py --at 2h --to /tmp/recovered-app.py
chron search "search index"
chron doctor
```

Use a path reported by `chron history` or `chron files`, and a timestamp from the record
when choosing an exact checkpoint. The relative `2h` example means two hours ago at the
time you run it. `chron why` finds narrative mentioning the file; it does not invent an
explanation where none was recorded.

Restoring to a separate path lets you inspect the result before touching current work.
An existing destination is refused unless you explicitly use `--force`.

### What recovery does—and does not—mean

Chronicle can recover **stored contents** beyond the versions you committed to Git and
help you reconstruct the context around them. Complete restoration depends on the evidence
and recovery artifacts you actually kept:

- It is not a filesystem-wide snapshotter. Unobserved edits, including changes made by a
  shell command without individual file capture, may have no recoverable file version.
- Exclusions, size limits, capture suspension, unavailable blobs, and failed hooks leave
  gaps. Redacted text restores as stored, not as the original secret-bearing bytes.
- The restore command writes one file's contents. It does not recreate a whole repository
  atomically or restore permissions, running processes, databases, cloud resources, or
  secrets. Those need their own backups and tested restore procedures.
- A recorded rollback command is context for an authorized recovery, not an executed or
  verified rollback. Preserve and back up the event lanes and content store as well as Git.

The aim is recovery of **files plus understanding**. Treat missing history as a gap, not an
invitation for an agent to fill it with a plausible story.

## Explore the history visually

Install the `canvas` extra and run `chron canvas` for the optional web interface. Keep its
default loopback binding: it exposes private history and has no authentication layer.

The canvas brings narrative and trace events onto one timeline with file views and diffs.
It is a way to inspect the evidence behind an account of the work, not a separate source
of truth.

## Storage and synchronization

Events live in append-only JSONL lanes under `.chronicle/` or `~/.chronicle/lanes/`.
Captured content lives in `~/.chronicle/cas/`; curated narrative lives in `CHRONICLE.md`.
Keep all of these private.

New captures use gzip across supported Python versions. Legacy Zstandard-only blobs
require Python 3.14 or later to read; a gzip copy is preferred when both exist.

`chron sync` stays local by default. Set `CHRONICLE_REMOTES` to a space-separated list of
SSH hosts for remote pulls. `CHRONICLE_SPINE` or `--spine` selects the destination.
**Local blob pushes** encrypt with `age`, or skip blobs when recipients are missing.
Store public recipients in `~/.chronicle/age_recipients.txt`, or set
`CHRONICLE_RECIPIENTS` to the path of another recipients file.

The current **remote-pull** path copies a remote content store directly over SSH; it does
not apply that local-push encryption step. A spine can therefore contain unencrypted
compressed file contents as well as plaintext event metadata. Keep it private, protect its
storage and backups, and inspect its contents before any repository commit or transfer.
Do not interpret configured recipients as a guarantee that the whole spine is encrypted.

Redaction cannot guarantee detection of every embedded secret. Read
[SECURITY.md](SECURITY.md) before enabling capture.

## Optional narration

Narration sends selected trace and transcript content through your Claude CLI and can
incur costs. Review `chron narrate --dry-run`, then set `CHRONICLE_NARRATOR_MODEL` to a model
available to your account. `CHRONICLE_NARRATOR_BUDGET` bounds prompt bytes, not spend.
Butler checks a project budget when installed; absent Butler is not a spending cap.
Capture, the CLI, and the canvas require no model calls.

## How it fits with the other continuity skills

- **Chronicle:** reconstruct the work—events, intermediate file versions, decisions, and
  recovery context within a project's history.
- **[Cross-Agent Sync](https://github.com/AntreasAntoniou/cross-agent-sync):** share a small,
  curated current-state handoff between Claude Code and Codex.
- **[Argus](https://github.com/AntreasAntoniou/argus-skill):** move lasting knowledge and
  commitments to their canonical records instead of leaving them buried in conversation.

They answer different questions: what happened, what does the next agent need now, and
what should become durable knowledge. Chronicle works without the other two.

## Development

```bash
pip install -e '.[dev]'
pytest -q
python src/chronicle/capture.py selftest
```

Tests cover concurrent append, interrupted writes, excluded content, command
classification, additive installation, and inferred-entry boundaries. The hook gate is a
coordination aid; enforcement depends on the host invoking and honoring it.

MIT licensed. See [CONTRIBUTING.md](CONTRIBUTING.md).
