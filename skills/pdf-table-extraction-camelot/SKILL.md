---
title: "PDF Table Extraction with Camelot"
description: "Extracts structured tables from PDF documents using Camelot’s lattice and stream parsing algorithms. Handles merged cells, multi-page tables, and outputs to pandas DataFrames, CSV, and JSON with column type inference."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pdf-table-extraction-camelot/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
---

# PDF Table Extraction with Camelot

The PDF Table Extraction skill leverages the Camelot library to accurately extract tabular data from PDF documents, handling complex layouts that defeat simpler regex-based approaches. It supports both lattice mode for tables with visible cell borders and stream mode for tables defined by whitespace alignment, automatically selecting the optimal strategy based on page analysis.

The skill handles common PDF table challenges including merged cells spanning multiple rows or columns, tables that flow across page boundaries, rotated text in header rows, and nested sub-tables. Extracted data is output as pandas DataFrames with automatic column type inference (numeric, date, currency, categorical), and can be serialized to CSV, JSON, Excel, or Parquet formats.

Advanced features include accuracy scoring per extracted table to flag low-confidence results for manual review, visual debugging overlays that show detected cell boundaries on the original PDF, batch processing of multi-page documents with table continuation detection, and OCR fallback via Tesseract for scanned PDF pages where text extraction returns empty results. The skill supports coordinate-based table region specification for precise extraction from known page layouts.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pdf-table-extraction-camelot/)
