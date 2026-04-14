---
title: "Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp"
description: "Use falcon-mcp when an agent needs CrowdStrike Falcon detections, incidents, behaviors, threat intel, or read-only response context to triage a security event without leaving an MCP workflow."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp/)
