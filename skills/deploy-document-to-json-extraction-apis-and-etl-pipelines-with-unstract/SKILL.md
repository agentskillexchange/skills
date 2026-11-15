---
name: "Deploy document-to-JSON extraction APIs and ETL pipelines with Unstract"
slug: "deploy-document-to-json-extraction-apis-and-etl-pipelines-with-unstract"
description: "Use Unstract when an operator needs agents or automation pipelines to turn recurring PDFs, scans, and document batches into structured JSON through prompt-defined extraction workflows."
github_stars: 6661
verification: "security_reviewed"
source: "https://github.com/Zipstack/unstract"
author: "Zipstack"
publisher_type: "open_source"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Zipstack/unstract"
  github_stars: 6661
---

# Deploy document-to-JSON extraction APIs and ETL pipelines with Unstract

Use Unstract when an operator needs agents or automation pipelines to turn recurring PDFs, scans, and document batches into structured JSON through prompt-defined extraction workflows.

## Prerequisites

Unstract platform; Docker and Docker Compose; Git; LLM provider credentials; target document source; optional API, ETL, MCP, or n8n integration

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/Zipstack/unstract.git

Requirements and caveats from upstream:
- <a href="https://hub.docker.com/u/unstract"><img src="https://img.shields.io/docker/pulls/unstract/backend" alt="Docker Pulls"></a>
- <img src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FZipstack%2Funstract%2Frefs%2Fheads%2Fmain%2Fpyproject.toml" alt="Python Version from PEP 621 TOML">
- **n8n Node** — Drop into existing automation workflows. [Docs →](https://docs.unstract.com/unstract/unstract_platform/api_deployment/unstract_api_deployment_n8n_custom_node/)

Basic usage or getting-started notes:
- | Deployment | Custom infrastructure | ./run-platform.sh or managed cloud |
- ./run-platform.sh
- ./run-platform.sh -v v0.1.0

- Source: https://github.com/Zipstack/unstract
- Extracted from upstream docs: https://raw.githubusercontent.com/Zipstack/unstract/HEAD/README.md

## Documentation

- https://docs.unstract.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-document-to-json-extraction-apis-and-etl-pipelines-with-unstract/)
