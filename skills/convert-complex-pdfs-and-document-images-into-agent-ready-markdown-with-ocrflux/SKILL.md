---
title: "Convert complex PDFs and document images into agent-ready Markdown with OCRFlux"
description: "Use OCRFlux when agents need local PDF or image parsing into Markdown/JSONL with layout-aware OCR, table handling, and cross-page paragraph or table merging."
verification: "security_reviewed"
source: "https://github.com/chatdoc-com/OCRFlux"
author: "ChatDOC"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "chatdoc-com/OCRFlux"
  github_stars: 2514
---

# Convert complex PDFs and document images into agent-ready Markdown with OCRFlux

Use OCRFlux when agents need local PDF or image parsing into Markdown/JSONL with layout-aware OCR, table handling, and cross-page paragraph or table merging.

## Prerequisites

Python 3.11, conda, NVIDIA GPU, vLLM, poppler-utils, OCRFlux-3B model

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install system dependencies such as poppler-utils, poppler-data, Microsoft core fonts, Croscore fonts, gsfonts, and lcdf-typetools. Create a clean environment with `conda create -n ocrflux python=3.11`, activate it, clone `https://github.com/chatdoc-com/OCRFlux.git`, then run `pip install -e . --find-links https://flashinfer.ai/whl/cu124/torch2.5/flashinfer/`. Download or mount the OCRFlux-3B model before running the pipeline.
```

## Documentation

- https://github.com/chatdoc-com/OCRFlux

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-complex-pdfs-and-document-images-into-agent-ready-markdown-with-ocrflux/)
