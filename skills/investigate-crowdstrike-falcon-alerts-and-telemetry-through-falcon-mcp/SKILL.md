---
title: "Investigate CrowdStrike Falcon alerts and telemetry through falcon-mcp"
description: "falcon-mcp gives an MCP-compatible agent a bounded CrowdStrike investigation workflow. It can pull detections and incidents, inspect host and identity telemetry, query threat intelligence, and use modules like Real Time Response for read-oriented triage steps before an analyst escalates or contains an issue. That makes it useful when the job is understanding what happened in Falcon and gathering the right evidence quickly.\nThe scope boundary is clear enough to be skill-shaped: this is not a generic CrowdStrike product listing or a broad SecOps platform card. Invoke it when the agent needs Falcon-native investigation and telemetry retrieval inside an MCP session, not when the user just wants to browse Falcon normally or adopt a general-purpose security stack."
verification: security_reviewed
source: "https://github.com/CrowdStrike/falcon-mcp"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-crowdstrike-falcon-alerts-and-telemetry-through-falcon-mcp/)
