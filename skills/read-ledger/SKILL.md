---
name: "Read Ledger"
slug: "read-ledger"
description: "Track research source and text-range coverage across contexts using JSONL snapshots, SHA-256 hashes, Unicode code-point offsets, and bounded resumable batches."
category: "Research & Scraping"
framework: "Codex"
verification: listed
source: "https://github.com/makoncline/read-ledger"
---

# Read Ledger

Read Ledger is a file-based workflow for Codex research tasks that span many source documents or multiple context windows. It uses an append-only JSONL ledger to keep source inventory, available text, and reported review coverage separately reconstructible. Source snapshots carry SHA-256 hashes of exact UTF-8 bytes, while review records identify end-exclusive ranges measured in Unicode code points. This combination lets a later context locate pending text without depending on conversation memory or treating a downloaded document as fully reviewed.

The workflow uses the agent's existing shell and language tools to parse records, hash files, slice bounded batches, and calculate interval coverage. It includes conventions for duplicate acknowledgments, overlapping dispositions, partial review, missing inputs, reopened ranges, and stale evidence after a source changes. Before resuming, the agent checks all local sources, including previously completed files. Review records are self-reported work evidence; they do not establish comprehension. The upstream repository supplies synthetic fixtures and an example ledger for inspecting the format.

## Installation

### Codex, project-local manual install

Run from the project where you want the skill available. Use a new destination so an existing installation remains intact:

```bash
mkdir -p .agents/skills
git clone --depth 1 https://github.com/makoncline/read-ledger.git .agents/skills/read-ledger
```

Then ask Codex to use `read-ledger` to inventory your supplied research files, review one bounded batch, and save a private `ledger.jsonl`. Keep that research ledger beside your source files, separate from the installed synthetic example.

### Optional third-party installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version and select Codex with project scope:

```bash
npm exec --package=skills@1.5.7 -- skills add makoncline/read-ledger --skill read-ledger
```

The canonical repository also supports the file-based workflow: give your agent its `SKILL.md` directly. An installer is optional.

Track which source text has been reviewed across batches. Keep `ledger.jsonl` beside the private research files. Use [example.jsonl](https://github.com/makoncline/read-ledger/blob/main/example.jsonl) only as a synthetic format example; start a new ledger for real work.

## Procedure

1. **Load.** Parse every complete JSONL line. Reject malformed records and conflicting reuse of a `review_id`; identical repeated review records count once. The last source record for each `source_id` selects its current snapshot. One coordinator appends records; workers return records to that coordinator. Finish with the current inventory and dispositions reconstructed from disk.

2. **Inventory.** Assign each intended source a stable ASCII `source_id` using letters, digits, `_` or `-`. Record its title and private locator. An entry awaiting content has `state: "not-started"`, `sha256: null`, and `chars: null`. For a supplied local UTF-8 file, hash the exact bytes with SHA-256 and count Unicode code points after decoding those bytes, preserving line endings and normalization. Record `state: "fetched"` only for available, nonempty text. Record empty, inaccessible, or invalid UTF-8 input as `blocked` with a reason; preserve a known hash/length or use null when unknown. Finish when every intended source has a record or an explicit inventory gap is reported.

3. **Batch.** Choose a character budget; default to 8,000 code points. Order fetched sources by `source_id`, then pending ranges by start offset. Take the earliest pending ranges until the combined text reaches the budget, splitting at the budget even inside a long paragraph. Emit each packet's `source_id`, current `sha256`, `[start,end)`, exact text, and ID `source_id:sha256:start-end`. Estimate tokens as `ceil(characters / 4)` and label that number an estimate. Missing content belongs in the remaining-work report. Finish with a reproducible packet within the budget; generating it records no review.

4. **Review.** Inspect the packet's actual text. Append a review record only for the range inspected, with a short finding or decision in `note` and relevant locators in `citations`. Record a partial range when interrupted or when tool output is truncated. Use `skipped` or `blocked` with a reason for other dispositions. To reopen a range, append a `fetched` disposition for that range. Finish with saved records for the work completed and an explicit next range. Review acknowledgments are self-reported evidence, not proof of understanding.

5. **Resume.** Reload the ledger and check every local source before selecting work, including sources previously marked fully reviewed. Rehash available files and append a source snapshot when bytes or availability changed. Record a missing file as blocked rather than retaining its fetched state. Retain older reviews as stale evidence; apply only reviews matching the current snapshot hash. Repeat Batch and Review from the earliest pending range. Finish when the next packet follows from saved records rather than conversation memory.

6. **Report.** Report inventory sources, fetched sources, fully reviewed sources, missing/blocked sources, and stale reviews separately. Count reviewed text as the union of current ranges whose effective disposition is `reviewed`. A source is fully reviewed only when its nonempty current text is entirely covered. Skipped, blocked, and pending ranges remain incomplete. Show reviewed characters / available characters, plus sources with unknown length; that denominator covers available text only. Export the ledger and exact next packet or remaining exceptions. Finish with counts reproducible from the saved ledger and the time its local snapshots were checked. Snapshot coverage does not establish that a remote original is still current. Publish only synthetic examples or separately authorized material.

## Record format

Each UTF-8 JSONL line is one object with `v: 1` and `kind: "source"` or `kind: "review"`. `at` is an ISO 8601 UTC timestamp. Append order determines precedence, rather than timestamps.

| Kind | Required fields |
| --- | --- |
| `source` | `source_id`, `title`, `locator`, `state` (`not-started`, `fetched`, `blocked`), `sha256` (64 lowercase hex characters or null), `chars` (nonnegative integer or null), `at`; `note` explains a blocked source. |
| `review` | `review_id` (stable ASCII identifier), `source_id`, `sha256`, `start`, `end`, `state` (`reviewed`, `skipped`, `blocked`, `fetched`), `reviewer` (label), `at`, `note` (nonempty), `citations` (array of strings). |

Review offsets are Unicode code points, zero-based, end-exclusive: `0 <= start < end <= chars` for the referenced fetched snapshot. A review must reference a known snapshot of that source. Keep `review_id` and its entire payload unchanged on retries. Overlapping current-hash dispositions use the last unique review record at each point; overlaps never multiply coverage. `fetched` reopens text as pending. Repeated source snapshots do not create additional sources. A changed hash makes previous-hash reviews stale, including previously complete ranges.

For local calculations, use the agent's existing shell or language tools. A UTF-8 byte hash, code-point slicing, interval union, and JSON parsing suffice; no service or model API is required.
