---
title: "Create, repair, and recalculate spreadsheet workbooks without breaking formulas"
slug: "create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas"
description: "Use the Anthropic xlsx skill when an agent needs to create, clean up, or modify .xlsx, .xlsm, .csv, or .tsv files as spreadsheet deliverables, not just inspect tabular data. It pushes the agent toward formula-safe edits, workbook validation, and recalculation instead of hardcoded outputs or one-off scripts."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/xlsx"
author: "Anthropic"
publisher_type: "official_repository"
category: "Data Extraction & Transformation"
framework: "Claude Agents"
---

# Create, repair, and recalculate spreadsheet workbooks without breaking formulas

Use the Anthropic xlsx skill when an agent needs to create, clean up, or modify .xlsx, .xlsm, .csv, or .tsv files as spreadsheet deliverables, not just inspect tabular data. It pushes the agent toward formula-safe edits, workbook validation, and recalculation instead of hardcoded outputs or one-off scripts.

## Prerequisites

pandas, openpyxl, LibreOffice

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use the upstream Anthropic xlsx skill from the anthropics/skills repository in an agent environment that can access spreadsheet tooling and LibreOffice for recalculation.
```

## Documentation

- https://github.com/anthropics/skills/tree/main/skills/xlsx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas/)
