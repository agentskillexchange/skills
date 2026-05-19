---
name: "Dispatch coding agents from GitHub issue labels and return pull requests with Patchwork Agents"
slug: "dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents"
description: "Use issue labels as a lightweight dispatch layer that fans repository work out to Claude Code, Codex, or Aider workers and brings back PRs."
github_stars: 0
verification: "security_reviewed"
source: "https://github.com/hey-intent/patchwork-agents"
author: "hey-intent"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hey-intent/patchwork-agents"
  github_stars: 0
---

# Dispatch coding agents from GitHub issue labels and return pull requests with Patchwork Agents

Use issue labels as a lightweight dispatch layer that fans repository work out to Claude Code, Codex, or Aider workers and brings back PRs.

## Prerequisites

GitHub App or webhook setup, Kubernetes or k3s environment, supported coding-agent credentials, repository access, Patchwork Agents deployment

## Installation

Use the upstream install or setup path that matches your environment:
- docker build -f images/orchestrator/Dockerfile -t ghcr.io/<your-org>/orchestrator:latest .
- docker save ghcr.io/<your-org>/orchestrator:latest | sudo k3s ctr images import -
- docker build -f images/worker-claude/Dockerfile -t worker-claude:latest .
- docker save worker-claude:latest | sudo k3s ctr images import -

Requirements and caveats from upstream:
- Tested on: VPS / 8 GB RAM / 4 vCPU / k3s single-node.
- ### 1. Prerequisites
- **Manual option**: k3s, Docker, and kubectl installed on the VPS

Basic usage or getting-started notes:
- A VPS (or machine) with 4 vCPU / 8 GB RAM minimum
- API keys for your desired AI worker providers
- **Ansible option**: ansible installed locally + SSH root access to the VPS

- Source: https://github.com/hey-intent/patchwork-agents
- Extracted from upstream docs: https://raw.githubusercontent.com/hey-intent/patchwork-agents/HEAD/README.md

## Documentation

- https://github.com/hey-intent/patchwork-agents

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents/)
