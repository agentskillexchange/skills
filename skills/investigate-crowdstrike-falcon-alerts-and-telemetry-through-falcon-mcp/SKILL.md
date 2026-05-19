---
name: "Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp"
slug: "investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp"
description: "Use falcon-mcp when an agent needs CrowdStrike Falcon detections, incidents, behaviors, threat intel, or read-only response context to triage a security event without leaving an MCP workflow."
github_stars: 136
verification: "security_reviewed"
source: "https://github.com/CrowdStrike/falcon-mcp"
author: "CrowdStrike"
publisher_type: "company"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "CrowdStrike/falcon-mcp"
  github_stars: 136
---

# Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp

Use falcon-mcp when an agent needs CrowdStrike Falcon detections, incidents, behaviors, threat intel, or read-only response context to triage a security event without leaving an MCP workflow.

## Prerequisites

Python 3.10+ with uv or pip; CrowdStrike Falcon API credentials with the scopes required for the enabled modules; an MCP-compatible client such as Claude Code, Claude Desktop, Cursor, or OpenClaw.

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install falcon-mcp
- pip install falcon-mcp
- docker pull quay.io/crowdstrike/falcon-mcp:latest
- docker run -i --rm --env-file /path/to/.env quay.io/crowdstrike/falcon-mcp:latest

Requirements and caveats from upstream:
- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/falcon-mcp)](https://pypi.org/project/falcon-mcp/)
- ### Docker
- "falcon-mcp-docker": {

Basic usage or getting-started notes:
- | [Sensor Usage](https://crowdstrike.github.io/falcon-mcp/modules/sensor-usage/) | Access and analyze sensor usage data |
- #### Using uv (recommended)
- bash

- Source: https://github.com/CrowdStrike/falcon-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/CrowdStrike/falcon-mcp/HEAD/README.md

## Documentation

- https://github.com/CrowdStrike/falcon-mcp/tree/main/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp/)
