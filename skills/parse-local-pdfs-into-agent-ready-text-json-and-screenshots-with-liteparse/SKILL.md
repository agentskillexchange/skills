---
name: "Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse"
slug: "parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse"
description: "Run LiteParse locally to extract PDF text, spatial JSON, OCR-backed output, and page screenshots before sending documents into an agent workflow."
github_stars: 5136
verification: "security_reviewed"
source: "https://github.com/run-llama/liteparse"
author: "LlamaIndex"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "run-llama/liteparse"
  github_stars: 5136
  npm_package: "@llamaindex/liteparse"
  npm_weekly_downloads: 36959
---

# Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse

Run LiteParse locally to extract PDF text, spatial JSON, OCR-backed output, and page screenshots before sending documents into an agent workflow.

## Prerequisites

Node.js, npm or Homebrew, LiteParse CLI (`lit`), optional OCR server

## Installation

Use the upstream install or setup path that matches your environment:
- npm i -g @llamaindex/liteparse
- brew tap run-llama/liteparse
- brew install llamaindex-liteparse
- git clone https://github.com/run-llama/liteparse.git

Requirements and caveats from upstream:
- scanned PDFs), you'll get significantly better results with [LlamaParse](https://developers.llamaindex.ai/python/cloud/llamaparse/?utm_source=github&utm_medium=liteparse),
- LiteParse's core parsing engine (PDF.js text extraction, grid projection, OCR via Tesseract.js) can run in the browser. Since the library has Node-only dependencies (sharp, fs, child_process), you'll need a bundler li...

Basic usage or getting-started notes:
- [![CI](https://github.com/run-llama/liteparse/actions/workflows/ci.yml/badge.svg)](https://github.com/run-llama/liteparse/actions/workflows/ci.yml)
- ### CLI Tool
- #### Option 1: Global Install (Recommended)

- Source: https://github.com/run-llama/liteparse
- Extracted from upstream docs: https://raw.githubusercontent.com/run-llama/liteparse/HEAD/README.md

## Documentation

- https://developers.llamaindex.ai/liteparse/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse/)
