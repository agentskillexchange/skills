---
title: "Operate Kubernetes and OpenShift clusters through MCP"
description: "Expose Kubernetes and OpenShift cluster operations to MCP clients with native API-backed tools for resources, pods, events, Helm, Tekton, and diagnostics."
verification: "security_reviewed"
source: "https://github.com/containers/kubernetes-mcp-server"
author: "containers"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "containers/kubernetes-mcp-server"
  github_stars: 1607
  npm_package: "kubernetes-mcp-server"
  npm_weekly_downloads: 7270
---

# Operate Kubernetes and OpenShift clusters through MCP

Expose Kubernetes and OpenShift cluster operations to MCP clients with native API-backed tools for resources, pods, events, Helm, Tekton, and diagnostics.

## Prerequisites

Access to a Kubernetes or OpenShift cluster, kubeconfig or in-cluster configuration, MCP-compatible client, optional npm, Python, Docker, or native binary install path

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For npm-based clients, add an MCP server command such as npx -y kubernetes-mcp-server@latest. For other environments, use the upstream native binary, Python package, container image, or VS Code/Cursor install links, then configure the server with an approved kubeconfig or in-cluster identity.
```

## Documentation

- https://github.com/containers/kubernetes-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-kubernetes-and-openshift-clusters-through-mcp/)
