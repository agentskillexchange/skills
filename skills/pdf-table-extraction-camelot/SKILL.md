---
title: "PDF Table Extraction with Camelot"
description: "Extracts structured tables from PDF documents using Camelot’s lattice and stream parsing algorithms. Handles merged cells, multi-page tables, and outputs to pandas DataFrames, CSV, and JSON with column type inference."
verification: "security_reviewed"
source: "https://github.com/camelot-dev/camelot"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "camelot-dev/camelot"
  github_stars: 3673
---

# PDF Table Extraction with Camelot

The PDF Table Extraction skill leverages the Camelot library to accurately extract tabular data from PDF documents, handling complex layouts that defeat simpler regex-based approaches. It supports both lattice mode for tables with visible cell borders and stream mode for tables defined by whitespace alignment, automatically selecting the optimal strategy based on page analysis.

The skill handles common PDF table challenges including merged cells spanning multiple rows or columns, tables that flow across page boundaries, rotated text in header rows, and nested sub-tables. Extracted data is output as pandas DataFrames with automatic column type inference (numeric, date, currency, categorical), and can be serialized to CSV, JSON, Excel, or Parquet formats.

Advanced features include accuracy scoring per extracted table to flag low-confidence results for manual review, visual debugging overlays that show detected cell boundaries on the original PDF, batch processing of multi-page documents with table continuation detection, and OCR fallback via Tesseract for scanned PDF pages where text extraction returns empty results. The skill supports coordinate-based table region specification for precise extraction from known page layouts.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pdf-table-extraction-camelot/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pdf-table-extraction-camelot
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pdf-table-extraction-camelot`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pdf-table-extraction-camelot/)
