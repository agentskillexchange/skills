---
title: "Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp"
description: "Use falcon-mcp when an agent needs CrowdStrike Falcon detections, incidents, behaviors, threat intel, or read-only response context to triage a security event without leaving an MCP workflow."
verification: "security_reviewed"
source: "https://github.com/CrowdStrike/falcon-mcp"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "CrowdStrike/falcon-mcp"
  github_stars: 136
---

# Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp

falcon-mcp gives an MCP-compatible agent a bounded CrowdStrike investigation workflow. It can pull detections and incidents, inspect host and identity telemetry, query threat intelligence, and use modules like Real Time Response for read-oriented triage steps before an analyst escalates or contains an issue. That makes it useful when the job is understanding what happened in Falcon and gathering the right evidence quickly.

The scope boundary is clear enough to be skill-shaped: this is not a generic CrowdStrike product listing or a broad SecOps platform card. Invoke it when the agent needs Falcon-native investigation and telemetry retrieval inside an MCP session, not when the user just wants to browse Falcon normally or adopt a general-purpose security stack.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp/)
