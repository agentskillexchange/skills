---
title: "Convert mixed documents into agent-ready Markdown and JSON with DocStrange"
description: "Convert PDFs, scans, office files, images, and URLs into clean Markdown, structured JSON, CSV, or HTML before an agent ingests or reviews the content."
verification: "security_reviewed"
source: "https://github.com/NanoNets/docstrange"
author: "NanoNets"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "NanoNets/docstrange"
  github_stars: 1489
  npm_package: "docstrange"
  npm_weekly_downloads: 90
---

# Convert mixed documents into agent-ready Markdown and JSON with DocStrange

Convert PDFs, scans, office files, images, and URLs into clean Markdown, structured JSON, CSV, or HTML before an agent ingests or reviews the content.

## Prerequisites

Python 3.8+, docstrange package, optional CUDA GPU for local processing, optional MCP-compatible client or local web UI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install docstrange` for library use. For the local web UI, install with `pip install "docstrange[web]"` and run `docstrange web` or `python -m docstrange.web_app`. Choose cloud mode for managed processing or GPU mode for local/private document conversion.
```

## Documentation

- https://docstrange.nanonets.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-mixed-documents-into-agent-ready-markdown-and-json-with-docstrange/)
