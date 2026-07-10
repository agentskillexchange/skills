---
title: "Parse multilingual documents for agent ingestion with dots.ocr"
description: "Use dots.ocr when an agent needs repeatable multilingual document layout parsing before retrieval, extraction, review, or downstream automation."
verification: "security_reviewed"
source: "https://github.com/rednote-hilab/dots.ocr"
author: "rednote-hilab"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "rednote-hilab/dots.ocr"
  github_stars: 8932
---

# Parse multilingual documents for agent ingestion with dots.ocr

Use dots.ocr when an agent needs repeatable multilingual document layout parsing before retrieval, extraction, review, or downstream automation.

## Prerequisites

Python, vLLM or Hugging Face Transformers, dots.mocr model weights

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/rednote-hilab/dots.ocr, create the documented Python 3.12 environment, install PyTorch for the target CUDA runtime, run `pip install -e .`, download model weights with `python3 tools/download_model.py`, then deploy through vLLM or run parser commands such as `python3 dots_mocr/parser.py demo/demo_pdf1.pdf --num_thread 64`.
```

## Documentation

- https://github.com/rednote-hilab/dots.ocr

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-multilingual-documents-for-agent-ingestion-with-dots-ocr/)
