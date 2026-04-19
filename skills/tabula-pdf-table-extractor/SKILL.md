---
title: "Tabula PDF Table Extractor"
description: "The Tabula PDF Table Extractor specializes in high-accuracy table extraction from PDF documents using the tabula-java library accessed through the python-tabula (tabula-py) wrapper. It handles both lattice-based tables (with visible gridlines) and stream-based tables (whitespace-aligned columns). The skill automatically analyzes each PDF page to determine the optimal extraction method — lattice mode for ruled tables and stream mode for borderless tables. Custom extraction areas can be specified using coordinate-based regions when automatic detection fails, with a visual preview mode that highlights detected table boundaries. Post-extraction processing includes automatic column type inference (numeric, date, currency, percentage, text), header row detection and normalization, merged cell handling, and multi-page table concatenation. Output formats include CSV with proper escaping, JSON with nested structures, and pandas DataFrame objects for direct analytical use. Batch processing supports directory scanning with file filtering, parallel extraction using concurrent.futures, and progress tracking. Integration with OpenPyXL enables direct Excel output with formatted headers, auto-sized columns, and conditional formatting for numeric data."
source: "https://agentskillexchange.com/skills/tabula-pdf-table-extractor/"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
---

# Tabula PDF Table Extractor

The Tabula PDF Table Extractor specializes in high-accuracy table extraction from PDF documents using the tabula-java library accessed through the python-tabula (tabula-py) wrapper. It handles both lattice-based tables (with visible gridlines) and stream-based tables (whitespace-aligned columns). The skill automatically analyzes each PDF page to determine the optimal extraction method — lattice mode for ruled tables and stream mode for borderless tables. Custom extraction areas can be specified using coordinate-based regions when automatic detection fails, with a visual preview mode that highlights detected table boundaries. Post-extraction processing includes automatic column type inference (numeric, date, currency, percentage, text), header row detection and normalization, merged cell handling, and multi-page table concatenation. Output formats include CSV with proper escaping, JSON with nested structures, and pandas DataFrame objects for direct analytical use. Batch processing supports directory scanning with file filtering, parallel extraction using concurrent.futures, and progress tracking. Integration with OpenPyXL enables direct Excel output with formatted headers, auto-sized columns, and conditional formatting for numeric data.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tabula-pdf-table-extractor/)
