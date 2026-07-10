---
title: "Deploy Kubernetes-native agents with kagent"
description: "Define agents, model configs, and MCP tool servers as Kubernetes resources so cloud operators can run controlled infrastructure workflows in-cluster."
verification: "listed"
source: "https://github.com/kagent-dev/kagent"
author: "kagent"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kagent-dev/kagent"
  github_stars: 2911
---

# Deploy Kubernetes-native agents with kagent

Define agents, model configs, and MCP tool servers as Kubernetes resources so cloud operators can run controlled infrastructure workflows in-cluster.

## Prerequisites

Kubernetes cluster, kubectl, Helm, kagent, MCP tool servers, supported LLM provider

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the kagent installation guide, install kagent into a Kubernetes cluster, configure a ModelConfig for the selected provider, define ToolServers for the infrastructure tools the agent may use, and create an Agent resource for the bounded operations workflow.
```

## Documentation

- https://kagent.dev/docs/kagent/getting-started/quickstart

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-kubernetes-native-agents-with-kagent/)
