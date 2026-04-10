---
title: "Camelot Advanced PDF Table Intelligence"
description: "Intelligent PDF table detection and extraction using Camelot-py with OpenCV-based lattice detection and morphological transformations. Handles rotated tables, merged cells, and multi-page spanning tables."
slug: "camelot-advanced-pdf-table-intelligence"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/"
listed: true
---

# Camelot Advanced PDF Table Intelligence

Intelligent PDF table detection and extraction using Camelot-py with OpenCV-based lattice detection and morphological transformations. Handles rotated tables, merged cells, and multi-page spanning tables.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install camelot-advanced-pdf-table-intelligence
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Camelot Advanced PDF Table Intelligence extends PDF table extraction capabilities using the Camelot-py library with its sophisticated OpenCV-based detection engine. Unlike basic extractors, it handles complex table layouts including rotated tables, nested sub-tables, and tables spanning multiple pages with header continuation.
The lattice detection mode uses OpenCV morphological transformations (erosion, dilation) to identify table gridlines even in low-quality scanned documents. Parameters for line detection threshold, iteration count, and minimum line length are auto-tuned based on page DPI and content density analysis.
Stream mode extraction employs text-position clustering using the PDFMiner layout analysis engine, with configurable column and row tolerances for whitespace-separated data. The skill includes preprocessing steps for deskewing via Hough line transform, contrast normalization, and noise reduction for scanned documents.
Output processing includes automatic header detection using typography analysis (bold, larger font size), merged cell expansion with configurable fill strategies (forward-fill, value repeat, blank), and data type inference with locale-aware number parsing. Integration with pandas enables direct DataFrame output with proper dtypes, MultiIndex support for hierarchical headers, and Excel export via openpyxl with preserved table formatting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/)
