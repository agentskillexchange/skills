---
title: "Run Kubernetes cluster operations through MCP"
description: "Use mcp-server-kubernetes so an MCP-capable agent can inspect, troubleshoot, and manage Kubernetes resources through a configured kubeconfig."
verification: "listed"
source: "https://github.com/Flux159/mcp-server-kubernetes"
author: "Flux159"
publisher_type: "individual"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "Flux159/mcp-server-kubernetes"
  github_stars: 1396
  npm_package: "mcp-server-kubernetes"
  npm_weekly_downloads: 78540
---

# Run Kubernetes cluster operations through MCP

Use mcp-server-kubernetes so an MCP-capable agent can inspect, troubleshoot, and manage Kubernetes resources through a configured kubeconfig.

## Prerequisites

MCP-compatible client, kubectl, valid kubeconfig, Kubernetes cluster access, and optional Helm v3

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Verify kubectl can reach the intended cluster, then add the server to an MCP client. For Claude Code, run claude mcp add kubernetes -- npx mcp-server-kubernetes. For other clients, configure the command npx mcp-server-kubernetes and provide the intended kubeconfig context.
```

## Documentation

- https://github.com/Flux159/mcp-server-kubernetes

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-kubernetes-cluster-operations-through-mcp/)
