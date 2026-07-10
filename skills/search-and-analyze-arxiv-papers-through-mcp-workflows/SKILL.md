---
name: "Search and analyze arXiv papers through MCP workflows"
slug: "search-and-analyze-arxiv-papers-through-mcp-workflows"
description: "Connect an MCP-capable assistant to arXiv search, paper download, local paper storage, and research prompts for grounded literature review workflows."
github_stars: 2760
verification: "security_reviewed"
source: "https://github.com/blazickjp/arxiv-mcp-server"
author: "blazickjp"
publisher_type: "individual"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "blazickjp/arxiv-mcp-server"
  github_stars: 2760
---

# Search and analyze arXiv papers through MCP workflows

Connect an MCP-capable assistant to arXiv search, paper download, local paper storage, and research prompts for grounded literature review workflows.

## Prerequisites

Python 3.11+, uv or supported MCP bundle installer, MCP-compatible client such as Claude Desktop, VS Code, Kiro, or another stdio MCP host

## Installation

Use the upstream install or setup path that matches your environment:
- uv pip install -e ".[pro]"

Requirements and caveats from upstream:
- [![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
- python
- Read the full text of a locally downloaded paper in markdown. **Requires download_paper to be called first.** Use start and max_chars with the returned next_start value to page through large papers.

Basic usage or getting-started notes:
- example, instructing it to exfiltrate data, invoke other tools with unintended
- asks you to run commands or visit external URLs that were not part of your
- Run the test suite:

- Source: https://github.com/blazickjp/arxiv-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/blazickjp/arxiv-mcp-server/HEAD/README.md

## Documentation

- https://github.com/blazickjp/arxiv-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-analyze-arxiv-papers-through-mcp-workflows/)
