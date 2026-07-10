---
title: "Run private document extraction pipelines with Text Extract API"
description: "Use Text Extract API when an agent needs to turn PDFs, Office files, or images into Markdown or structured JSON with local OCR, optional Ollama models, PII removal, and queued batch processing."
verification: "security_reviewed"
source: "https://github.com/CatchTheTornado/text-extract-api"
author: "CatchTheTornado"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "CatchTheTornado/text-extract-api"
  github_stars: 3111
---

# Run private document extraction pipelines with Text Extract API

Use Text Extract API when an agent needs to turn PDFs, Office files, or images into Markdown or structured JSON with local OCR, optional Ollama models, PII removal, and queued batch processing.

## Prerequisites

Python, FastAPI, Celery, Redis, Docker, Ollama, OCR backend

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/CatchTheTornado/text-extract-api, copy .env.localhost.example to .env.localhost, install Docker and Ollama, then run make install and make run. For manual setup, create a Python virtualenv, run pip install -e ., start the service, and run a Celery worker before submitting files with python client/cli.py ocr_upload.
```

## Documentation

- https://github.com/CatchTheTornado/text-extract-api

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-private-document-extraction-pipelines-with-text-extract-api/)
