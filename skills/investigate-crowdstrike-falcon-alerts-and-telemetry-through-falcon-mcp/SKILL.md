---
title: "Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp"
description: "Use falcon-mcp when an agent needs CrowdStrike Falcon detections, incidents, behaviors, threat intel, or read-only response context to triage a security event without leaving an MCP workflow."
verification: "security_reviewed"
source: "https://github.com/CrowdStrike/falcon-mcp"
author: "CrowdStrike"
publisher_type: "company"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "CrowdStrike/falcon-mcp"
  github_stars: 136
---

# Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp

Use falcon-mcp when an agent needs CrowdStrike Falcon detections, incidents, behaviors, threat intel, or read-only response context to triage a security event without leaving an MCP workflow.

## Prerequisites

Python 3.10+ with uv or pip; CrowdStrike Falcon API credentials with the scopes required for the enabled modules; an MCP-compatible client such as Claude Code, Claude Desktop, Cursor, or OpenClaw.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with uv tool install falcon-mcp or pip install falcon-mcp, set the required Falcon API credentials in your environment or .env file, then run falcon-mcp for stdio transport or add flags like --transport sse or --transport streamable-http when you need a networked deployment.
```

## Documentation

- https://github.com/CrowdStrike/falcon-mcp/tree/main/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp/)
