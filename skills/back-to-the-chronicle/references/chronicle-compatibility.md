# Public Chronicle compatibility

The optional integration targets [AntreasAntoniou/chronicle](https://github.com/AntreasAntoniou/chronicle),
whose public 2.0.0 CLI provides the verbs used here. This package does not bundle or
silently install Chronicle. Inventory and manifest validation work without it.

After separate installation approval, its documented install command is:
`pipx install 'git+https://github.com/AntreasAntoniou/chronicle.git'`.
Check `chron --help` and each needed subcommand on your installed version. Do not
install hooks, run narration, synchronize a spine, or assume capture coverage.

Run in the approved canonical project root. The integration is deliberately manual:
no bundled script appends a manifest automatically. A reviewed entry can be recorded
with `chron note "historical observation" --state "ARTIFACT-MEASURED; occurred_at=..."`
and `--stdin` for its reviewed body, including manifest key and source anchors.
Use `chron decision TITLE --why REASON --state STATE` only for witnessed choices.
For inferred notes, start state with `INFERRED - NOT WITNESSED - MAY BE WRONG`.
Chronicle's ordinary note command does not itself convert that prose into a typed
inferred flag; the warning must remain in the visible body as well.

`chron correct ENTRY_ID WHAT_WAS_WRONG --truth TRUTH --evidence ANCHOR` has a
different argument shape from ordinary entries. A manifest's `corrects` points
to the actual existing entry ID; never guess it. `chron experiment` accepts
`--hypothesis`, `--setup`, `--varied`, `--result`, `--conclusion` and
`--outcome`; report only measured values with their scope.

A present-day bulk-write ARM needs `--intent`, `--class`, `--restore` and
`--verified`. For append-only history, restoration means a tested correction or
supersession procedure, not rewriting the past. Never claim it was tested when it
was only proposed. If you cannot meet the installed CLI's requirements, keep the
manifest as a proposal and report the missing prerequisite.

Even read-oriented commands can update Chronicle's derived local index. Keep its
ledger and generated CHRONICLE.md private unless a separately reviewed public
derivative is authorized. Backfill cannot establish historical hook coverage.
