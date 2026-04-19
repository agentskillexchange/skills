---
title: "Create, repair, and recalculate spreadsheet workbooks without breaking formulas"
description: "The upstream tool here is Anthropic&#8217;s xlsx skill from the anthropics/skills repository. This entry is not a generic spreadsheet product card. It describes a bounded agent workflow: create, repair, restructure, and recalculate spreadsheet workbooks while preserving formulas, formatting intent, and deliverable quality. The agent behavior is concrete. It should pick spreadsheet-native operations, use formulas instead of hardcoded computed values, recalculate the workbook after edits, and verify that the file ships without Excel errors like #REF! , #DIV/0! , or broken cross-sheet references. Invoke this skill when the user wants the output to be a spreadsheet file or wants an existing workbook fixed. Good fits include adding columns, cleaning malformed rows, rebuilding formulas, standardizing assumptions, exporting structured data into Excel, or rescuing a model that was damaged by unsafe edits. This is the right path when a normal product workflow would leave the user manually rebuilding formulas or checking every tab by hand. The scope boundary matters. This is not a listing for Excel, pandas, or a generic data library. It is also not the right skill when the real deliverable is a dashboard, database pipeline, HTML report, or Google Sheets integration. The job-to-be-done is specifically workbook-safe agent execution. Integration points include Python data tooling such as pandas and openpyxl, LibreOffice-based recalculation, CSV/TSV ingestion, and downstream export to finished spreadsheet artifacts."
source: "https://github.com/anthropics/skills/tree/main/skills/xlsx"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116918
---

# Create, repair, and recalculate spreadsheet workbooks without breaking formulas

The upstream tool here is Anthropic&#8217;s xlsx skill from the anthropics/skills repository. This entry is not a generic spreadsheet product card. It describes a bounded agent workflow: create, repair, restructure, and recalculate spreadsheet workbooks while preserving formulas, formatting intent, and deliverable quality. The agent behavior is concrete. It should pick spreadsheet-native operations, use formulas instead of hardcoded computed values, recalculate the workbook after edits, and verify that the file ships without Excel errors like #REF! , #DIV/0! , or broken cross-sheet references. Invoke this skill when the user wants the output to be a spreadsheet file or wants an existing workbook fixed. Good fits include adding columns, cleaning malformed rows, rebuilding formulas, standardizing assumptions, exporting structured data into Excel, or rescuing a model that was damaged by unsafe edits. This is the right path when a normal product workflow would leave the user manually rebuilding formulas or checking every tab by hand. The scope boundary matters. This is not a listing for Excel, pandas, or a generic data library. It is also not the right skill when the real deliverable is a dashboard, database pipeline, HTML report, or Google Sheets integration. The job-to-be-done is specifically workbook-safe agent execution. Integration points include Python data tooling such as pandas and openpyxl, LibreOffice-based recalculation, CSV/TSV ingestion, and downstream export to finished spreadsheet artifacts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas/)
