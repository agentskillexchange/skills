---
title: "Docling Document Conversion and Extraction Toolkit"
description: "Docling is an open source document processing toolkit from the Docling project that converts PDFs, Office files, HTML, and other formats into structured output for downstream AI and automation workflows. It is well documented, actively maintained, and published as a Python package with a live docs site."
slug: "docling-document-conversion-and-extraction-toolkit"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/docling-project/docling"
tool_ecosystem:
  github_repo: "docling-project/docling"
  github_stars: 57465
---

# Docling Document Conversion and Extraction Toolkit

Docling is an open source document processing toolkit from the Docling project that converts PDFs, Office files, HTML, and other formats into structured output for downstream AI and automation workflows. It is well documented, actively maintained, and published as a Python package with a live docs site.

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
clawhub install docling-document-conversion-and-extraction-toolkit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Docling is a document conversion and extraction toolkit designed to turn messy enterprise documents into structured data that downstream agents can actually use. The upstream project lives at github.com/docling-project/docling with an MIT license, release tags, and a high-activity commit history, and it publishes documentation at docling-project.github.io/docling. In practice, Docling helps an agent ingest PDFs, presentations, spreadsheets, HTML pages, images, and Office documents, then normalize them into text, markdown, JSON, or richer document representations that preserve layout and semantic structure.
This makes it a good ASE candidate for data extraction and transformation workflows. An agent can use Docling before retrieval, summarization, indexing, or validation steps, especially when raw OCR or plain text extraction is not enough. The toolkit is especially useful in pipelines that need table preservation, section-aware parsing, or consistent chunking before sending content into embeddings, search indexes, or LLM prompts. Because the project ships as a Python package, it integrates cleanly with notebooks, ETL jobs, batch workers, FastAPI services, and CLI-based automation.
The real install path is straightforward: the project docs recommend installing the docling package from pip, with Python 3.10 or higher for current releases. For agents working across invoices, reports, manuals, and mixed document corpora, Docling provides a concrete, production-relevant job to be done: convert source files into structured machine-readable artifacts with better fidelity than ad hoc parsing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-conversion-and-extraction-toolkit/)
