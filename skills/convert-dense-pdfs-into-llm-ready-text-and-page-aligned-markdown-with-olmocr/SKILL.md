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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a clean Python environment, install required PDF rendering dependencies, then install the package with pip install olmocr for remote inference or pip install olmocr[gpu] for local GPU inference.
```

## Documentation

- https://github.com/allenai/olmocr#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr/)
