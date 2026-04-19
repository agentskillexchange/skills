---
title: "Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs"
description: "Tool: csv-diff by Simon Willison. This skill gives an agent a reliable way to compare two structured snapshots and turn them into an actionable change report. The upstream tool accepts CSV, TSV, and JSON inputs, aligns rows by a user-supplied key, and emits exactly what changed: rows added, rows removed, columns added or removed, and field-level edits for rows that still exist. That makes it well suited to operational checks around vendor exports, nightly data pulls, pricing tables, inventories, CRM dumps, and other recurring feeds that agents need to validate before pushing updates elsewhere. Invoke this when the real task is change detection, review, or gating. If an agent is preparing a sync, writing a summary of what changed since yesterday, checking whether a source export is safe to import, or generating a machine-readable delta for another workflow, csv-diff is a better fit than opening the files manually or using a generic text diff. Text diffs are noisy for tabular data. This skill stays focused on records and values. The scope boundary is important. This is not a generic spreadsheet product listing and it is not a full ETL platform. It does one job: compare two structured tabular or object-array snapshots using a stable key and produce a row-level delta. If you need transforms, warehousing, or live database replication, use something else. Integration points are simple. Agents can run it as a CLI for human-readable summaries, use the JSON output for downstream automations, or import the Python library directly into a larger pipeline. The only real prerequisite is having two comparable exports and knowing which column or field should act as the durable key."
source: "https://github.com/simonw/csv-diff"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/csv-diff"
  github_stars: 330
---

# Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs

Tool: csv-diff by Simon Willison. This skill gives an agent a reliable way to compare two structured snapshots and turn them into an actionable change report. The upstream tool accepts CSV, TSV, and JSON inputs, aligns rows by a user-supplied key, and emits exactly what changed: rows added, rows removed, columns added or removed, and field-level edits for rows that still exist. That makes it well suited to operational checks around vendor exports, nightly data pulls, pricing tables, inventories, CRM dumps, and other recurring feeds that agents need to validate before pushing updates elsewhere. Invoke this when the real task is change detection, review, or gating. If an agent is preparing a sync, writing a summary of what changed since yesterday, checking whether a source export is safe to import, or generating a machine-readable delta for another workflow, csv-diff is a better fit than opening the files manually or using a generic text diff. Text diffs are noisy for tabular data. This skill stays focused on records and values. The scope boundary is important. This is not a generic spreadsheet product listing and it is not a full ETL platform. It does one job: compare two structured tabular or object-array snapshots using a stable key and produce a row-level delta. If you need transforms, warehousing, or live database replication, use something else. Integration points are simple. Agents can run it as a CLI for human-readable summaries, use the JSON output for downstream automations, or import the Python library directly into a larger pipeline. The only real prerequisite is having two comparable exports and knowing which column or field should act as the durable key.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs/)
