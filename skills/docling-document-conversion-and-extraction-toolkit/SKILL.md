---
title: "Docling Document Conversion and Extraction Toolkit"
description: "Docling is an open source document processing toolkit from the Docling project that converts PDFs, Office files, HTML, and other formats into structured output for downstream AI and automation workflows. It is well documented, actively maintained, and published as a Python package with a live docs site."
verification: security_reviewed
source: "https://github.com/docling-project/docling"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "docling-project/docling"
  github_stars: 57622
---

# Docling Document Conversion and Extraction Toolkit

Docling is a document conversion and extraction toolkit designed to turn messy enterprise documents into structured data that downstream agents can actually use. The upstream project lives at github.com/docling-project/docling with an MIT license, release tags, and a high-activity commit history, and it publishes documentation at docling-project.github.io/docling. In practice, Docling helps an agent ingest PDFs, presentations, spreadsheets, HTML pages, images, and Office documents, then normalize them into text, markdown, JSON, or richer document representations that preserve layout and semantic structure.

This makes it a good ASE candidate for data extraction and transformation workflows. An agent can use Docling before retrieval, summarization, indexing, or validation steps, especially when raw OCR or plain text extraction is not enough. The toolkit is especially useful in pipelines that need table preservation, section-aware parsing, or consistent chunking before sending content into embeddings, search indexes, or LLM prompts. Because the project ships as a Python package, it integrates cleanly with notebooks, ETL jobs, batch workers, FastAPI services, and CLI-based automation.

The real install path is straightforward: the project docs recommend installing the docling package from pip, with Python 3.10 or higher for current releases. For agents working across invoices, reports, manuals, and mixed document corpora, Docling provides a concrete, production-relevant job to be done: convert source files into structured machine-readable artifacts with better fidelity than ad hoc parsing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docling-document-conversion-and-extraction-toolkit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docling-document-conversion-and-extraction-toolkit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-conversion-and-extraction-toolkit/)
