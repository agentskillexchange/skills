# Backfill evidence standard

## Purpose

Use this standard to prevent a polished retrospective from becoming more
authoritative than the evidence it summarizes.

## Source priority

1. Raw first-hand record: a project-related Codex or Claude session JSONL event
   containing the user instruction, or a contemporaneous witnessed Chronicle
   decision.
2. Immutable or append-only artifact: commit, content hash, provider receipt,
   CONTROL/event ledger, signed or generation-pinned object.
3. Direct measurement: tool output in a raw session JSONL, test output, model
   result, or process/provider readback, subject to truncation and exit status.
4. Curated programme record: research logbook, handoff, architecture document.
5. Session summary, transcript reconstruction, or memory index.
6. Agent inference or unverified assistant assertion.

Lower-priority sources may locate evidence but must not silently override a
higher-priority contradiction.

Priority applies claim by claim. A user prompt in a raw JSONL is first-hand
evidence of authority or intent; a tool call is evidence of an attempt; a tool
result is evidence of the returned observation; assistant prose is only a
contemporaneous assertion unless another anchor verifies it.

## Claim rules

- Attach at least one anchor to every entry; use two independent anchors for
  external publication, deletion, migration, or headline experimental results.
- Keep timestamps absolute and UTC. Preserve both event time and backfill time.
- Preserve exact independent seed counts, parameter counts, exposure units,
  architecture identity, checkpoint identity, and evaluation contract for ML
  results when available.
- A missing field remains missing. Do not backfill it from a neighbouring run.
- Distinguish current readback from historical state.
- Preserve failed attempts even when a later retry succeeded.
- A green static test is implementation evidence, not live provider evidence.

## Inference caveat

Every inferred-intent entry must contain this semantic warning, even if the
exact typography differs:

> INFERRED - NOT WITNESSED - MAY BE WRONG. Reconstructed from named anchors;
> verify those anchors before acting. First-hand evidence wins on conflict.

For machine-validated manifests, begin the `caveat` string with the exact words
`INFERRED - NOT WITNESSED - MAY BE WRONG` (case-insensitive); put explanatory text
after that prefix. A lone "INFERRED" label is insufficient.

An inferred entry cannot certify authority, approval, destructive safety,
publication permission, experiment success, or session closure.

## Granularity

Create an entry when it changes at least one of:

- the project's authority or intent;
- the chosen architecture or rejected alternative;
- what evidence supports a scientific or operational claim;
- the state of an external resource;
- the recovery path;
- the next discriminating action.

Do not create entries merely because a file or commit exists; the automatic
trace already records that.

## Required adversarial pass

Before appending, ask:

1. What failed before the surviving path?
2. Which result is single-seed, confounded, partial, or incomparable?
3. Which external state may have drifted?
4. What did the session claim but never verify?
5. Which artifact is known missing?
6. What would a future agent accidentally retry or overclaim without this
   entry?
