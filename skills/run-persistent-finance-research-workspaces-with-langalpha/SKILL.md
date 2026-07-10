---
name: "Run persistent finance research workspaces with LangAlpha"
slug: "run-persistent-finance-research-workspaces-with-langalpha"
description: "Create persistent investment-research workspaces where agents process market data, filings, models, charts, and thesis updates over time."
github_stars: 1175
verification: "security_reviewed"
source: "https://github.com/ginlix-ai/LangAlpha"
author: "ginlix-ai"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ginlix-ai/LangAlpha"
  github_stars: 1175
---

# Run persistent finance research workspaces with LangAlpha

Create persistent investment-research workspaces where agents process market data, filings, models, charts, and thesis updates over time.

## Prerequisites

Python 3.12+, LangAlpha backend and web or CLI/TUI, configured model credentials, optional financial data provider keys and MCP servers

## Installation

Use the upstream install or setup path that matches your environment:
- All tiers are enabled by default. To run with **free data only** (Yahoo Finance), run make config with prompted selection. You can also edit agent_config.yaml manually.
- git clone https://github.com/ginlix-ai/langalpha.git
- make config # interactive wizard — creates .env, configures LLM, data sources, sandbox, and search
- make up # starts PostgreSQL, Redis, backend, and frontend

Requirements and caveats from upstream:
- <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python 3.12+" />
- **Programmatic Tool Calling (PTC)** — The agent writes and executes Python to process financial data from mcp servers instead of pouring raw data into the LLM context window, enabling complex multi-step analysis while...
- LLM["LLM"] -- "1 — Writes Python" --> EC["ExecuteCode Tool"]

Basic usage or getting-started notes:
- <a href="#getting-started">Getting Started</a> &bull;
- EC -- "2 — Sends to sandbox" --> Run["Code Runner"]
- Run -- "3 — import tools.*" --> Wrappers["Generated Wrappers<br/>One module per MCP server"]

- Source: https://github.com/ginlix-ai/LangAlpha
- Extracted from upstream docs: https://raw.githubusercontent.com/ginlix-ai/LangAlpha/HEAD/README.md

## Documentation

- https://github.com/ginlix-ai/LangAlpha

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-persistent-finance-research-workspaces-with-langalpha/)
