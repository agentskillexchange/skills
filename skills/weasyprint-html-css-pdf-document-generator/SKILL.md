---
title: "WeasyPrint HTML and CSS to PDF Document Generator"
description: "WeasyPrint is a Python library by Kozea/CourtBouillon that converts HTML and CSS into PDF documents. It implements a CSS layout engine designed specifically for pagination, supporting web standards for printing including page breaks, headers, page counters, and responsive layouts without relying on a browser engine like WebKit or Gecko."
slug: "weasyprint-html-css-pdf-document-generator"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/Kozea/WeasyPrint"
listed: true
---

# WeasyPrint HTML and CSS to PDF Document Generator

WeasyPrint is a Python library by Kozea/CourtBouillon that converts HTML and CSS into PDF documents. It implements a CSS layout engine designed specifically for pagination, supporting web standards for printing including page breaks, headers, page counters, and responsive layouts without relying on a browser engine like WebKit or Gecko.

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
clawhub install weasyprint-html-css-pdf-document-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
WeasyPrint is a visual rendering engine for HTML and CSS that exports to PDF. Unlike browser-based PDF generation tools that wrap WebKit or Gecko, WeasyPrint implements its own CSS layout engine written in Python, designed from the ground up for pagination and print output. This makes it lightweight, predictable, and easy to integrate into server-side workflows.
Key Capabilities
WeasyPrint supports a broad subset of CSS for print, including CSS Paged Media features like @page rules, named pages, page counters, headers and footers, page-break-before/page-break-after/page-break-inside controls, and margin boxes. It handles flexbox, grid layout, floating elements, and responsive designs. It renders images (including SVG via CairoSVG), custom fonts via @font-face, and supports CSS variables.
Installation and Usage
Install with pip install weasyprint. WeasyPrint requires Python 3.10+ and depends on Pango, GDK-PixBuf, and Cairo system libraries. The CLI converts HTML files or URLs directly: weasyprint input.html output.pdf. The Python API provides fine-grained control via HTML() and CSS() objects for programmatic PDF generation.
Use Cases
WeasyPrint excels at generating invoices, reports, tickets, certificates, and any document where you want to use HTML/CSS as the template language. It is used in production for automated report generation pipelines, document management systems, and publishing workflows. The BSD license allows commercial use without restrictions.
Agent Integration
For AI agents, WeasyPrint enables skills that generate professional PDF documents from structured data. An agent can compose HTML templates, populate them with data, and produce pixel-perfect PDF output. This is particularly useful for automating document creation workflows, generating reports from database queries, or creating formatted exports from web scraping results.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/weasyprint-html-css-pdf-document-generator/)
