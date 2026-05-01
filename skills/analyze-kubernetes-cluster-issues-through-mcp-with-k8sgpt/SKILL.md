---
title: "Analyze Kubernetes cluster issues through MCP with K8sGPT"
description: "Run K8sGPT as an MCP server so an agent can scan a Kubernetes cluster, explain unhealthy resources, and return prioritized remediation clues in natural language."
verification: "security_reviewed"
source: "https://github.com/k8sgpt-ai/k8sgpt"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "k8sgpt-ai/k8sgpt"
  github_stars: 7687
---

# Analyze Kubernetes cluster issues through MCP with K8sGPT

Use K8sGPT when an agent needs a fast diagnostic pass over a Kubernetes cluster before a human starts manually stitching together events, failing resources, and likely causes. K8sGPT analyzes cluster objects, explains findings in plain language, and can expose that workflow through an MCP server for Claude Desktop and other MCP-compatible clients.

Invoke it for outage triage, failed rollout review, and namespace health checks when the job is to summarize what is broken and why. The scope boundary is specific: this skill is about running K8sGPT analysis and explanation flows via its MCP surface, not about general cluster administration or a generic Kubernetes product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt/)
