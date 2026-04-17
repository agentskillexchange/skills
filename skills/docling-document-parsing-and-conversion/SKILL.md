---
title: "Docling Document Parsing and Conversion"
description: "Docling is an open-source document processing project designed to prepare files for modern AI workflows. According to the upstream repository, it parses many input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text, then converts them into structured representations and export formats such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake layer when an agent needs to work from real documents instead of manually curated text.\nThe repository highlights advanced PDF understanding, including layout analysis, reading order, table structure, formulas, code blocks, image classification, OCR for scanned files, and support for visual language models. It also provides a Python API through DocumentConverter, a CLI that can convert local paths or URLs, and integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. The project additionally notes local execution for sensitive or air-gapped environments and mentions an MCP server for agent-facing connectivity.\nFor ASE users, the main job-to-be-done is high-quality document ingestion and transformation before downstream summarization, extraction, search, or agent orchestration. That includes converting messy PDFs into structured markdown, extracting tables, preserving metadata, and standardizing heterogeneous file types for retrieval pipelines. With strong GitHub adoption, active releases, MIT licensing, and official docs hosted by the project, Docling clearly passes the discovery intake gate."
verification: security_reviewed
source: "https://github.com/docling-project/docling"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "docling-project/docling"
  github_stars: 57771
---

# Docling Document Parsing and Conversion

Docling is an open-source document processing project designed to prepare files for modern AI workflows. According to the upstream repository, it parses many input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text, then converts them into structured representations and export formats such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake layer when an agent needs to work from real documents instead of manually curated text.
The repository highlights advanced PDF understanding, including layout analysis, reading order, table structure, formulas, code blocks, image classification, OCR for scanned files, and support for visual language models. It also provides a Python API through DocumentConverter, a CLI that can convert local paths or URLs, and integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. The project additionally notes local execution for sensitive or air-gapped environments and mentions an MCP server for agent-facing connectivity.
For ASE users, the main job-to-be-done is high-quality document ingestion and transformation before downstream summarization, extraction, search, or agent orchestration. That includes converting messy PDFs into structured markdown, extracting tables, preserving metadata, and standardizing heterogeneous file types for retrieval pipelines. With strong GitHub adoption, active releases, MIT licensing, and official docs hosted by the project, Docling clearly passes the discovery intake gate.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docling-document-parsing-and-conversion
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docling-document-parsing-and-conversion` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-parsing-and-conversion/)
