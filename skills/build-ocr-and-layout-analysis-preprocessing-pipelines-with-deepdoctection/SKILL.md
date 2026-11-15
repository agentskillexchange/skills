---
name: "Build OCR and layout-analysis preprocessing pipelines with deepdoctection"
slug: "build-ocr-and-layout-analysis-preprocessing-pipelines-with-deepdoctection"
description: "Use deepdoctection when an agent workflow needs a local Python pipeline for document layout analysis, OCR, table recognition, and page-level extraction before LLM ingestion."
github_stars: 3177
verification: "security_reviewed"
source: "https://github.com/deepdoctection/deepdoctection"
author: "deepdoctection"
publisher_type: "open_source"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "deepdoctection/deepdoctection"
  github_stars: 3177
---

# Build OCR and layout-analysis preprocessing pipelines with deepdoctection

Use deepdoctection when an agent workflow needs a local Python pipeline for document layout analysis, OCR, table recognition, and page-level extraction before LLM ingestion.

## Prerequisites

Python environment; deepdoctection package; selected OCR/layout/model dependencies; local PDFs or scanned document images

## Installation

Use the upstream install or setup path that matches your environment:
- uv pip install timm # needed for the default setup
- uv pip install transformers
- uv pip install python-doctr
- uv pip install deepdoctection

Requirements and caveats from upstream:
- **deep**doctection is a Python library that orchestrates Scan and PDF document layout analysis, OCR and document
- python
- Python >= 3.10

Basic usage or getting-started notes:
- and token classification. Build and run a pipeline for your document extraction tasks, develop your own document
- The following example shows how to use the built-in analyzer to decompose a PDF document into its layout structures.
- ![requirements](https://github.com/deepdoctection/deepdoctection/raw/master/docs/_imgs/install_01.png)

- Source: https://github.com/deepdoctection/deepdoctection
- Extracted from upstream docs: https://raw.githubusercontent.com/deepdoctection/deepdoctection/HEAD/README.md

## Documentation

- https://deepdoctection.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-ocr-and-layout-analysis-preprocessing-pipelines-with-deepdoctection/)
