---
name: "Convert dense PDFs into LLM-ready text and page-aligned markdown with olmOCR"
slug: "convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr"
description: "Use olmOCR when an agent needs to turn scanned or layout-heavy documents into clean markdown or text before chunking, search, extraction, or citation workflows."
github_stars: 17135
verification: "security_reviewed"
source: "https://github.com/allenai/olmocr"
author: "Allen Institute for AI"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "allenai/olmocr"
  github_stars: 17135
---

# Convert dense PDFs into LLM-ready text and page-aligned markdown with olmOCR

Use olmOCR when an agent needs to turn scanned or layout-heavy documents into clean markdown or text before chunking, search, extraction, or citation workflows.

## Prerequisites

Python 3.11, pip or conda, poppler-utils, optional NVIDIA GPU for local inference

## Installation

Use the upstream install or setup path that matches your environment:
- conda create -n olmocr python=3.11
- conda activate olmocr
- pip install olmocr
- pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128

Requirements and caveats from upstream:
- (Based on a 7B parameter VLM, so it requires a GPU)
- June 17, 2025 - v0.1.75 - Switch from sglang to vllm based inference pipeline, updated docker image to CUDA 12.8.
- May 23, 2025 - v0.1.70 - Official docker support and images are now available! [See Docker usage](#using-docker)

Basic usage or getting-started notes:
- #### System Dependencies
- You will need to install poppler-utils and additional fonts for rendering PDF images.
- bash

- Source: https://github.com/allenai/olmocr
- Extracted from upstream docs: https://raw.githubusercontent.com/allenai/olmocr/HEAD/README.md

## Documentation

- https://github.com/allenai/olmocr#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr/)
