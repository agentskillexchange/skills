---
name: "MarkItDown Document-to-Markdown Converter by Microsoft"
description: "MarkItDown is a Python utility by Microsoft that converts PDF, Word, PowerPoint, Excel, images, audio, HTML, and other files into Markdown for LLM consumption. It preserves headings, lists, tables, and links while producing token-efficient output optimized for text analysis pipelines."
category: "Data Extraction &amp; Transformation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/microsoft/markitdown"
tool_ecosystem:
  github_repo: "microsoft/markitdown"
  github_stars: 93207
  license: "MIT"
---
# MarkItDown Document-to-Markdown Converter by Microsoft

MarkItDown is a Python utility by Microsoft that converts PDF, Word, PowerPoint, Excel, images, audio, HTML, and other files into Markdown for LLM consumption. It preserves headings, lists, tables, and links while producing token-efficient output optimized for text analysis pipelines.

MarkItDown is a lightweight Python utility developed by Microsoft for converting a wide variety of file formats into clean, structured Markdown. It is specifically designed for use with Large Language Models and text analysis pipelines, where Markdown offers a highly token-efficient and semantically meaningful representation of document content.

Supported Formats MarkItDown handles an extensive range of input formats including PDF documents, Microsoft Word (.docx), PowerPoint (.pptx), Excel (.xlsx), images (with EXIF metadata extraction and OCR), audio files (with EXIF metadata and speech transcription), HTML pages, text-based formats like CSV, JSON, and XML, ZIP archives (iterating over contents), YouTube URLs, EPubs, and more. This breadth makes it a universal first step in any document ingestion pipeline.

How It Works The tool can be used as a CLI command (markitdown path-to-file.pdf > output.md) or as a Python library. It reads binary file streams, applies format-specific converters, and produces Markdown that preserves important structural elements: headings, lists, tables, links, and formatting. The output prioritizes machine readability over pixel-perfect human rendering.

Installation and Usage Install via pip: pip install markitdown[all] for full format support, or install individual format groups like pip install markitdown[pdf,docx,pptx]. The CLI supports piping (cat file.pdf | markitdown) and output redirection (markitdown file.pdf -o output.md).

MCP Integration MarkItDown also offers an MCP (Model Context Protocol) server via the markitdown-mcp package, enabling integration with LLM applications like Claude Desktop for direct document conversion within AI workflows.

Integration Points MarkItDown integrates with LangChain, AutoGen, and any LLM pipeline that consumes text. It serves as a preprocessing step that converts heterogeneous document collections into a uniform Markdown format suitable for embedding, summarization, RAG, and question-answering tasks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill markitdown-document-to-markdown-converter-microsoft
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill markitdown-document-to-markdown-converter-microsoft -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill markitdown-document-to-markdown-converter-microsoft -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill markitdown-document-to-markdown-converter-microsoft -a codex
```

### OpenClaw

```bash
clawhub install markitdown-document-to-markdown-converter-microsoft
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markitdown-document-to-markdown-converter-microsoft/)
