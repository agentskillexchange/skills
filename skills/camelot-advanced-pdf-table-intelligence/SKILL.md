---
title: "Camelot Advanced PDF Table Intelligence"
description: "Camelot Advanced PDF Table Intelligence extends PDF table extraction capabilities using the Camelot-py library with its sophisticated OpenCV-based detection engine. Unlike basic extractors, it handles complex table layouts including rotated tables, nested sub-tables, and tables spanning multiple pages with header continuation.\nThe lattice detection mode uses OpenCV morphological transformations (erosion, dilation) to identify table gridlines even in low-quality scanned documents. Parameters for line detection threshold, iteration count, and minimum line length are auto-tuned based on page DPI and content density analysis.\nStream mode extraction employs text-position clustering using the PDFMiner layout analysis engine, with configurable column and row tolerances for whitespace-separated data. The skill includes preprocessing steps for deskewing via Hough line transform, contrast normalization, and noise reduction for scanned documents.\nOutput processing includes automatic header detection using typography analysis (bold, larger font size), merged cell expansion with configurable fill strategies (forward-fill, value repeat, blank), and data type inference with locale-aware number parsing. Integration with pandas enables direct DataFrame output with proper dtypes, MultiIndex support for hierarchical headers, and Excel export via openpyxl with preserved table formatting."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/"
framework:
  - "Cursor"
---

# Camelot Advanced PDF Table Intelligence

Camelot Advanced PDF Table Intelligence extends PDF table extraction capabilities using the Camelot-py library with its sophisticated OpenCV-based detection engine. Unlike basic extractors, it handles complex table layouts including rotated tables, nested sub-tables, and tables spanning multiple pages with header continuation.
The lattice detection mode uses OpenCV morphological transformations (erosion, dilation) to identify table gridlines even in low-quality scanned documents. Parameters for line detection threshold, iteration count, and minimum line length are auto-tuned based on page DPI and content density analysis.
Stream mode extraction employs text-position clustering using the PDFMiner layout analysis engine, with configurable column and row tolerances for whitespace-separated data. The skill includes preprocessing steps for deskewing via Hough line transform, contrast normalization, and noise reduction for scanned documents.
Output processing includes automatic header detection using typography analysis (bold, larger font size), merged cell expansion with configurable fill strategies (forward-fill, value repeat, blank), and data type inference with locale-aware number parsing. Integration with pandas enables direct DataFrame output with proper dtypes, MultiIndex support for hierarchical headers, and Excel export via openpyxl with preserved table formatting.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/camelot-advanced-pdf-table-intelligence
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/camelot-advanced-pdf-table-intelligence` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/)
