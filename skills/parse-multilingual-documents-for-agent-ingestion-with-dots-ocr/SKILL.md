---
name: "Parse multilingual documents for agent ingestion with dots.ocr"
slug: "parse-multilingual-documents-for-agent-ingestion-with-dots-ocr"
description: "Use dots.ocr when an agent needs repeatable multilingual document layout parsing before retrieval, extraction, review, or downstream automation."
github_stars: 8932
verification: "security_reviewed"
source: "https://github.com/rednote-hilab/dots.ocr"
author: "rednote-hilab"
publisher_type: "open_source"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "rednote-hilab/dots.ocr"
  github_stars: 8932
---

# Parse multilingual documents for agent ingestion with dots.ocr

Use dots.ocr when an agent needs repeatable multilingual document layout parsing before retrieval, extraction, review, or downstream automation.

## Prerequisites

Python, vLLM or Hugging Face Transformers, dots.mocr model weights

## Installation

Use the upstream install or setup path that matches your environment:
- conda create -n dots_mocr python=3.12
- conda activate dots_mocr
- git clone https://github.com/rednote-hilab/dots.mocr.git
- pip install -e .

Requirements and caveats from upstream:
- [OCRVerse](https://github.com/DocTron-hub/OCRVerse) results are derived from various code formats (e.g., SVG, Python), whereas results for Gemini 3 Pro and dots.mocr are based specifically on SVG code.
- If you have trouble with the installation, try our [Docker Image](https://hub.docker.com/r/rednotehilab/dots.ocr) for an easier setup, and follow these steps:
- We highly recommend using vLLM for deployment and inference. **Since vLLM version 0.11.0, Dots OCR has been officially integrated into vLLM with verified performance** and you can use vLLM docker image directly (e.g,...

Basic usage or getting-started notes:
- cd dots.mocr
- 💡**Note:** Please use a directory name without periods (e.g., DotsMOCR instead of dots.mocr) for the model save path. This is a temporary workaround pending our integration with Transformers.
- python3 tools/download_model.py

- Source: https://github.com/rednote-hilab/dots.ocr
- Extracted from upstream docs: https://raw.githubusercontent.com/rednote-hilab/dots.ocr/HEAD/README.md

## Documentation

- https://github.com/rednote-hilab/dots.ocr

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-multilingual-documents-for-agent-ingestion-with-dots-ocr/)
