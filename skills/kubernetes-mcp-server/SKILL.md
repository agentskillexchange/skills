---
name: "Kubernetes MCP Server"
description: "Use this skill when you need to inspect Kubernetes cluster state, list pods, check deployment status, view logs, or apply manifest changes from your AI agent. It gives agents kubectl-like capabilities to manage workloads and diagnose cluster issues without direct cluster access."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes MCP Server

Use this skill when you need to inspect Kubernetes cluster state, list pods, check deployment status, view logs, or apply manifest changes from your AI agent. It gives agents kubectl-like capabilities to manage workloads and diagnose cluster issues without direct cluster access.

## Overview

Use this skill when you need to inspect Kubernetes cluster state, list pods, check deployment status, view logs, or apply manifest changes from your AI agent. It gives agents kubectl-like capabilities to manage workloads and diagnose cluster issues without direct cluster access.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-mcp-server/
