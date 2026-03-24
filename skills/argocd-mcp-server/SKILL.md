---
name: "ArgoCD MCP Server"
description: "Use this skill when you need to deploy applications via ArgoCD, check sync status, roll back deployments, or view application health from your AI agent. It connects to ArgoCD’s API to give agents full GitOps deployment control without requiring kubectl access."
category: "Developer Tools"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "argocd"  # from ase_tool_match
  github_stars: 22391  # from ase_github_stars (integer, not string)
  github_repo: "argoproj/argo-cd"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ArgoCD MCP Server

Use this skill when you need to deploy applications via ArgoCD, check sync status, roll back deployments, or view application health from your AI agent. It connects to ArgoCD’s API to give agents full GitOps deployment control without requiring kubectl access.

## Overview

Use this skill when you need to deploy applications via ArgoCD, check sync status, roll back deployments, or view application health from your AI agent. It connects to ArgoCD’s API to give agents full GitOps deployment control without requiring kubectl access.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install argocd-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/argocd-mcp-server/
