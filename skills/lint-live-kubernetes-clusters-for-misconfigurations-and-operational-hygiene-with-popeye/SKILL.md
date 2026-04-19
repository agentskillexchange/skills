---
title: "Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye"
description: "Use Popeye when an agent needs to review the current health and hygiene of a running Kubernetes cluster rather than only validate YAML before apply. The agent scans live resources, flags common operational problems, and turns those findings into a prioritized cleanup list for cluster owners. Invoke this instead of using the product normally when the task is cluster-state review and remediation planning, not generic Kubernetes browsing or platform administration. The boundary is the live-cluster lint workflow itself."
source: "https://github.com/derailed/popeye"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "derailed/popeye"
  github_stars: 6262
---

# Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye

Use Popeye when an agent needs to review the current health and hygiene of a running Kubernetes cluster rather than only validate YAML before apply. The agent scans live resources, flags common operational problems, and turns those findings into a prioritized cleanup list for cluster owners. Invoke this instead of using the product normally when the task is cluster-state review and remediation planning, not generic Kubernetes browsing or platform administration. The boundary is the live-cluster lint workflow itself.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/)
