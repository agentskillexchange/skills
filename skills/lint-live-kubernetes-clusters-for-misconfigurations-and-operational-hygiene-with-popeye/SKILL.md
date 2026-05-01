---
title: "Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye"
description: "Inspect a live Kubernetes cluster for unhealthy resource settings, missing probes, and other operational smells."
verification: "listed"
source: "https://github.com/derailed/popeye"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "derailed/popeye"
  github_stars: 6262
---

# Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye

Use Popeye when an agent needs to review the current health and hygiene of a running Kubernetes cluster rather than only validate YAML before apply. The agent scans live resources, flags common operational problems, and turns those findings into a prioritized cleanup list for cluster owners. Invoke this instead of using the product normally when the task is cluster-state review and remediation planning, not generic Kubernetes browsing or platform administration. The boundary is the live-cluster lint workflow itself.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/)
