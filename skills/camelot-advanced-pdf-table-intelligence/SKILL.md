---
title: Camelot Advanced PDF Table Intelligence
description: Camelot Advanced PDF Table Intelligence extends PDF table extraction
  capabilities using the Camelot-py library with its sophisticated OpenCV-based detection
  engine. Unlike basic extractors, it handles complex table layouts including rotated
  tables, nested sub-tables, and tables spanning multiple pages with header continuation.
  The lattice detection mode uses OpenCV morphological transformations (erosion, dilation)
  to identify table gridlines even in low-quality scanned documents. Parameters for
  line detection threshold, iteration count, and minimum line length are auto-tuned
  based on page DPI and content density analysis. Stream mode extraction employs text-position
  clustering using the PDFMiner layout analysis engine, with configurable column and
  row tolerances for whitespace-separated data. The skill includes preprocessing steps
  for deskewing via Hough line transform, contrast normalization, and noise reduction
  for scanned documents. Output processing includes automatic header detection using
  typography analysis (bold, larger font size), merged cell expansion with configurable
  fill strategies (forward-fill, value repeat, blank), and data type inference with
  locale-aware number parsing. Integration with pandas enables direct DataFrame output
  with proper dtypes, MultiIndex support for hierarchical headers, and Excel export
  via openpyxl with preserved table formatting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/
category:
- Data Extraction &amp; Transformation
framework:
- Cursor
---

# Camelot Advanced PDF Table Intelligence

Camelot Advanced PDF Table Intelligence extends PDF table extraction capabilities using the Camelot-py library with its sophisticated OpenCV-based detection engine. Unlike basic extractors, it handles complex table layouts including rotated tables, nested sub-tables, and tables spanning multiple pages with header continuation. The lattice detection mode uses OpenCV morphological transformations (erosion, dilation) to identify table gridlines even in low-quality scanned documents. Parameters for line detection threshold, iteration count, and minimum line length are auto-tuned based on page DPI and content density analysis. Stream mode extraction employs text-position clustering using the PDFMiner layout analysis engine, with configurable column and row tolerances for whitespace-separated data. The skill includes preprocessing steps for deskewing via Hough line transform, contrast normalization, and noise reduction for scanned documents. Output processing includes automatic header detection using typography analysis (bold, larger font size), merged cell expansion with configurable fill strategies (forward-fill, value repeat, blank), and data type inference with locale-aware number parsing. Integration with pandas enables direct DataFrame output with proper dtypes, MultiIndex support for hierarchical headers, and Excel export via openpyxl with preserved table formatting.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-advanced-pdf-table-intelligence/)
