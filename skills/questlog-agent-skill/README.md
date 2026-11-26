# Questlog

A small commitments ledger with a useful local cockpit: see the current focus, next steps, deadlines and waiting-on items without building a task database. Markdown remains the source of truth. Includes the original cockpit, compact bar and quick-add views, workstream parser, urgency logic, capture and structured mutation flows.

## Install and run

Python 3.10+ on macOS/Linux; standard library only. Copy or symlink the public `questlog-agent-skill` repository as `questlog` into your agent's skills directory to enable SKILL.md discovery. There is one entrypoint and no legacy alias. Runtime use does not require an agent.

With the skills CLI: `npx skills add https://github.com/AntreasAntoniou/questlog-agent-skill --skill questlog`. This installer requires Node/network access; inspect the repository before installing.

From the repository:

```sh
export QUESTLOG_ROOT="$PWD/.questlog"
python3 scripts/ledger.py init
python3 scripts/ledger.py show
python3 ui/server.py --port 8321
```

Open http://127.0.0.1:8321 for the overview, /bar for the interactive cockpit, /quickadd for capture. Stop with Ctrl-C. No daemon, scheduler, git repository, account or external service is initialized. Initial state has only an empty NOW and INBOX: no tasks, journal or demo records. Choose a dedicated private state directory outside the skill for permanent installation; startup applies owner-only permissions to that dedicated directory.

## Use the ledger

`python3 scripts/ledger.py capture "YOUR NOTE"` adds a local inbox note. `new "YOUR WORKSTREAM"` creates a warm workstream; `now "YOUR CURRENT ACTION"` sets the focus. These commands are local mutations, not external actions. `show` prints parsed state and the current content-hash revision. To replace an edited ledger safely, use `replace --file EDITED.md --base CURRENT_REVISION`; stale bases are rejected before any write. [Ledger grammar](references/ledger-format.md) describes the portable format.

The UI supports capture, new workstreams, state changes, NOW selection, subtasks, pins and card ordering. Pending instructions are **local drafts only**: there is no executor, mail/calendar integration, shell runner or auto-completion mechanism. Search is literal and local; semantic search is not bundled. Unsupported external integrations must be reviewed and explicitly configured separately.

## How concurrency works

Ledger writers share a POSIX file lock around read, validation, atomic replacement and an optional local history commit. HTTP structured writes additionally require an `If-Match` content revision; a stale request returns 409 without overwriting newer content. UI requests fetch a revision immediately before submission. This protects the storage transaction, but does not infer whether a decision made from an older visible card is still correct. Refresh/reconsider after conflicts. Arbitrary text editors that ignore the lock remain outside this contract; use the replacement command for full-file edits.

Enable the optional Git journal explicitly with `python3 scripts/ledger.py init --git` (requires Git). Successful ledger mutations commit only LEDGER.md; other staged files are not included. The cockpit shows recent commit subjects and workstream recency. Hooks are disabled and no remotes or pushes are configured or invoked. Default commit identity is `Questlog local ledger <questlog@localhost>`; set `QUESTLOG_GIT_NAME` and `QUESTLOG_GIT_EMAIL` if you want your own local identity. State's `head` remains the optimistic content revision; `git_head` is the separate Git commit. If committing fails after the atomic save, the error explicitly says the ledger was saved but uncommitted—inspect/recover history rather than blindly repeating a non-idempotent capture. To recover an older ledger, export it with `git show REV:LEDGER.md` and submit through `replace` with the current content revision. Keep independent backups: Git history is not a remote backup.

## Scope and security

The server binds only to loopback. Host and same-origin JSON checks protect the browser surface; request bodies are bounded. This is not a remotely authenticated multi-user service. State is private to the local user, and no transcript, ledger, calendar, account or operational history ships with the package. Runtime initialization never overwrites an existing ledger. Do not use a workspace root as QUESTLOG_ROOT because the dedicated state directory is chmod 0700.

Run `python3 -m unittest discover -s tests -v`. Node.js is required for the HTML escaper behavior tests; no browser/provider account is needed. Synthetic tests cover empty bootstrap, HTTP guards, stale revision rejection, parallel capture and XSS escaping. See [SECURITY.md](SECURITY.md). MIT licensed.
