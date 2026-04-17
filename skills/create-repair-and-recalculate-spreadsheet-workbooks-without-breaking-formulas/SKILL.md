---
title: "Create, repair, and recalculate spreadsheet workbooks without breaking formulas"
description: "The upstream tool here is Anthropic’s xlsx skill from the anthropics/skills repository. This entry is not a generic spreadsheet product card. It describes a bounded agent workflow: create, repair, restructure, and recalculate spreadsheet workbooks while preserving formulas, formatting intent, and deliverable quality. The agent behavior is concrete. It should pick spreadsheet-native operations, use formulas instead of hardcoded computed values, recalculate the workbook after edits, and verify that the file ships without Excel errors like #REF!, #DIV/0!, or broken cross-sheet references.\nInvoke this skill when the user wants the output to be a spreadsheet file or wants an existing workbook fixed. Good fits include adding columns, cleaning malformed rows, rebuilding formulas, standardizing assumptions, exporting structured data into Excel, or rescuing a model that was damaged by unsafe edits. This is the right path when a normal product workflow would leave the user manually rebuilding formulas or checking every tab by hand.\nThe scope boundary matters. This is not a listing for Excel, pandas, or a generic data library. It is also not the right skill when the real deliverable is a dashboard, database pipeline, HTML report, or Google Sheets integration. The job-to-be-done is specifically workbook-safe agent execution. Integration points include Python data tooling such as pandas and openpyxl, LibreOffice-based recalculation, CSV/TSV ingestion, and downstream export to finished spreadsheet artifacts."
verification: security_reviewed
source: "https://github.com/anthropics/skills/tree/main/skills/xlsx"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116918
---

# Create, repair, and recalculate spreadsheet workbooks without breaking formulas

The upstream tool here is Anthropic’s xlsx skill from the anthropics/skills repository. This entry is not a generic spreadsheet product card. It describes a bounded agent workflow: create, repair, restructure, and recalculate spreadsheet workbooks while preserving formulas, formatting intent, and deliverable quality. The agent behavior is concrete. It should pick spreadsheet-native operations, use formulas instead of hardcoded computed values, recalculate the workbook after edits, and verify that the file ships without Excel errors like #REF!, #DIV/0!, or broken cross-sheet references.
Invoke this skill when the user wants the output to be a spreadsheet file or wants an existing workbook fixed. Good fits include adding columns, cleaning malformed rows, rebuilding formulas, standardizing assumptions, exporting structured data into Excel, or rescuing a model that was damaged by unsafe edits. This is the right path when a normal product workflow would leave the user manually rebuilding formulas or checking every tab by hand.
The scope boundary matters. This is not a listing for Excel, pandas, or a generic data library. It is also not the right skill when the real deliverable is a dashboard, database pipeline, HTML report, or Google Sheets integration. The job-to-be-done is specifically workbook-safe agent execution. Integration points include Python data tooling such as pandas and openpyxl, LibreOffice-based recalculation, CSV/TSV ingestion, and downstream export to finished spreadsheet artifacts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas/)
