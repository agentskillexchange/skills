---
title: "Scan agent workflows for tools, MCP exposure, and adversarial risk with Agentic Radar"
description: "Use Agentic Radar to statically scan agent workflows, map tools and MCP servers, generate shareable security reports, and optionally run adversarial runtime tests before rollout."
verification: "security_reviewed"
source: "https://github.com/splx-ai/agentic-radar"
author: "SPLX AI"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "splx-ai/agentic-radar"
  github_stars: 953
---

# Scan agent workflows for tools, MCP exposure, and adversarial risk with Agentic Radar

Use Agentic Radar to statically scan agent workflows, map tools and MCP servers, generate shareable security reports, and optionally run adversarial runtime tests before rollout.

## Prerequisites

Python, agentic-radar CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install agentic-radar`. For framework-specific extras, use `pip install "agentic-radar[crewai]"` or `pip install "agentic-radar[openai-agents]"` when needed. Run `agentic-radar scan <framework> -i <path> -o report.html` to generate a report, or `agentic-radar test openai-agents "<entrypoint>"` for runtime adversarial testing.
```

## Documentation

- https://github.com/splx-ai/agentic-radar

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-workflows-for-tools-mcp-exposure-and-adversarial-risk-with-agentic-radar/)
