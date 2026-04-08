---
title: Docling Document Parsing and Conversion
description: Docling is an open-source document processing project designed to prepare
  files for modern AI workflows. According to the upstream repository, it parses many
  input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX,
  and plain text, then converts them into structured representations and export formats
  such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake
  layer when an agent needs to work from real documents instead of manually curated
  text. The repository highlights advanced PDF understanding, including layout analysis,
  reading order, table structure, formulas, code blocks, image classification, OCR
  for scanned files, and support for visual language models. It also provides a Python
  API through DocumentConverter , a CLI that can convert local paths or URLs, and
  integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack.
  The project additionally notes local execution for sensitive or air-gapped environments
  and mentions an MCP server for agent-facing connectivity. For ASE users, the main
  job-to-be-done is high-quality document ingestion and transformation before downstream
  summarization, extraction, search, or agent orchestration. That includes converting
  messy PDFs into structured markdown, extracting tables, preserving metadata, and
  standardizing heterogeneous file types for retrieval pipelines. With strong GitHub
  adoption, active releases, MIT licensing, and official docs hosted by the project,
  Docling clearly passes the discovery intake gate.
verification: security_reviewed
source: https://github.com/docling-project/docling
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
---

# Docling Document Parsing and Conversion

Docling is an open-source document processing project designed to prepare files for modern AI workflows. According to the upstream repository, it parses many input formats including PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text, then converts them into structured representations and export formats such as Markdown, HTML, WebVTT, DocTags, and JSON. That makes it a practical intake layer when an agent needs to work from real documents instead of manually curated text. The repository highlights advanced PDF understanding, including layout analysis, reading order, table structure, formulas, code blocks, image classification, OCR for scanned files, and support for visual language models. It also provides a Python API through DocumentConverter , a CLI that can convert local paths or URLs, and integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. The project additionally notes local execution for sensitive or air-gapped environments and mentions an MCP server for agent-facing connectivity. For ASE users, the main job-to-be-done is high-quality document ingestion and transformation before downstream summarization, extraction, search, or agent orchestration. That includes converting messy PDFs into structured markdown, extracting tables, preserving metadata, and standardizing heterogeneous file types for retrieval pipelines. With strong GitHub adoption, active releases, MIT licensing, and official docs hosted by the project, Docling clearly passes the discovery intake gate.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-parsing-and-conversion/)
