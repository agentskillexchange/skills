---
name: "Convert mixed documents into agent-ready Markdown and JSON with DocStrange"
slug: "convert-mixed-documents-into-agent-ready-markdown-and-json-with-docstrange"
description: "Convert PDFs, scans, office files, images, and URLs into clean Markdown, structured JSON, CSV, or HTML before an agent ingests or reviews the content."
github_stars: 1489
verification: "security_reviewed"
source: "https://github.com/NanoNets/docstrange"
author: "NanoNets"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "NanoNets/docstrange"
  github_stars: 1489
  npm_package: "docstrange"
  npm_weekly_downloads: 90
---

# Convert mixed documents into agent-ready Markdown and JSON with DocStrange

Convert PDFs, scans, office files, images, and URLs into clean Markdown, structured JSON, CSV, or HTML before an agent ingests or reviews the content.

## Prerequisites

Python 3.8+, docstrange package, optional CUDA GPU for local processing, optional MCP-compatible client or local web UI

## Installation

Use the upstream install or setup path that matches your environment:
- pip install "docstrange[web]"
- pip install -e ".[web]"
- pip install Flask
- git clone https://github.com/nanonets/docstrange.git

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/pypi/pyversions/docstrange.svg)](https://pypi.org/project/docstrange/)
- DocStrange is a Python library for converting a wide range of document formats—including **PDF**, **DOCX**, **PPTX**, **XLSX**, and **images** — into clean, usable data. It produces LLM-optimized **Markdown**, structu...
- python -m docstrange.web_app

Basic usage or getting-started notes:
- The library offers both a powerful cloud API and a 100% private, offline mode that runs locally on your GPU. Developed by **Nanonets**, DocStrange is built on a powerful pipeline of OCR and layout detection models and...
- **Example outputs: Here's a quick preview of the quality of output**
- 💡 Want a GUI? Run the simple, drag-and-drop local web interface for private, offline document conversion.

- Source: https://github.com/NanoNets/docstrange
- Extracted from upstream docs: https://raw.githubusercontent.com/NanoNets/docstrange/HEAD/README.md

## Documentation

- https://docstrange.nanonets.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-mixed-documents-into-agent-ready-markdown-and-json-with-docstrange/)
