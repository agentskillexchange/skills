---
title: "Docling Document Parsing and Conversion"
description: "Docling is an open-source document processing toolkit for turning PDFs and other files into structured outputs for AI systems. It handles advanced PDF understanding, OCR, multiple export formats, and integrations with agent and retrieval frameworks."
slug: "docling-document-parsing-and-conversion"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/docling-project/docling"
listed: true
---

# Docling Document Parsing and Conversion

Docling is an open-source document processing toolkit for turning PDFs and other files into structured outputs for AI systems. It handles advanced PDF understanding, OCR, multiple export formats, and integrations with agent and retrieval frameworks.

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
clawhub install docling-document-parsing-and-conversion
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Docling is an open-source document processing project designed to prepare files for modern AI workflows. According to the upstream repository, it parses many input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text, then converts them into structured representations and export formats such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake layer when an agent needs to work from real documents instead of manually curated text.
The repository highlights advanced PDF understanding, including layout analysis, reading order, table structure, formulas, code blocks, image classification, OCR for scanned files, and support for visual language models. It also provides a Python API through DocumentConverter, a CLI that can convert local paths or URLs, and integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. The project additionally notes local execution for sensitive or air-gapped environments and mentions an MCP server for agent-facing connectivity.
For ASE users, the main job-to-be-done is high-quality document ingestion and transformation before downstream summarization, extraction, search, or agent orchestration. That includes converting messy PDFs into structured markdown, extracting tables, preserving metadata, and standardizing heterogeneous file types for retrieval pipelines. With strong GitHub adoption, active releases, MIT licensing, and official docs hosted by the project, Docling clearly passes the discovery intake gate.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-parsing-and-conversion/)
