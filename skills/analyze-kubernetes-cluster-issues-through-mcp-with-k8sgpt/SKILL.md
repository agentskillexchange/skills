---
title: "Analyze Kubernetes cluster issues through MCP with K8sGPT"
description: "Run K8sGPT as an MCP server so an agent can scan a Kubernetes cluster, explain unhealthy resources, and return prioritized remediation clues in natural language."
verification: "security_reviewed"
source: "https://github.com/k8sgpt-ai/k8sgpt"
author: "K8sGPT Authors"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "k8sgpt-ai/k8sgpt"
  github_stars: 7687
---

# Analyze Kubernetes cluster issues through MCP with K8sGPT

Run K8sGPT as an MCP server so an agent can scan a Kubernetes cluster, explain unhealthy resources, and return prioritized remediation clues in natural language.

## Prerequisites

A reachable Kubernetes cluster, K8sGPT, and an MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install K8sGPT (for example: brew install k8sgpt), configure an AI backend with k8sgpt auth, then start the MCP server with k8sgpt serve --mcp --mcp-http and connect your MCP client.
```

## Documentation

- https://docs.k8sgpt.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt/)
