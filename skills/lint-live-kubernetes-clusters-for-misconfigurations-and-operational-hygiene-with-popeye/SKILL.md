---
title: "Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye"
description: "Use Popeye when an agent needs to review the current health and hygiene of a running Kubernetes cluster rather than only validate YAML before apply. The agent scans live resources, flags common operational problems, and turns those findings into a prioritized cleanup list for cluster owners. Invoke this instead of using the product normally when the task is cluster-state review and remediation planning, not generic Kubernetes browsing or platform administration. The boundary is the live-cluster lint workflow itself."
verification: listed
source: "https://github.com/derailed/popeye"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "derailed/popeye"
  github_stars: 6262
---

# Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye

Use Popeye when an agent needs to review the current health and hygiene of a running Kubernetes cluster rather than only validate YAML before apply. The agent scans live resources, flags common operational problems, and turns those findings into a prioritized cleanup list for cluster owners. Invoke this instead of using the product normally when the task is cluster-state review and remediation planning, not generic Kubernetes browsing or platform administration. The boundary is the live-cluster lint workflow itself.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/)
