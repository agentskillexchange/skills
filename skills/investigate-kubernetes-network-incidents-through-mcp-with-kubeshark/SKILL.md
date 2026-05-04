---
title: "Investigate Kubernetes network incidents through MCP with Kubeshark"
description: "Query live and historical Kubernetes network traffic through Kubeshark’s MCP server when an agent needs packet-level evidence, API payloads, or service-path traces for incident response."
verification: "security_reviewed"
source: "https://github.com/kubeshark/kubeshark"
author: "Kubeshark"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "kubeshark/kubeshark"
  github_stars: 11873
---

# Investigate Kubernetes network incidents through MCP with Kubeshark

Query live and historical Kubernetes network traffic through Kubeshark’s MCP server when an agent needs packet-level evidence, API payloads, or service-path traces for incident response.

## Prerequisites

Kubeshark deployed in the target Kubernetes cluster and an MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Kubeshark in the cluster with Helm (for example: helm repo add kubeshark https://helm.kubeshark.com && helm install kubeshark kubeshark/kubeshark --set mcp.enabled=true --set mcp.port=8898), then connect an MCP client to the Kubeshark MCP endpoint.
```

## Documentation

- https://docs.kubeshark.com/en/mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-kubernetes-network-incidents-through-mcp-with-kubeshark/)
