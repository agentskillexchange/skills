---
name: "Archivum"
slug: "archivum"
description: "Operate a Git-backed Archivum as durable agent memory for projects, research, decisions, meetings, tasks, sources, and outputs. Use when the user asks to capture, find, connect, update, audit, or resume work in an Archivum, or to initialize an Archivum workspace. Do not use merely because a repository contains Markdown."
category: "Templates & Workflows"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/archivum"
---

# Archivum

Make useful work survive the conversation. Search before creating, preserve evidence and maturity, and write durable state back to the correct record.

## Resolve the workspace

Use this order:

1. Use a path the user explicitly supplied.
2. Use `ARCHIVUM_ROOT` when set.
3. From the current directory, walk upward for both `config.yaml` and `00_meta/`.
4. If several Archivums are plausible, show the candidates and ask which one. Never guess.

If no Archivum exists and the user asks to create one, initialize from `https://github.com/AntreasAntoniou/archivum`. Do not clone or create a workspace without permission.

## Orient with bounded context

1. Read `AGENTS.md` when present.
2. Read `00_meta/workspace_profile.md`, `00_meta/workspace_state.md`, and `config.yaml`.
3. Inspect `git status --short` and preserve unrelated changes.
4. Run `archivum status` when available, or inspect recent files and active projects directly.
5. Search with `rg` or `rg --files`; load only records relevant to the request.

Do not recursively read the whole archive as an initialization ritual. Large Archivums must remain usable without fitting into one context window.

## Think independently

- Treat the user's framing as context, not automatic ground truth.
- Do not spend words agreeing, praising, or restating. Reframe, synthesize, challenge, or add evidence.
- Distinguish the literal request from the desired outcome. Complete safe, reversible adjacent work when necessary; offer materially broader, external, or authority-changing steps instead of silently taking them.
- Identify the disputed assumption when you disagree and suggest the cheapest discriminating check.
- Say when the archive does not support a strong view. Never fill an evidence gap with confidence.

## Adapt to the user and task

- Read the user's expertise, preferred explanation depth, working style, accessibility needs, and quality bar from `00_meta/workspace_profile.md`.
- Match their technical altitude. Use and blend engineering, research, writing, reflection, and project-delivery stances as the work requires.
- Treat work stances as lenses, not personas with invented experience, credentials, memories, or authority. The user may say `Activate <stance>`, but explicit activation is not required.
- For changing software choices, inspect the environment and verify compatibility with primary documentation; do not equate newest with most robust.
- When full code is requested, provide a complete runnable implementation or identify every omission and blocker.

## Learn durably

- Write stable, explicit user preferences to `00_meta/workspace_profile.md`. Write project-specific corrections and lessons to the smallest canonical record.
- Do not infer a lasting preference from one ambiguous interaction, and do not claim learning or memory unless a durable record changed.
- Preserve superseded preferences and rationale when they may affect future decisions.
- Ask for focused feedback at meaningful decision or review points, not as a periodic ritual.

## Select the operation

### Find or answer

- Search titles, tags, frontmatter, aliases, and body text.
- Prefer canonical records and primary sources over later summaries.
- Answer with repository-relative source paths.
- Distinguish what the archive states from your inference.
- Do not mutate the workspace unless the user also asked to capture or update something.

### Capture

- Search for an existing canonical record first.
- Route the content using `00_meta/schema.md` and a template from `00_meta/templates/`.
- Default to `visibility: private`.
- Preserve quotation, paraphrase, observation, and inference as different things.
- Add source URLs or repository-relative paths.
- Use `archivum new <kind> "<title>"` when available.

### Update or connect

- Edit the smallest canonical record that can own the new state.
- Preserve `created_date`; update `last_updated_date` with the actual date.
- Link related records instead of duplicating prose.
- Preserve authorship and mark AI-assisted synthesis when attribution matters.
- Never promote an idea to a result or a result to established fact without linked evidence.

### Resume a project

- Read the project's `README.md`, `tasks.md`, latest logbook entries, and directly relevant experiment or decision records.
- Report current state, strongest evidence, blockers, and the next meaningful action.
- If work continues, append a dated logbook entry and update task/state records only when reality changed.

### Record research

- Keep question, mechanism, design, observation, interpretation, and decision separate.
- Use `maturity: seed | proposal | in-progress | observed | validated | retired`.
- Record contradictory, null, negative, or inconclusive evidence when it changes belief or action.
- Attach code, data, configuration, and artefact paths where available.
- State the narrowest claim supported by the evidence and what remains unestablished.

### Process a meeting or conversation

- Preserve the source or stable pointer.
- Extract decisions with rationale, actions with owners and dates, unresolved questions, and changed project state.
- Promote durable decisions to decision records and link back to the meeting.
- Do not manufacture consensus from silence or ambiguity.

### Prepare an output

- Trace material claims to source records.
- Label proposals, implementations, observations, and results accurately.
- Keep authorship and AI assistance honest.
- Treat `visibility: public` as permission metadata, not authorization to publish.
- Never send, upload, submit, or publish without explicit approval.

## Delegate without context loss

Use workers only when decomposition, parallelism, specialist review, or long-running execution materially helps. A dispatch must be self-contained: objective and stop condition; workspace and canonical source paths; allowed writes; dirty-worktree, privacy, evidence, and external-action constraints; expected artefacts; validation; and failure handling.

Keep one integration owner. Avoid concurrent edits to the same canonical record unless isolation and merge ownership are explicit. A worker report is evidence to inspect, not proof of completion.

## Close durable work

1. Inspect and integrate any delegated outputs; reconcile contradictions and preserve useful partial work.
2. Verify the requested outcome in the environment where it must hold.
3. Review the relevant diff.
4. Update tasks, decision records, and `00_meta/workspace_state.md` only when the underlying state changed.
5. Run focused checks and `archivum doctor` after structural edits when available.
6. Report changed paths, evidence boundaries, unresolved questions, and the next meaningful action if incomplete.

Do not turn the state file into a transcript of agent activity. The archive records the work, not the chat.

## Installation and upstream provenance

The upstream skill identifier is `archivum`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/archivum --skill archivum --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/archivum#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`97485ef1f149`](https://github.com/AntreasAntoniou/archivum/tree/97485ef1f149fc56a8b8843b7bdcf1b9ad47c877). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
