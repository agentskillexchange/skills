---
name: "pdfplumber Python PDF Text and Table Extraction Library"
description: "pdfplumber is a Python library for extracting detailed information from PDFs — text, tables, lines, rectangles, and curves — with visual debugging support. Built on pdfminer.six, it excels at structured table extraction from machine-generated PDFs and includes both a Python API and CLI."
category: "Data Extraction & Transformation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/jsvine/pdfplumber"
---
# pdfplumber Python PDF Text and Table Extraction Library

pdfplumber is a Python library for extracting detailed information from PDFs — text, tables, lines, rectangles, and curves — with visual debugging support. Built on pdfminer.six, it excels at structured table extraction from machine-generated PDFs and includes both a Python API and CLI.

pdfplumber is a Python library for plumbing PDFs for detailed information about every text character, rectangle, line, curve, and image on each page. Its primary strength is structured table extraction from machine-generated PDFs, with a visual debugging system that lets you see exactly what the parser detects. The library is maintained by Jeremy Singer-Vine and has over 7,000 GitHub stars and millions of PyPI downloads.



Core Capabilities

pdfplumber provides access to every visual element on a PDF page. The page.chars property returns a list of dictionaries describing each character’s text, font, size, and bounding box. Similarly, page.lines, page.rects, page.curves, and page.images expose geometric and visual elements. This granular access makes pdfplumber useful for PDFs where layout matters — financial statements, government forms, invoices, and research papers.



Table Extraction

The page.extract_tables() and page.extract_table() methods identify table structures by detecting intersections of lines and edges. Table extraction is highly configurable through a table_settings dictionary that controls parameters like vertical and horizontal strategy (lines, text, or explicit), minimum words per horizontal and vertical lines, snap tolerances, and edge detection. This makes it possible to tune extraction for specific PDF layouts.



Text Extraction

The page.extract_text() method reconstructs readable text from character-level data, with a layout=True option that preserves spatial positioning. Additional parameters control x and y tolerances for grouping characters into words and lines, making it adaptable to PDFs with unusual spacing or formatting.



Visual Debugging

pdfplumber includes a visual debugging system via page.to_image() that renders the page as a PIL Image with overlays. You can draw bounding boxes around detected characters, tables, lines, and rectangles to visually verify what the parser finds. This is invaluable for diagnosing extraction issues.



Cropping and Filtering

Pages can be cropped with page.crop(bounding_box) to focus extraction on specific regions, and objects can be filtered with page.filter() to remove unwanted elements before extraction. These operations return new Page-like objects that support all the same extraction methods.



Form Value Extraction

For interactive PDF forms (AcroForms), pdfplumber can extract form field values and annotations, providing access to filled-in form data programmatically.



CLI Interface

pdfplumber includes a command-line interface that outputs CSV, JSON, or plain text. Run pdfplumber input.pdf to get a CSV of all objects, or use --format text for layout-preserved plain text output. The --pages flag supports page ranges.



Installation and Compatibility

Install with pip install pdfplumber. The library supports Python 3.10 through 3.14 and is built on pdfminer.six. It is MIT-licensed and available at github.com/jsvine/pdfplumber and pypi.org/project/pdfplumber.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pdfplumber-python-pdf-text-table-extraction
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pdfplumber-python-pdf-text-table-extraction -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pdfplumber-python-pdf-text-table-extraction -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pdfplumber-python-pdf-text-table-extraction -a codex
```

### OpenClaw

```bash
clawhub install pdfplumber-python-pdf-text-table-extraction
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pdfplumber-python-pdf-text-table-extraction/)
