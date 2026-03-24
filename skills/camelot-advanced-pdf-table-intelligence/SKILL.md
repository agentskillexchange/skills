---
name: "Camelot Advanced PDF Table Intelligence"
description: "Intelligent PDF table detection and extraction using Camelot-py with OpenCV-based lattice detection and morphological transformations. Handles rotated tables, merged cells, and multi-page spanning tables."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48224  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Camelot Advanced PDF Table Intelligence

Intelligent PDF table detection and extraction using Camelot-py with OpenCV-based lattice detection and morphological transformations. Handles rotated tables, merged cells, and multi-page spanning tables.

## Overview

Camelot Advanced PDF Table Intelligence extends PDF table extraction capabilities using the Camelot-py library with its sophisticated OpenCV-based detection engine. Unlike basic extractors, it handles complex table layouts including rotated tables, nested sub-tables, and tables spanning multiple pages with header continuation.

The lattice detection mode uses OpenCV morphological transformations (erosion, dilation) to identify table gridlines even in low-quality scanned documents. Parameters for line detection threshold, iteration count, and minimum line length are auto-tuned based on page DPI and content density analysis.

Stream mode extraction employs text-position clustering using the PDFMiner layout analysis engine, with configurable column and row tolerances for whitespace-separated data. The skill includes preprocessing steps for deskewing via Hough line transform, contrast normalization, and noise reduction for scanned documents.

Output processing includes automatic header detection using typography analysis (bold, larger font size), merged cell expansion with configurable fill strategies (forward-fill, value repeat, blank), and data type inference with locale-aware number parsing. Integration with pandas enables direct DataFrame output with proper dtypes, MultiIndex support for hierarchical headers, and Excel export via openpyxl with preserved table formatting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill camelot-advanced-pdf-table-intelligence
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill camelot-advanced-pdf-table-intelligence -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill camelot-advanced-pdf-table-intelligence -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill camelot-advanced-pdf-table-intelligence -a codex
```

### OpenClaw

```bash
clawhub install camelot-advanced-pdf-table-intelligence
```

## Source

- Marketplace: https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/
