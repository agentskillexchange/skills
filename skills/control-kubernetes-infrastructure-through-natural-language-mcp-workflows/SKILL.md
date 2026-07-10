---
title: "Control Kubernetes infrastructure through natural-language MCP workflows"
description: "Let MCP-compatible agents inspect, debug, deploy, audit, and manage Kubernetes clusters through a controlled kubectl-backed server."
verification: "security_reviewed"
source: "https://github.com/rohitg00/kubectl-mcp-server"
author: "Rohit Ghumare"
publisher_type: "individual"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "rohitg00/kubectl-mcp-server"
  github_stars: 898
  npm_package: "kubectl-mcp-server"
  npm_weekly_downloads: 150
---

# Control Kubernetes infrastructure through natural-language MCP workflows

Let MCP-compatible agents inspect, debug, deploy, audit, and manage Kubernetes clusters through a controlled kubectl-backed server.

## Prerequisites

Node.js or Python, kubectl, Kubernetes cluster access, MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run with npx -y kubectl-mcp-server, install globally with npm install -g kubectl-mcp-server, or install the Python package with pip install kubectl-mcp-server[ui], then register the server with an MCP-compatible client that has access to the intended kubeconfig.
```

## Documentation

- https://github.com/rohitg00/kubectl-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-kubernetes-infrastructure-through-natural-language-mcp-workflows/)
