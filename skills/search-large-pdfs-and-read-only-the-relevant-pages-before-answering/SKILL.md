---
name: "Search large PDFs and read only the relevant pages before answering"
slug: "search-large-pdfs-and-read-only-the-relevant-pages-before-answering"
description: "Use pdf-mcp to inspect a PDF, search it, and load only the pages that matter so an agent can answer questions from long documents without brute-forcing the whole file into context."
github_stars: 17
verification: "security_reviewed"
source: "https://github.com/jztan/pdf-mcp"
author: "jztan"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "jztan/pdf-mcp"
  github_stars: 17
  npm_package: "pdf-mcp"
  npm_weekly_downloads: 42
---

# Search large PDFs and read only the relevant pages before answering

Use pdf-mcp to inspect a PDF, search it, and load only the pages that matter so an agent can answer questions from long documents without brute-forcing the whole file into context.

## Prerequisites

Python 3.10+; an MCP-compatible client; local PDFs or accessible PDF URLs; optional extra dependencies for semantic search.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install pdf-mcp
- pip install 'pdf-mcp[semantic]'
- brew install tesseract
- git clone https://github.com/jztan/pdf-mcp.git

Requirements and caveats from upstream:
- [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
- A [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server that enables AI agents to read, search, and extract content from PDF files. Built with Python and PyMuPDF, with SQLite-based caching for persis...
- For OCR on scanned PDFs (requires system Tesseract):

Basic usage or getting-started notes:
- bash
- For semantic search (adds fastembed and numpy, ~67 MB model download on first use):
- # macOS

- Source: https://github.com/jztan/pdf-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/jztan/pdf-mcp/HEAD/README.md

## Documentation

- https://github.com/jztan/pdf-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-large-pdfs-and-read-only-the-relevant-pages-before-answering/)
