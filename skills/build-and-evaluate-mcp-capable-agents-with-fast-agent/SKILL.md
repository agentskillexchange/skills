---
title: "Build and evaluate MCP-capable agents with fast-agent"
description: "Scaffold, run, inspect, and evaluate model-agnostic agents that connect to MCP servers, skills, shell tools, and workflow packs."
verification: "security_reviewed"
source: "https://github.com/evalstate/fast-agent"
author: "evalstate"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "evalstate/fast-agent"
  github_stars: 3807
---

# Build and evaluate MCP-capable agents with fast-agent

Scaffold, run, inspect, and evaluate model-agnostic agents that connect to MCP servers, skills, shell tools, and workflow packs.

## Prerequisites

Python, uv, fast-agent-mcp, target model provider, optional MCP servers

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with uv tool install -U fast-agent-mcp or run uvx fast-agent-mcp@latest -x. Use fast-agent scaffold or fast-agent go, connect MCP servers with /connect, select a model, and run or evaluate the configured agent workflow.
```

## Documentation

- https://fast-agent.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-evaluate-mcp-capable-agents-with-fast-agent/)
