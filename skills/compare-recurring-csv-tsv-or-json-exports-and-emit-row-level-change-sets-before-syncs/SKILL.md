---
title: "Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs"
description: "Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON."
verification: listed
source: "https://github.com/simonw/csv-diff"
tool_ecosystem:
  github_repo: "simonw/csv-diff"
  github_stars: 330
---

# Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs

Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs/)
