---
title: "Use MCP Context Forge as an MCP gateway and registry"
description: "Put a governed gateway in front of MCP, A2A, REST, and gRPC tools so agent calls can be discovered, routed, observed, and controlled."
verification: "security_reviewed"
source: "https://github.com/IBM/mcp-context-forge"
author: "IBM"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "IBM/mcp-context-forge"
  github_stars: 3812
---

# Use MCP Context Forge as an MCP gateway and registry

Put a governed gateway in front of MCP, A2A, REST, and gRPC tools so agent calls can be discovered, routed, observed, and controlled.

## Prerequisites

Python 3.11+, Docker optional, MCP-compatible clients, optional PostgreSQL or Redis for production-style deployment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For development, clone the repository and run `make venv install-dev` followed by `make serve` to start the gateway on port 4444. Alternative documented setup uses `uv venv && source .venv/bin/activate && uv pip install -e '.[dev]'` or the published container image.
```

## Documentation

- https://ibm.github.io/mcp-context-forge

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-mcp-context-forge-as-an-mcp-gateway-and-registry/)
