---
title: "Marker PDF-to-Markdown Converter"
description: "Marker converts PDF, DOCX, PPTX, and image files to clean Markdown, JSON, and HTML with high accuracy. It handles tables, equations, code blocks, and multi-column layouts, with optional LLM-boosted extraction for maximum fidelity."
verification: "security_reviewed"
source: "https://github.com/datalab-to/marker"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "datalab-to/marker"
  github_stars: 33237
---

# Marker PDF-to-Markdown Converter

Marker is an open-source document conversion tool that transforms PDF, DOCX, PPTX, XLSX, HTML, EPUB, and image files into clean Markdown, JSON, chunks, or HTML output. Built by Datalab (formerly VikParuchuri/marker), it has become one of the most widely adopted PDF-to-Markdown converters in the AI and data engineering ecosystem.


The core pipeline uses a combination of OCR, layout detection, and reading-order analysis to parse complex document structures. Marker handles multi-column layouts, nested tables, inline and block-level math (LaTeX), code blocks, footnotes, headers/footers, and embedded images. It automatically removes artifacts like page numbers and watermarks, producing output suitable for downstream NLP pipelines, RAG systems, or LLM context windows.


For higher accuracy, Marker supports an LLM-boosted mode (--use_llm) that uses Gemini or Ollama models to merge tables across pages, properly format complex tables, handle inline math conversion, and extract form values. Benchmarks show this combined mode outperforms both standalone Marker and standalone Gemini on table extraction tasks.


Installation is straightforward via pip install marker-pdf, with optional extras for non-PDF formats. Marker runs on GPU (CUDA), CPU, or Apple MPS, and includes a Streamlit demo app for interactive testing. Batch processing on an H100 achieves approximately 25 pages per second. The tool also supports structured extraction given a JSON schema (beta), making it useful for data extraction workflows that require typed output fields.


Marker integrates naturally into AI agent pipelines as a preprocessing step: feed documents in, get structured Markdown out, then pass to LLMs for summarization, Q&A, or analysis. It is available on PyPI as marker-pdf and the source code is hosted on GitHub under GPL license with a commercial option.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/marker-pdf-to-markdown-converter/)
