---
name: "Extract invoice fields from vendor PDFs into structured records"
slug: "extract-invoice-fields-from-vendor-pdfs-into-structured-records"
description: "Uses invoice2data to turn invoice PDFs into structured JSON, CSV, or XML using supplier-specific templates. This is for repeatable invoice field extraction and renaming workflows, not for full accounting system automation or generic OCR catalog listings."
github_stars: 2137
verification: "security_reviewed"
source: "https://github.com/invoice-x/invoice2data"
author: "invoice-x"
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

Install the Python package from PyPI:

- pip install invoice2data

The default pdfium backend bundles its own dependencies, so no system PDF extraction library is required for the default path. See the upstream installation guide for optional OCR and backend extras.

- Source: https://github.com/invoice-x/invoice2data
- Extracted from upstream docs: https://raw.githubusercontent.com/invoice-x/invoice2data/HEAD/README.md

## Documentation

- https://invoice2data.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-invoice-fields-from-vendor-pdfs-into-structured-records/)
