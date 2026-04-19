---
title: "Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp"
description: "falcon-mcp gives an MCP-compatible agent a bounded CrowdStrike investigation workflow. It can pull detections and incidents, inspect host and identity telemetry, query threat intelligence, and use modules like Real Time Response for read-oriented triage steps before an analyst escalates or contains an issue. That makes it useful when the job is understanding what happened in Falcon and gathering the right evidence quickly. The scope boundary is clear enough to be skill-shaped: this is not a generic CrowdStrike product listing or a broad SecOps platform card. Invoke it when the agent needs Falcon-native investigation and telemetry retrieval inside an MCP session, not when the user just wants to browse Falcon normally or adopt a general-purpose security stack."
source: "https://github.com/CrowdStrike/falcon-mcp"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "CrowdStrike/falcon-mcp"
  github_stars: 136
---

# Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp

falcon-mcp gives an MCP-compatible agent a bounded CrowdStrike investigation workflow. It can pull detections and incidents, inspect host and identity telemetry, query threat intelligence, and use modules like Real Time Response for read-oriented triage steps before an analyst escalates or contains an issue. That makes it useful when the job is understanding what happened in Falcon and gathering the right evidence quickly. The scope boundary is clear enough to be skill-shaped: this is not a generic CrowdStrike product listing or a broad SecOps platform card. Invoke it when the agent needs Falcon-native investigation and telemetry retrieval inside an MCP session, not when the user just wants to browse Falcon normally or adopt a general-purpose security stack.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp/)
