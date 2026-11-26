---
name: "ML Run Provenance"
slug: "ml-run-provenance"
description: "Design or audit self-describing ML run metadata attached at initialization, including intent, code and data identity, resume lineage, and evidence limits. Use when wiring a tracker, introducing a run naming pattern, or investigating why a run exists."
category: "Developer Tools"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/ml-run-provenance"
---

# ML Run Provenance

Treat provenance as a trainer output alongside checkpoints and metrics. A cryptic run directory or dashboard title does not preserve campaign intent. Capture context at run birth and distinguish recorded facts from reconstructed metadata.

This package provides a protocol and a local JSON validator, **not** a trainer integration, tracker adapter, classifier, backfill service, or guarantee of reproducibility. Those project-specific pieces must be implemented and tested where needed. No other private repository or skill is required.

## Metadata contract

Read [the schema reference](references/metadata-contract.md) when creating or validating a record. The core is:

- Identity: stable unique `run_id`, `created_at`, `phase`, `variant`, `modality`, and `seed`.
- Intent: a concrete `dataset` description, one-sentence `reason`, and Markdown `notes` linking the authorized proposal, config, prior results, and parent campaign when available.
- Code: `repo_url`, `branch`, `commit`, `dirty`, `commit_url`, and `code_snapshot`. A commit is insufficient when the worktree is dirty; a link is not proof an object is accessible or was executed.
- Execution inputs: resolved `config` identity, `data` identity and preprocessing/tokenizer information; hashes need algorithms and immutable artifacts, not just filenames.
- Evidence: `metadata_origin` (birth or backfill), `recorded_at`, `missing`, and `tags`. Unknown facts are null and named in `missing`; never invent historical values.

Use local identifiers/nulls where repository URLs or data must remain private. Do not upload source paths, internal links, dataset samples, secrets, or resolved secret configuration to a third-party tracker without an appropriate disclosure boundary. Redaction and artifact hashes belong in the record when relevant.

## Classify once, attach at initialization

The reusable architecture is:

1. A project-local `run_context.py` is the source of truth for approved run-name patterns and curated metadata.
2. A pure `classify(run_name)` returns structured context. Unknown names return explicit unknowns and a diagnostic, not a confident guessed classification. Do not let a permissive fallback silently make provenance look complete.
3. An idempotent `attach_run_context(logger, context, resolved_config)` merges only fields/tags it owns and preserves unrelated user notes. The project adapter is optional until integration is requested.
4. At logger initialization, classify and supply metadata before the first logged training step. Capture code/config identity once per execution attempt. On resume, read back tracker state, preserve original birth facts, and append an attempt with current code/config/checkpoint identities. Do not assume every provider applies initialization fields on resume.
5. A backfill tool, if needed, reuses the classifier/attachment logic. It first previews an exact diff, labels reconstructed metadata and its sources, and applies only authorized fields to exact run IDs. Never overwrite unknown historical commits with today's checkout.

Keep human-readable names separate from unique execution IDs. A shape such as `<phase>_<size>-<variant>_seed<N>` is useful, but phase/variant/seed need not uniquely identify retries. Do not rename existing directories or delete tracker records merely to enforce a convention. Provider-specific ID/reuse behavior must be verified before relying on it.

## New project, extension, or audit

- New project: agree naming and metadata ownership; implement the pure classifier and adapter only if requested; validate the record; test an authorized short run; read back local and remote fields before an expensive campaign.
- New pattern: add a table-driven classifier test, preview classification across authorized run names, and check unknown-name handling. A tag rename is a migration proposal, not permission for campaign-wide backfill.
- Existing campaign: slice by phase/variant/dataset/seed and inspect missing fields. Diagnose missing provenance; it may reflect failed writes, old code, permissions, or a different naming pattern. Do not assume a cause or backfill automatically.

Use `python3 <installed-skill>/scripts/validate_metadata.py <record.json>` for a local shape/consistency check. `--strict` additionally requires core provenance fields to be non-null. Passing checks cannot prove timestamps, hashes, dataset permissions, tracker attachment, or that a recorded commit produced a result. Verify those against actual artifacts and tracker readback.

## Progress is part of observability

Long-running loops should expose total/current/rate/ETA/elapsed when meaningful. Unknown-length work still needs count/rate/elapsed. Use timestamped, rate-limited discrete log lines for redirected output; terminal carriage-return bars can corrupt logs. Framework progress hooks or a small compatible library may suffice; do not install an observability stack just for this convention.

Record stage, last successful operation, output/checkpoint identity, failures, and completion separately. A progress bar is not a liveness proof: interpret log advance together with output growth and device activity. Idle devices or static logs alone do not prove a hang.

## Handoff and trust boundary

Report which pieces exist (protocol, classifier, adapter, backfill), checks actually run, fields verified at initialization/resume, unresolved gaps, and exact artifact paths. Local validation is not tracker integration; integration is not a reproduced experiment. No paid runs, uploads, provider writes, deletions, or global metadata migration follow from invoking this skill alone.

## Installation and upstream provenance

The upstream skill identifier is `ml-run-provenance`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/ml-run-provenance --skill ml-run-provenance --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/ml-run-provenance#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata, a matching display heading, and this installation section added. The source snapshot is [`da8be7e25830`](https://github.com/AntreasAntoniou/ml-run-provenance/tree/da8be7e258307f13a7a3174f2437a5c75bd4bb88). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
