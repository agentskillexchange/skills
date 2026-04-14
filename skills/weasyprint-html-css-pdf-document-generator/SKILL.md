---
title: "WeasyPrint HTML and CSS to PDF Document Generator"
description: "WeasyPrint is a Python library by Kozea/CourtBouillon that converts HTML and CSS into PDF documents. It implements a CSS layout engine designed specifically for pagination, supporting web standards for printing including page breaks, headers, page counters, and responsive layouts without relying on a browser engine like WebKit or Gecko."
verification: security_reviewed
source: "https://github.com/Kozea/WeasyPrint"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Kozea/WeasyPrint"
  github_stars: 8841
---

# WeasyPrint HTML and CSS to PDF Document Generator

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/weasyprint-html-css-pdf-document-generator/)
