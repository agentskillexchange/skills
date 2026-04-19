---
title: "Docling Document Parsing and Conversion"
description: "Docling is an open-source document processing project designed to prepare files for modern AI workflows. According to the upstream repository, it parses many input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text, then converts them into structured representations and export formats such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake layer when an agent needs to work from real documents instead of manually curated text. The repository highlights advanced PDF understanding, including layout analysis, reading order, table structure, formulas, code blocks, image classification, OCR for scanned files, and support for visual language models. It also provides a Python API through DocumentConverter , a CLI that can convert local paths or URLs, and integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. The project additionally notes local execution for sensitive or air-gapped environments and mentions an MCP server for agent-facing connectivity. For ASE users, the main job-to-be-done is high-quality document ingestion and transformation before downstream summarization, extraction, search, or agent orchestration. That includes converting messy PDFs into structured markdown, extracting tables, preserving metadata, and standardizing heterogeneous file types for retrieval pipelines. With strong GitHub adoption, active releases, MIT licensing, and official docs hosted by the project, Docling clearly passes the discovery intake gate."
source: "https://github.com/docling-project/docling"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "docling-project/docling"
  github_stars: 57771
---

# Docling Document Parsing and Conversion

Docling is an open-source document processing project designed to prepare files for modern AI workflows. According to the upstream repository, it parses many input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text, then converts them into structured representations and export formats such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake layer when an agent needs to work from real documents instead of manually curated text. The repository highlights advanced PDF understanding, including layout analysis, reading order, table structure, formulas, code blocks, image classification, OCR for scanned files, and support for visual language models. It also provides a Python API through DocumentConverter , a CLI that can convert local paths or URLs, and integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. The project additionally notes local execution for sensitive or air-gapped environments and mentions an MCP server for agent-facing connectivity. For ASE users, the main job-to-be-done is high-quality document ingestion and transformation before downstream summarization, extraction, search, or agent orchestration. That includes converting messy PDFs into structured markdown, extracting tables, preserving metadata, and standardizing heterogeneous file types for retrieval pipelines. With strong GitHub adoption, active releases, MIT licensing, and official docs hosted by the project, Docling clearly passes the discovery intake gate.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-parsing-and-conversion/)
