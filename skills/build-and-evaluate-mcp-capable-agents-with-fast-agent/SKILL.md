---
name: "Build and evaluate MCP-capable agents with fast-agent"
slug: "build-and-evaluate-mcp-capable-agents-with-fast-agent"
description: "Scaffold, run, inspect, and evaluate model-agnostic agents that connect to MCP servers, skills, shell tools, and workflow packs."
github_stars: 3807
verification: "security_reviewed"
source: "https://github.com/evalstate/fast-agent"
author: "evalstate"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "MCP"
tool_ecosystem:
  github_repo: "evalstate/fast-agent"
  github_stars: 3807
---

# Build and evaluate MCP-capable agents with fast-agent

Scaffold, run, inspect, and evaluate model-agnostic agents that connect to MCP servers, skills, shell tools, and workflow packs.

## Prerequisites

Python, uv, fast-agent-mcp, target model provider, optional MCP servers

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install -U fast-agent-mcp
- uv pip install fast-agent-mcp # install fast-agent!
- uv run agent.py # run your first agent
- uv run agent.py --model='o3-mini?reasoning=low' # specify a model

Requirements and caveats from upstream:
- Start by installing the [uv package manager](https://docs.astral.sh/uv/) for Python. Then:
- Windows Users - there are a couple of configuration changes needed for the Filesystem and Docker MCP Servers - necessary changes are detailed within the configuration files.

Basic usage or getting-started notes:
- To start an interactive session with shell support, install [uv](https://astral.sh/uv) and run
- Enter a shell with !, or run shell commands e.g. ! cd web && npm run build.
- fast-agent --model opus -x --smart

- Source: https://github.com/evalstate/fast-agent
- Extracted from upstream docs: https://raw.githubusercontent.com/evalstate/fast-agent/HEAD/README.md

## Documentation

- https://fast-agent.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-evaluate-mcp-capable-agents-with-fast-agent/)
