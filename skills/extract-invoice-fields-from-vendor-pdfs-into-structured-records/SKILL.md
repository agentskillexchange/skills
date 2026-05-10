---
title: "Extract invoice fields from vendor PDFs into structured records"
slug: "extract-invoice-fields-from-vendor-pdfs-into-structured-records"
description: "Uses invoice2data to turn invoice PDFs into structured JSON, CSV, or XML using supplier-specific templates. This is for repeatable invoice field extraction and renaming workflows, not for full accounting system automation or generic OCR catalog listings."
github_stars: 2137
verification: "security_reviewed"
source: "https://github.com/invoice-x/invoice2data"
publisher_type: "open_source_project"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "invoice-x/invoice2data"
  github_stars: 2137
---

# Extract invoice fields from vendor PDFs into structured records

Uses invoice2data to turn invoice PDFs into structured JSON, CSV, or XML using supplier-specific templates. This is for repeatable invoice field extraction and renaming workflows, not for full accounting system automation or generic OCR catalog listings.

## Prerequisites

pdftotext or pdfminer or pdfplumber or OCRmyPDF or Tesseract or Google Cloud Vision

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install invoice2data plus one supported input reader such as pdftotext, pdfminer, pdfplumber, OCRmyPDF, Tesseract, or Google Cloud Vision as documented upstream.
```

## Documentation

- https://invoice2data.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-invoice-fields-from-vendor-pdfs-into-structured-records/)
