---
title: "Parse agent-ready PDFs and document images with MonkeyOCR"
description: "Run MonkeyOCR over PDFs, scanned pages, formulas, and tables to produce structured Markdown/text that downstream agents can ingest and reason over."
verification: "security_reviewed"
source: "https://github.com/Yuliang-Liu/MonkeyOCR"
author: "Yuliang-Liu"
publisher_type: "individual"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Yuliang-Liu/MonkeyOCR"
  github_stars: 6595
---

# Parse agent-ready PDFs and document images with MonkeyOCR

Run MonkeyOCR over PDFs, scanned pages, formulas, and tables to produce structured Markdown/text that downstream agents can ingest and reason over.

## Prerequisites

Python environment, CUDA-capable GPU or supported inference backend, Hugging Face Hub or ModelScope access for model weights, PDF or image documents to parse

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream install guide, download model weights with `python tools/download_model.py -n MonkeyOCR-pro-3B` or another documented model name, then run `python parse.py input_path` with optional flags such as `-o ./output`, `-g 20`, `-s`, or `-t text/formula/table` for the parsing mode.
```

## Documentation

- https://github.com/Yuliang-Liu/MonkeyOCR

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-agent-ready-pdfs-and-document-images-with-monkeyocr/)
