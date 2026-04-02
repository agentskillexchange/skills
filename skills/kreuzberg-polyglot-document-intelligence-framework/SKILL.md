---
name: "Kreuzberg Polyglot Document Intelligence Framework with Rust Core"
description: "Kreuzberg is a high-performance document intelligence framework with a Rust core that extracts text, metadata, images, and structured information from 91+ file formats including PDFs, Office documents, images, and archives. It provides native bindings for 12 programming languages and can be deployed as a library, CLI, REST API, or MCP server."
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
source: "https://github.com/kreuzberg-dev/kreuzberg"
verification: "listed"
---

# Kreuzberg Polyglot Document Intelligence Framework with Rust Core

Kreuzberg is a polyglot document intelligence framework built around a high-performance Rust core. It extracts text, metadata, images, and structured information from over 91 file formats across 8 major categories, without requiring a GPU. The framework supports native bindings for Rust, Python, TypeScript/Node.js, Ruby, Go, Java, C#, PHP, Elixir, R, and C.

## Architecture and Performance

The Rust core provides native PDFium integration, SIMD optimizations, and full parallelism for high-throughput document processing. Streaming parsers handle multi-gigabyte files with minimal memory overhead. The TOON wire format provides token-efficient serialization for LLM and RAG pipelines, reducing token count by 30-50% compared to JSON.

## Format Coverage

Kreuzberg processes word processing documents (.docx, .odt, .pages), spreadsheets (.xlsx, .xls, .ods, .numbers), presentations (.pptx, .key), PDFs with OCR support, ebooks (.epub, .fb2), HTML/XML, email formats, archives, and programming source files. Code intelligence extracts functions, classes, imports, symbols, and docstrings from 248 programming languages via tree-sitter integration.

## OCR Support

Multiple OCR backends are supported: Tesseract (including Tesseract-WASM for browsers), PaddleOCR, and EasyOCR (Python). The plugin system allows custom OCR backends, validators, post-processors, document extractors, and renderers to be added.

## Deployment Options

Kreuzberg can be used as a library in any supported language, as a CLI tool for batch processing, as a REST API server, or as an MCP server for AI agent integration. Official Docker images are available in Core (~1.0-1.3GB) and Full (~1.0-1.3GB with OCR and legacy format support) variants.

## Embeddings

With ONNX Runtime 1.24+, Kreuzberg provides built-in embeddings generation for extracted content, enabling direct integration with vector databases and semantic search pipelines.

## Installation

Install as an agent skill using one of these methods:

### OpenClaw
```bash
openclaw skill install kreuzberg-polyglot-document-intelligence-framework
```

### Claude Code
```bash
claude mcp add kreuzberg-polyglot-document-intelligence-framework
```

### Cursor / Windsurf
Add to your `.cursor/skills/` or `.windsurf/skills/` directory.

### Manual Install
```bash
# Python
pip install kreuzberg

# Node.js
npm install @kreuzberg/node

# Rust
cargo add kreuzberg

# CLI
curl -sSL https://kreuzberg.dev/install.sh | sh

# Docker
docker pull ghcr.io/kreuzberg-dev/kreuzberg
```

### ChatGPT
Import this skill via the Agent Skill Exchange.

## Source

- [Kreuzberg on GitHub](https://github.com/kreuzberg-dev/kreuzberg)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/kreuzberg-polyglot-document-intelligence-framework/)
