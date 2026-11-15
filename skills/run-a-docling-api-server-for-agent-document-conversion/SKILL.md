---
name: "Run a Docling API server for agent document conversion"
slug: "run-a-docling-api-server-for-agent-document-conversion"
description: "Deploy Docling API so agents can convert PDFs, Office files, images, HTML, CSV, and other documents into Markdown through sync, batch, and async HTTP endpoints."
github_stars: 1690
verification: "security_reviewed"
source: "https://github.com/drmingler/docling-api"
author: "drmingler"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "drmingler/docling-api"
  github_stars: 1690
---

# Run a Docling API server for agent document conversion

Deploy Docling API so agents can convert PDFs, Office files, images, HTML, CSV, and other documents into Markdown through sync, batch, and async HTTP endpoints.

## Prerequisites

Python 3.12, Poetry, Redis, FastAPI, Celery, optional GPU runtime

## Installation

Install or set up from the source-backed instructions:

Clone `https://github.com/drmingler/docling-api`, run `poetry install`, configure Redis in `.env`, start Redis, then run `poetry run uvicorn main:app --reload --port 8080` and call endpoints such as `/documents/convert`.

- Source: https://github.com/drmingler/docling-api

## Documentation

- https://github.com/drmingler/docling-api

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-a-docling-api-server-for-agent-document-conversion/)
