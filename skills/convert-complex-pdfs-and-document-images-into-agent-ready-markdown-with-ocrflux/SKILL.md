---
name: "Convert complex PDFs and document images into agent-ready Markdown with OCRFlux"
slug: "convert-complex-pdfs-and-document-images-into-agent-ready-markdown-with-ocrflux"
description: "Use OCRFlux when agents need local PDF or image parsing into Markdown/JSONL with layout-aware OCR, table handling, and cross-page paragraph or table merging."
github_stars: 2514
verification: "security_reviewed"
source: "https://github.com/chatdoc-com/OCRFlux"
author: "ChatDOC"
publisher_type: "open_source"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "chatdoc-com/OCRFlux"
  github_stars: 2514
---

# Convert complex PDFs and document images into agent-ready Markdown with OCRFlux

Use OCRFlux when agents need local PDF or image parsing into Markdown/JSONL with layout-aware OCR, table handling, and cross-page paragraph or table merging.

## Prerequisites

Python 3.11, conda, NVIDIA GPU, vLLM, poppler-utils, OCRFlux-3B model

## Installation

Use the upstream install or setup path that matches your environment:
- conda create -n ocrflux python=3.11
- conda activate ocrflux
- git clone https://github.com/chatdoc-com/OCRFlux.git
- pip install -e . --find-links https://flashinfer.ai/whl/cu124/torch2.5/flashinfer/

Requirements and caveats from upstream:
- are difficult to install in an existing python environment, so please do make a clean python environment to install into.
- python -m ocrflux.pipeline ./localworkspace --data test.pdf --model /model_dir/OCRFlux-3B
- python -m ocrflux.pipeline ./localworkspace --data test_page.png --model /model_dir/OCRFlux-3B

Basic usage or getting-started notes:
- Based on a 3B parameter VLM, so it can run even on GTX 3090 GPU.
- Then for the merging task, if the elements to be merged are paragraphs, we can just concate them. However, for two table fragments, their merging is much more challenging. For example, the table spanning multiple page...
- [OCRFlux-bench-cross](https://huggingface.co/datasets/ChatDOC/OCRFlux-bench-cross): Containing 1000 samples (500 English samples and 500 Chinese samples), each sample contains the Markdown element lists of two consecu...

- Source: https://github.com/chatdoc-com/OCRFlux
- Extracted from upstream docs: https://raw.githubusercontent.com/chatdoc-com/OCRFlux/HEAD/README.md

## Documentation

- https://github.com/chatdoc-com/OCRFlux

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-complex-pdfs-and-document-images-into-agent-ready-markdown-with-ocrflux/)
