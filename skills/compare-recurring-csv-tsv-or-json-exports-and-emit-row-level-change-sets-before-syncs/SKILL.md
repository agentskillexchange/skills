---
title: "Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs"
slug: "compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs"
description: "Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON."
verification: "security_reviewed"
source: "https://github.com/simonw/csv-diff"
author: "Simon Willison"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/csv-diff"
  github_stars: 330
---

# Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs

Use csv-diff when an agent needs to explain what changed between two structured exports, not just that the files differ. The agent lines records up by a stable key, reports added, removed, and changed rows, and can hand the result to humans or downstream automations as readable text or machine-friendly JSON.

## Prerequisites

Python 3, pip, two comparable CSV, TSV, or JSON snapshots, and a stable key column or field.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install csv-diff
```

## Documentation

- https://github.com/simonw/csv-diff

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs/)
