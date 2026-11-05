# Butler

Per-project resource accounting for agent and GPU work: understand spend, make an admission decision, reserve before launch, and replace reservations with measured outcomes. Includes the original substantial accounting engine, terminal panel and web dashboard.

## Install and run

Requires Python 3.10+ on macOS/Linux (POSIX file locking). The web UI and CLI use the standard library; the optional terminal panel needs `rich` (install in your own virtual environment). Clone the public `butler-agent-skill` repository and copy or symlink this folder as `butler` into your agent's skills directory. There is exactly one skill entrypoint, SKILL.md. You can also use the runtime without an agent.

With the skills CLI: `npx skills add https://github.com/AntreasAntoniou/butler-agent-skill --skill butler`. This installer requires Node/network access; inspect the repository before installing.

From the repository:

```sh
export BUTLER_ROOT="$PWD/.butler"
python3 scripts/butler.py init
python3 scripts/butler.py dashboard
python3 scripts/webui.py
```

Open http://127.0.0.1:8322 (change with `BUTLER_PORT`). Stop with Ctrl-C. Startup does not install a daemon, cron, provider adapter, or scheduler. Choose a dedicated private state directory outside the skill when installing it permanently. Initial `config.json` contains empty accounts and policy defaults; there are no sample projects or usage records. Do not use `init --force` against existing configuration unless you intend to replace it.

State writes create owner-only directories (0700) and atomically replace private files (0600), independently of the process umask. Append operations use a stable file lock and atomic replacement. An existing root is accepted only when empty or containing recognizable Butler state; home directories, the current working directory/ancestors, symlinked roots and mixed-use directories are refused without chmod. Pick a new dedicated directory instead of pointing BUTLER_ROOT at a repository or broad data folder. Existing dedicated state directories are tightened to 0700; touched files become 0600. Keep independent backups before migrating state. The browser rejects non-finite numbers, numeric booleans and arithmetic overflow before mutations; HTML responses include anti-framing and same-origin CSP headers. The retained UI still uses inline scripts/styles, so CSP is an additional boundary, not a claim of strict-script XSS prevention.

## Configure deliberately

Edit your private `$BUTLER_ROOT/config.json`: each account label maps to `weekly_weighted_budget`, `reset_dow` (Monday=0) and `reset_hour_utc`. These are user-calibrated **Claude weighted-token estimates**, not actual Codex quota. No budgets are invented at install. Register your own project using `register --project SLUG --root /absolute/project --weekly-pct PERCENT`; use `--gpu-day`, `--gpu-week`, `--gpu-month` for explicit GPU-hour ceilings. The CLI help lists all parameters.

By default no home transcripts, provider cache or local processes are read. To opt in, set `BUTLER_CLAUDE_PROJECTS` to the transcript directory and optionally `BUTLER_CLAUDE_CACHE` to a Claude usage-cache JSON file. Scans stay scoped to registered project roots. `show_session_topics` and `inspect_local_processes` in private config separately enable sensitive previews. No data is sent anywhere by these local scans. The explicit `collect` CLI command is an optional SSH adapter for machines you configure; it scans their Claude transcript directory and stores aggregated snapshots locally. It is disabled from the browser and requires separate authorization. No machine configuration is shipped.

## How accounting works

`gate` checks local token policy; `gpu-gate` previews GPU admission without reserving. `gpu-reserve` locks the ledger, checks projected GPU-hours/concurrency/cost/disk commitments, and appends an idempotent hold. `gpu-reconcile` replaces that hold with measured actual usage; exact retries are no-ops and conflicting retries fail. `gpu-import-usage` records provider-evidenced retrospective usage. [Accounting details](references/accounting.md) explain constraints and limitations.

The web UI supports local project allocation, status, event and usage entry. It never launches compute. Ordinary configuration edits across CLI and web are not a cross-process transactional API; serialize policy changes. GPU reservations use a cross-process lock. Token gates do not reserve tokens.

## Trust and verification

This is a single-user local service, not a provider-enforced spending cap. Cached provider usage can be stale; no actual Codex quota adapter is included. A caller may ignore an advisory gate. Missing GPU ceilings are unbounded, so set them before launching compute. Monetary units must be consistent; no FX conversion occurs. State remains private and is not included in this repository.

Run `python3 -m unittest discover -s tests -v`. Tests use synthetic temporary ledgers and ephemeral loopback servers, covering atomic reservation races, reconciliation/idempotency, scopes, corruption rejection, empty bootstrap and HTTP security guards. See [SECURITY.md](SECURITY.md) for the local threat boundary. MIT licensed.
