---
title: "Convert PDFs and document images into agent-ready Markdown with Docext"
description: "Run Docext locally or with a chosen model backend to turn PDFs and document images into structured Markdown for RAG, extraction, and review workflows."
verification: "security_reviewed"
source: "https://github.com/NanoNets/docext"
author: "Nanonets"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "NanoNets/docext"
  github_stars: 2029
---

# Convert PDFs and document images into agent-ready Markdown with Docext

Run Docext locally or with a chosen model backend to turn PDFs and document images into structured Markdown for RAG, extraction, and review workflows.

## Prerequisites

Python 3.11 environment, Docext package, source PDFs or document images, and a supported VLM backend such as vLLM, Ollama, or a configured hosted model provider

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create and activate a Python 3.11 virtual environment, install Docext from PyPI with pip install docext or uv pip install docext, configure the supported model backend required for the chosen workflow, then run the Docext PDF/image-to-Markdown interface or API described in the PDF2MD_README and EXT_README guides.
```

## Documentation

- https://github.com/NanoNets/docext/blob/main/PDF2MD_README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-pdfs-and-document-images-into-agent-ready-markdown-with-docext/)
