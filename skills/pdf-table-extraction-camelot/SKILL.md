---
title: "PDF Table Extraction with Camelot"
description: "The PDF Table Extraction skill leverages the Camelot library to accurately extract tabular data from PDF documents, handling complex layouts that defeat simpler regex-based approaches. It supports both lattice mode for tables with visible cell borders and stream mode for tables defined by whitespace alignment, automatically selecting the optimal strategy based on page analysis. The skill handles common PDF table challenges including merged cells spanning multiple rows or columns, tables that flow across page boundaries, rotated text in header rows, and nested sub-tables. Extracted data is output as pandas DataFrames with automatic column type inference (numeric, date, currency, categorical), and can be serialized to CSV, JSON, Excel, or Parquet formats. Advanced features include accuracy scoring per extracted table to flag low-confidence results for manual review, visual debugging overlays that show detected cell boundaries on the original PDF, batch processing of multi-page documents with table continuation detection, and OCR fallback via Tesseract for scanned PDF pages where text extraction returns empty results. The skill supports coordinate-based table region specification for precise extraction from known page layouts."
source: "https://agentskillexchange.com/skills/pdf-table-extraction-camelot/"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
---

# PDF Table Extraction with Camelot

The PDF Table Extraction skill leverages the Camelot library to accurately extract tabular data from PDF documents, handling complex layouts that defeat simpler regex-based approaches. It supports both lattice mode for tables with visible cell borders and stream mode for tables defined by whitespace alignment, automatically selecting the optimal strategy based on page analysis. The skill handles common PDF table challenges including merged cells spanning multiple rows or columns, tables that flow across page boundaries, rotated text in header rows, and nested sub-tables. Extracted data is output as pandas DataFrames with automatic column type inference (numeric, date, currency, categorical), and can be serialized to CSV, JSON, Excel, or Parquet formats. Advanced features include accuracy scoring per extracted table to flag low-confidence results for manual review, visual debugging overlays that show detected cell boundaries on the original PDF, batch processing of multi-page documents with table continuation detection, and OCR fallback via Tesseract for scanned PDF pages where text extraction returns empty results. The skill supports coordinate-based table region specification for precise extraction from known page layouts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pdf-table-extraction-camelot/)
