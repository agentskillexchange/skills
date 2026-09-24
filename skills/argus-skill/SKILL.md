---
name: "Argus"
slug: "argus-skill"
description: "Preserve durable context from conversations and completed work by routing commitments, evidence, decisions, preferences, and project state to their canonical Git-backed records. Use when the user asks to archive, remember, checkpoint, capture context, update an Archivum-style workspace, or close the loop; also use at natural milestones when workspace instructions require durable-state capture."
category: "Templates & Workflows"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/argus-skill"
---

# Argus

Keep a hundred eyes on the live context, but preserve only the delta that should outlive it. Do not archive the conversation itself.

## Run one checkpoint

1. Identify durable changes only:
   - explicit decisions, corrections, and stable preferences;
   - promises, deadlines, waiting-on states, and changed priorities;
   - project state, evidence, results, blockers, and next actions;
   - reusable methods, sources, and outputs.
2. Exclude unselected brainstorming, conversational filler, duplicated summaries, unsupported claims, and secrets outside their authorised store.
3. Discover the home registry and candidate archives:

   ```bash
   python3 scripts/discover_archivums.py --json
   ```

   Resolve `scripts/` relative to this installed skill. Prefer an explicit
   `--registry`, then `ARCHIVUM_REGISTRY`, then
   `$ARCHIVUM_HOME/00_meta/archivum_registry.toml`. If no registry resolves the
   choice and several archives remain plausible, ask rather than guess.
4. Route each delta using [routing.md](references/routing.md). One checkpoint may update several surfaces, but each fact has one canonical owner.
5. For commitment-shaped state, use the workspace's configured commitment system rather than inventing a parallel ledger. Read its contract before mutation.
6. For resource-shaped state or substantial autonomous work, use the configured budget authority rather than creating a second resource ledger. Gate expensive work and record actual usage where that system requires it.
7. In each selected Archivum, read its agent contract and `config.yaml`, then load only the bounded core context and record needed for the delta. Inspect its worktree and search before creating.
8. Apply the bidirectional home-anchor contract in [backlink-contract.md](references/backlink-contract.md). Every private satellite record must remain reachable from the home Archivum and link back to its home anchor.
9. Verify changed files, links, schema or ledger checks, and relevant tests. Commit only where the archive contract or user requires it. Never publish, send, submit, or disclose merely because capture is complete.
10. Report the durable records changed, surfaces intentionally untouched, and one next action if work remains.

## Route by ownership, not keywords

- **Commitment system:** promises, deadlines, waiting on people, and current workstream custody.
- **Budget authority:** token and GPU budgets, account windows, autonomous-run gates, session histories, and artefact custody.
- **Home Archivum:** cross-domain projects, identity, relationships, personal decisions, stable preferences, and the cross-archive index.
- **Research Archivum:** hypotheses, literature, experiments, results, methods, and scientific strategy.
- **Admin Archivum:** company operations, governance, finance, legal, people operations, and internal administration.
- **Career archive:** role research, applications, evidence packets, and pipeline state.
- **Existing specialist Archivum:** use when the project already has a canonical domain store.
- **New Archivum:** propose only for a distinct audience, permission boundary, owner, or lifecycle. Never create one silently.

Read [routing.md](references/routing.md) whenever a delta spans domains or has more than one plausible owner.

## Respect each Archivum's configured layout

Treat a version-2 workspace's `config.yaml` as the authoritative path map. Resolve `workspace.profile_file`, `workspace.state_file`, `workspace.schema_file`, `directories.*`, and `canonical_files.*` from that file before reading or writing. Never assume numbered directory names such as `01_projects`; the research Archivum, for example, maps projects to `01_active_research`.

Read the selected archive's `AGENTS.md` first when present, then its configured profile, state, and schema only as needed. Prefer the archive-local `archivum` CLI for deterministic creation, status, and doctor checks when available. For a legacy workspace without version-2 configuration, inspect its existing structure and preserve it; do not migrate it unless the user requested migration.

## Keep the watcher quiet

- Run once after a meaningful milestone or before ending work that changed durable state.
- Batch related deltas; never checkpoint after every edit or tool call.
- Do not recursively archive the mechanical fact that Argus updated an archive.
- If nothing durable changed, make no write and say nothing about capture.
- Treat a checkpoint as preservation authority, not permission to broaden scope or perform unrelated external actions.

Use [checkpoint-prompt.md](references/checkpoint-prompt.md) to make Argus available automatically in repository-aware agents.

## Validate the archive graph

```bash
python3 scripts/discover_archivums.py --registry /path/to/00_meta/archivum_registry.toml --json
python3 scripts/check_backlinks.py --registry /path/to/00_meta/archivum_registry.toml
```

Both scripts are read-only. Discovery also reports each Archivum's configuration version and available agent contracts. Backlink validation rejects logical paths that escape their registered archive root.

## Installation and upstream provenance

The upstream skill identifier is `argus`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/argus-skill --skill argus --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/argus-skill#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`76184070c296`](https://github.com/AntreasAntoniou/argus-skill/tree/76184070c29682fa27a26b1df476acbc947d3d7b). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
