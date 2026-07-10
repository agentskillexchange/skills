---
title: "Build OCR and layout-analysis preprocessing pipelines with deepdoctection"
description: "Use deepdoctection when an agent workflow needs a local Python pipeline for document layout analysis, OCR, table recognition, and page-level extraction before LLM ingestion."
verification: "security_reviewed"
source: "https://github.com/deepdoctection/deepdoctection"
author: "deepdoctection"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "deepdoctection/deepdoctection"
  github_stars: 3177
---

# Build OCR and layout-analysis preprocessing pipelines with deepdoctection

Use deepdoctection when an agent workflow needs a local Python pipeline for document layout analysis, OCR, table recognition, and page-level extraction before LLM ingestion.

## Prerequisites

Python environment; deepdoctection package; selected OCR/layout/model dependencies; local PDFs or scanned document images

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install deepdoctection using the official documentation, configure the OCR and model backends required for the target documents, create an analyzer with dd.get_dd_analyzer() or a custom pipeline, and run analyzer.analyze(path=...) to produce page-level text, layout, table, and diagnostic outputs.
```

## Documentation

- https://deepdoctection.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-ocr-and-layout-analysis-preprocessing-pipelines-with-deepdoctection/)
