---
title: "Deploy document-to-JSON extraction APIs and ETL pipelines with Unstract"
description: "Use Unstract when an operator needs agents or automation pipelines to turn recurring PDFs, scans, and document batches into structured JSON through prompt-defined extraction workflows."
verification: "security_reviewed"
source: "https://github.com/Zipstack/unstract"
author: "Zipstack"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Zipstack/unstract"
  github_stars: 6661
---

# Deploy document-to-JSON extraction APIs and ETL pipelines with Unstract

Use Unstract when an operator needs agents or automation pipelines to turn recurring PDFs, scans, and document batches into structured JSON through prompt-defined extraction workflows.

## Prerequisites

Unstract platform; Docker and Docker Compose; Git; LLM provider credentials; target document source; optional API, ETL, MCP, or n8n integration

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/Zipstack/unstract, run ./run-platform.sh, open the local Unstract frontend, configure provider credentials, define the extraction prompt/schema in Prompt Studio, then deploy as a REST API or ETL pipeline using the official Unstract docs.
```

## Documentation

- https://docs.unstract.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-document-to-json-extraction-apis-and-etl-pipelines-with-unstract/)
