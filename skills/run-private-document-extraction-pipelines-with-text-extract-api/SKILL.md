---
name: "Run private document extraction pipelines with Text Extract API"
slug: "run-private-document-extraction-pipelines-with-text-extract-api"
description: "Use Text Extract API when an agent needs to turn PDFs, Office files, or images into Markdown or structured JSON with local OCR, optional Ollama models, PII removal, and queued batch processing."
github_stars: 3111
verification: "security_reviewed"
source: "https://github.com/CatchTheTornado/text-extract-api"
author: "CatchTheTornado"
publisher_type: "open_source"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "CatchTheTornado/text-extract-api"
  github_stars: 3111
---

# Run private document extraction pipelines with Text Extract API

Use Text Extract API when an agent needs to turn PDFs, Office files, or images into Markdown or structured JSON with local OCR, optional Ollama models, PII removal, and queued batch processing.

## Prerequisites

Python, FastAPI, Celery, Redis, Docker, Ollama, OCR backend

## Installation

Use the upstream install or setup path that matches your environment:
- [Download and install Docker](https://www.docker.com/products/docker-desktop/)
- git clone https://github.com/CatchTheTornado/text-extract-api.git
- pip install -e .
- brew update && brew install libmagic poppler pkg-config ghostscript ffmpeg automake autoconf

Requirements and caveats from upstream:
- **No Cloud/external dependencies** all you need: PyTorch based OCR (EasyOCR) + Ollama are shipped and configured via docker-compose no data is sent outside your dev/server environment,
- python client/cli.py ocr_upload --file examples/example-mri.pdf --prompt_file examples/example-mri-2-json-prompt.txt
- python client/cli.py ocr_upload --file examples/example-invoice.pdf --prompt_file examples/example-invoice-remove-pii.txt

Basic usage or getting-started notes:
- Before running the example see [getting started](#getting-started)
- ![Converting MRI report to Markdown](./screenshots/example-1.png)
- ![Converting Invoice to JSON](./screenshots/example-2.png)

- Source: https://github.com/CatchTheTornado/text-extract-api
- Extracted from upstream docs: https://raw.githubusercontent.com/CatchTheTornado/text-extract-api/HEAD/README.md

## Documentation

- https://github.com/CatchTheTornado/text-extract-api

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-private-document-extraction-pipelines-with-text-extract-api/)
