---
title: "Camelot Advanced PDF Table Intelligence"
description: "Intelligent PDF table detection and extraction using Camelot-py with OpenCV-based lattice detection and morphological transformations. Handles rotated tables, merged cells, and multi-page spanning tables."
verification: "security_reviewed"
source: "https://github.com/camelot-dev/camelot"
category:
  - "Data Extraction & Transformation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "camelot-dev/camelot"
  github_stars: 3673
---

# Camelot Advanced PDF Table Intelligence

Camelot Advanced PDF Table Intelligence extends PDF table extraction capabilities using the Camelot-py library with its sophisticated OpenCV-based detection engine. Unlike basic extractors, it handles complex table layouts including rotated tables, nested sub-tables, and tables spanning multiple pages with header continuation.

The lattice detection mode uses OpenCV morphological transformations (erosion, dilation) to identify table gridlines even in low-quality scanned documents. Parameters for line detection threshold, iteration count, and minimum line length are auto-tuned based on page DPI and content density analysis.

Stream mode extraction employs text-position clustering using the PDFMiner layout analysis engine, with configurable column and row tolerances for whitespace-separated data. The skill includes preprocessing steps for deskewing via Hough line transform, contrast normalization, and noise reduction for scanned documents.

Output processing includes automatic header detection using typography analysis (bold, larger font size), merged cell expansion with configurable fill strategies (forward-fill, value repeat, blank), and data type inference with locale-aware number parsing. Integration with pandas enables direct DataFrame output with proper dtypes, MultiIndex support for hierarchical headers, and Excel export via openpyxl with preserved table formatting.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/camelot-advanced-pdf-table-intelligence
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/camelot-advanced-pdf-table-intelligence`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/)
