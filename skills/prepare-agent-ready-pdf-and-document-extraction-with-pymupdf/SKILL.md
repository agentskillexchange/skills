---
title: "Prepare agent-ready PDF and document extraction with PyMuPDF"
description: "Use PyMuPDF to extract text, layout metadata, tables, images, Markdown, or JSON from PDFs and documents before an agent ingests or reviews them."
verification: "security_reviewed"
source: "https://github.com/pymupdf/PyMuPDF"
author: "PyMuPDF"
publisher_type: "company"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pymupdf/PyMuPDF"
  github_stars: 10058
---

# Prepare agent-ready PDF and document extraction with PyMuPDF

Use PyMuPDF to extract text, layout metadata, tables, images, Markdown, or JSON from PDFs and documents before an agent ingests or reviews them.

## Prerequisites

Python 3.10+, PyMuPDF, source PDFs or supported document files, and optional pymupdf4llm or Tesseract OCR for LLM-ready Markdown or scanned pages.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install pymupdf. For LLM/RAG-oriented Markdown or JSON extraction, also install pymupdf4llm; for scanned-page OCR, install Tesseract separately and configure the extraction workflow to emit reviewed text, Markdown, or JSON outputs.
```

## Documentation

- https://pymupdf.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-agent-ready-pdf-and-document-extraction-with-pymupdf/)
