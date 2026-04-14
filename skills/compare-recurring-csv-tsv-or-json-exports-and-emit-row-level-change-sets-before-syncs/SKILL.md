---
title: "Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs"
description: "Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON."
verification: security_reviewed
source: "https://github.com/simonw/csv-diff"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/csv-diff"
  github_stars: 330
---

# Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs

Tool: csv-diff by Simon Willison.

This skill gives an agent a reliable way to compare two structured snapshots and turn them into an actionable change report. The upstream tool accepts CSV, TSV, and JSON inputs, aligns rows by a user-supplied key, and emits exactly what changed: rows added, rows removed, columns added or removed, and field-level edits for rows that still exist. That makes it well suited to operational checks around vendor exports, nightly data pulls, pricing tables, inventories, CRM dumps, and other recurring feeds that agents need to validate before pushing updates elsewhere.

Invoke this when the real task is change detection, review, or gating. If an agent is preparing a sync, writing a summary of what changed since yesterday, checking whether a source export is safe to import, or generating a machine-readable delta for another workflow, csv-diff is a better fit than opening the files manually or using a generic text diff. Text diffs are noisy for tabular data. This skill stays focused on records and values.

The scope boundary is important. This is not a generic spreadsheet product listing and it is not a full ETL platform. It does one job: compare two structured tabular or object-array snapshots using a stable key and produce a row-level delta. If you need transforms, warehousing, or live database replication, use something else.

Integration points are simple. Agents can run it as a CLI for human-readable summaries, use the JSON output for downstream automations, or import the Python library directly into a larger pipeline. The only real prerequisite is having two comparable exports and knowing which column or field should act as the durable key.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs/)
