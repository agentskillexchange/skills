---
name: "Nexus"
slug: "nexus"
description: "Map an unfamiliar repository, select task-relevant implementation and verification paths, and build a code-cited context pack for planning, debugging, review, or handoff."
category: "Developer Tools"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/nexus"
---

# Nexus

Reconstruct a repository in two passes: map broadly, then read selectively. Connect implementation, contracts, configuration, tests, and operational paths. A map is an inventory, not semantic understanding.

## Establish the task and snapshot

1. State the outcome, constraints, and non-goals. Resolve the explicit repository root or use `git rev-parse --show-toplevel`; label a non-Git directory honestly.
2. Read applicable repository instructions before inspecting scoped files. Record `git rev-parse HEAD` and `git status --short` when available. Preserve dirty changes.
3. Choose a context directory outside the repository by default. Treat its contents as private working material; source names alone can be sensitive. Sharing a portable pack requires an explicit disclosure boundary.

## Map broadly

Run the bundled `scripts/map_directory.py` using its installed absolute location, the authorized root, and a new output path:

```text
python3 <installed-skill>/scripts/map_directory.py <repository-root> <context-directory>/directory-map.md
```

The Python 3.10+ standard-library mapper lists paths and top-level Python functions/classes. It skips common generated/cache directories, hidden entries and sensitive filename patterns by default, never follows symlinks, bounds Python source reads, and refuses to overwrite an output. New map files use owner-only POSIX permissions. It parses Python but never executes repository code. Review `--help` to add task-specific exclusions with `--ignore-dir` and `--ignore-file`. Exclusions are risk reduction, not a secret detector: review the result before disclosure. The map omits function bodies, values, and string literals; even names may need redaction.

If mapping fails, report the exact failure. Do not silently present another tool's inventory as this mapper's output. Partial parsing failures are annotated without copying source or exception contents. Read the map entirely when practical; otherwise use line counts and chunked reads. Identify entry points, manifests, schemas, migrations, tests, docs, CI, deployment surfaces, and generated-code boundaries.

## Select zoom areas

Translate the task into a small set of investigation questions. Search the map and scoped repository using `rg` for task nouns, symbols, routes, configuration keys, errors, and tests. Select an area only when it:

- implements or invokes the target behavior;
- defines an interface, model, schema, policy, or configuration contract;
- verifies behavior in tests or operational checks; or
- controls a relevant build, migration, delivery, or runtime path.

For each area record why it matters, files/symbols, the question it answers, and its relation to other areas. Include implementation and verification paths when they exist. Do not broaden into adjacent subsystems just because they are interesting.

## Zoom in and trace behavior

Read the smallest coherent set answering the questions: authoritative overview/manifest → entry point/caller → implementation → interfaces/configuration → tests/fixtures → relevant operational path. Trace imports, calls, transformations, state changes, and configuration across boundaries.

Use line-numbered reads and cite repository-relative paths plus line ranges. Treat comments/docs as claims until corroborated. Do not read or reproduce secrets, credential stores, private keys, `.env` values, dependency caches, or unrelated generated artifacts. Do not execute unfamiliar repository code merely to map it. Tests or other executions need their own scope and side-effect assessment.

Stop expanding when questions are answered and the execution path is coherent; retain contradictions and unknowns. A static trace does not establish runtime correctness.

## Build and verify the context pack

Read [the context-pack template](references/context-pack-template.md) when composing the handoff. Write `context-pack.md`, `directory-map.md`, and `sources.txt` (ordered evidence paths, one per line) together at the chosen destination.

Separate observed facts, reasoned inferences, and open questions. Cite important claims, record revision and dirty-worktree caveat, explain only task-relevant architecture, name the likely change surface without claiming edits, derive validation commands from repository evidence, and explain exclusions. Quote only decisive snippets, not entire files.

Before handoff, verify that cited paths/lines still resolve at the recorded snapshot; the call/data flow is consistent; implementation, contracts, and verification are represented where available; the evidence manifest matches actual reads; and no secrets or unrelated private material entered the pack. Report map/context paths, selected areas, unknowns, and one recommended next action. Mapping is read-only apart from the requested local artifacts; it authorizes neither changes nor publication.

## Installation and upstream provenance

The upstream skill identifier is `nexus`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/nexus --skill nexus --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/nexus#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata, a matching display heading, and this installation section added. The source snapshot is [`910c34e7e03a`](https://github.com/AntreasAntoniou/nexus/tree/910c34e7e03aebadbb4fd8dc6e33769839a1fdd4). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
