---
name: Docling AI Document Intelligence Pipeline
description: Docling is an IBM-backed open-source toolkit that converts PDF, DOCX,
  PPTX, XLSX, HTML, images, audio, and LaTeX files into structured formats for gen
  AI workflows. It features advanced PDF layout understanding, OCR, table extraction,
  and integrations with LangChain, LlamaIndex, and CrewAI.
category: "Data Extraction &amp; Transformation"
framework: Claude Code
verification: security_reviewed
source: "https://github.com/docling-project/docling"
tool_ecosystem:
  github_repo: "https://github.com/docling-project/docling"
  github_stars: 56871
---
# Docling AI Document Intelligence Pipeline

Docling is an IBM-backed open-source toolkit that converts PDF, DOCX, PPTX, XLSX, HTML, images, audio, and LaTeX files into structured formats for gen AI workflows. It features advanced PDF layout understanding, OCR, table extraction, and integrations with LangChain, LlamaIndex, and CrewAI.

Docling is an open-source document processing toolkit originally developed by IBM Research and now maintained under the docling-project organization on GitHub. It converts a wide range of document formats — PDF, DOCX, PPTX, XLSX, HTML, images (PNG, TIFF, JPEG), LaTeX, WAV, MP3, WebVTT, and plain text — into a unified DoclingDocument representation that can be exported as Markdown, HTML, JSON, or DocTags.

For PDF documents, Docling performs advanced layout analysis including page structure detection, reading order determination, table structure recognition, code block identification, mathematical formula extraction, and image classification. It supports scanned documents through built-in OCR and can leverage Visual Language Models such as GraniteDocling for enhanced understanding. The toolkit also handles chart interpretation (bar charts, pie charts, line plots) and molecular structure recognition.

Docling provides a straightforward Python API and CLI. A basic conversion is as simple as calling DocumentConverter().convert(source) on a local file path or URL, then exporting with result.document.export_to_markdown(). The CLI supports batch conversion with docling https://arxiv.org/pdf/2206.01062. For production deployments, Docling offers an MCP server for agentic applications.

The toolkit integrates directly with popular AI frameworks: LangChain, LlamaIndex, CrewAI, Haystack, and spaCy all have Docling connectors. This makes it a natural fit as the document ingestion layer in RAG (Retrieval-Augmented Generation) pipelines, where documents need to be parsed, chunked, and embedded before retrieval.

Docling supports local execution for sensitive data and air-gapped environments, runs on macOS, Linux, and Windows (x86_64 and arm64), and requires Python 3.10+. It is available on PyPI via pip install docling and is licensed under the MIT license. The project has accumulated over 10,000 GitHub stars and was accepted to AAAI 2025.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docling-ai-document-intelligence-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docling-ai-document-intelligence-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docling-ai-document-intelligence-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docling-ai-document-intelligence-pipeline -a codex
```

### OpenClaw

```bash
clawhub install docling-ai-document-intelligence-pipeline
```


## Source

- [GitHub](https://github.com/docling-project/docling)
