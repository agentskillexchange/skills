---
title: Docling AI Document Intelligence Pipeline
description: 'Docling is an open-source document processing toolkit originally developed
  by IBM Research and now maintained under the docling-project organization on GitHub.
  It converts a wide range of document formats — PDF, DOCX, PPTX, XLSX, HTML, images
  (PNG, TIFF, JPEG), LaTeX, WAV, MP3, WebVTT, and plain text — into a unified DoclingDocument
  representation that can be exported as Markdown, HTML, JSON, or DocTags. For PDF
  documents, Docling performs advanced layout analysis including page structure detection,
  reading order determination, table structure recognition, code block identification,
  mathematical formula extraction, and image classification. It supports scanned documents
  through built-in OCR and can leverage Visual Language Models such as GraniteDocling
  for enhanced understanding. The toolkit also handles chart interpretation (bar charts,
  pie charts, line plots) and molecular structure recognition. Docling provides a
  straightforward Python API and CLI. A basic conversion is as simple as calling DocumentConverter().convert(source)
  on a local file path or URL, then exporting with result.document.export_to_markdown()
  . The CLI supports batch conversion with docling https://arxiv.org/pdf/2206.01062
  . For production deployments, Docling offers an MCP server for agentic applications.
  The toolkit integrates directly with popular AI frameworks: LangChain, LlamaIndex,
  CrewAI, Haystack, and spaCy all have Docling connectors. This makes it a natural
  fit as the document ingestion layer in RAG (Retrieval-Augmented Generation) pipelines,
  where documents need to be parsed, chunked, and embedded before retrieval. Docling
  supports local execution for sensitive data and air-gapped environments, runs on
  macOS, Linux, and Windows (x86_64 and arm64), and requires Python 3.10+. It is available
  on PyPI via pip install docling and is licensed under the MIT license. The project
  has accumulated over 10,000 GitHub stars and was accepted to AAAI 2025.'
verification: security_reviewed
source: https://github.com/docling-project/docling
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
tool_ecosystem:
  github_repo: docling-project/docling
  github_stars: 56871
---

# Docling AI Document Intelligence Pipeline

Docling is an open-source document processing toolkit originally developed by IBM Research and now maintained under the docling-project organization on GitHub. It converts a wide range of document formats — PDF, DOCX, PPTX, XLSX, HTML, images (PNG, TIFF, JPEG), LaTeX, WAV, MP3, WebVTT, and plain text — into a unified DoclingDocument representation that can be exported as Markdown, HTML, JSON, or DocTags. For PDF documents, Docling performs advanced layout analysis including page structure detection, reading order determination, table structure recognition, code block identification, mathematical formula extraction, and image classification. It supports scanned documents through built-in OCR and can leverage Visual Language Models such as GraniteDocling for enhanced understanding. The toolkit also handles chart interpretation (bar charts, pie charts, line plots) and molecular structure recognition. Docling provides a straightforward Python API and CLI. A basic conversion is as simple as calling DocumentConverter().convert(source) on a local file path or URL, then exporting with result.document.export_to_markdown() . The CLI supports batch conversion with docling https://arxiv.org/pdf/2206.01062 . For production deployments, Docling offers an MCP server for agentic applications. The toolkit integrates directly with popular AI frameworks: LangChain, LlamaIndex, CrewAI, Haystack, and spaCy all have Docling connectors. This makes it a natural fit as the document ingestion layer in RAG (Retrieval-Augmented Generation) pipelines, where documents need to be parsed, chunked, and embedded before retrieval. Docling supports local execution for sensitive data and air-gapped environments, runs on macOS, Linux, and Windows (x86_64 and arm64), and requires Python 3.10+. It is available on PyPI via pip install docling and is licensed under the MIT license. The project has accumulated over 10,000 GitHub stars and was accepted to AAAI 2025.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-ai-document-intelligence-pipeline/)
