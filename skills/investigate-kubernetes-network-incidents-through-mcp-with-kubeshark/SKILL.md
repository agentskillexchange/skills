---
title: "Investigate Kubernetes network incidents through MCP with Kubeshark"
description: "Query live and historical Kubernetes network traffic through Kubeshark’s MCP server when an agent needs packet-level evidence, API payloads, or service-path traces for incident response."
verification: "security_reviewed"
source: "https://github.com/kubeshark/kubeshark"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "kubeshark/kubeshark"
  github_stars: 11873
---

# Investigate Kubernetes network incidents through MCP with Kubeshark

Use Kubeshark when an agent needs direct access to Kubernetes network evidence instead of guessing from logs alone. Kubeshark captures and indexes L4 and L7 traffic with Kubernetes context, exposes that data through MCP, and lets the agent ask focused questions about failed requests, service-to-service paths, TLS traffic, and retrospective packet captures.

Invoke it during root cause analysis, degraded API investigations, and cross-service incident response, especially when the important signal lives in the network path rather than in one workload’s logs. The scope boundary is tight: this skill is about querying captured cluster traffic and exporting targeted evidence through Kubeshark’s MCP tools, not about being a general observability platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/investigate-kubernetes-network-incidents-through-mcp-with-kubeshark/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/investigate-kubernetes-network-incidents-through-mcp-with-kubeshark
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/investigate-kubernetes-network-incidents-through-mcp-with-kubeshark`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-kubernetes-network-incidents-through-mcp-with-kubeshark/)
