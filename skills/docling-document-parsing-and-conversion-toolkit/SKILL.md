---
title: "Docling Document Parsing and Conversion Toolkit"
description: "Docling is an open source document processing toolkit that converts PDFs, Office files, HTML, images, audio, and more into structured outputs for AI workflows. It supports local execution, OCR, and integrations with agent frameworks and retrieval pipelines."
slug: "docling-document-parsing-and-conversion-toolkit"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/docling-project/docling"
tool_ecosystem:
  github_repo: "docling-project/docling"
  github_stars: 57465
listed: true
---

# Docling Document Parsing and Conversion Toolkit

Docling is an open source document processing toolkit that converts PDFs, Office files, HTML, images, audio, and more into structured outputs for AI workflows. It supports local execution, OCR, and integrations with agent frameworks and retrieval pipelines.

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
clawhub install docling-document-parsing-and-conversion-toolkit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Docling is an open source document parsing and conversion project that focuses on preparing real-world documents for AI and automation workflows. The upstream repository and docs show support for PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text inputs, with output options including Markdown, HTML, JSON, and DocTags. For agent use cases, that means a single tool can normalize messy source material into formats that are easier to search, summarize, chunk, and pass into downstream models.
Its job to be done is concrete: take heterogeneous files and turn them into structured, machine-usable representations without forcing every workflow to build a custom parser. Docling also exposes OCR support for scanned PDFs and images, ships a CLI for direct conversion, and documents integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. Those integration points make it especially useful for ingestion pipelines, document QA systems, knowledge base preparation, and batch content extraction jobs where agents need more than plain text scraping.
The project has strong intake evidence. It has an official GitHub repository, live documentation, a published PyPI package, an MIT license, and recent repository activity. The maintainers also document a straightforward install path and current Python version requirements, which keeps adoption friction low for marketplace users looking for a real upstream tool rather than a speculative pattern.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-parsing-and-conversion-toolkit/)
