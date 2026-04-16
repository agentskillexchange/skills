---
title: "Tabula PDF Table Extractor"
description: "Extracts structured tables from PDF documents using Tabula-java with lattice and stream detection modes. Outputs to CSV, JSON, or pandas DataFrames with automatic column type inference via python-tabula."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tabula-pdf-table-extractor/"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
---

# Tabula PDF Table Extractor

The Tabula PDF Table Extractor specializes in high-accuracy table extraction from PDF documents using the tabula-java library accessed through the python-tabula (tabula-py) wrapper. It handles both lattice-based tables (with visible gridlines) and stream-based tables (whitespace-aligned columns).


The skill automatically analyzes each PDF page to determine the optimal extraction method — lattice mode for ruled tables and stream mode for borderless tables. Custom extraction areas can be specified using coordinate-based regions when automatic detection fails, with a visual preview mode that highlights detected table boundaries.


Post-extraction processing includes automatic column type inference (numeric, date, currency, percentage, text), header row detection and normalization, merged cell handling, and multi-page table concatenation. Output formats include CSV with proper escaping, JSON with nested structures, and pandas DataFrame objects for direct analytical use.


Batch processing supports directory scanning with file filtering, parallel extraction using concurrent.futures, and progress tracking. Integration with OpenPyXL enables direct Excel output with formatted headers, auto-sized columns, and conditional formatting for numeric data.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tabula-pdf-table-extractor/)
