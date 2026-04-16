---
title: "Lint live Kubernetes clusters for misconfigurations and operational hygiene with Popeye"
description: "Inspect a live Kubernetes cluster for unhealthy resource settings, missing probes, and other operational smells."
verification: "listed"
source: "https://github.com/derailed/popeye"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-live-kubernetes-clusters-for-misconfigurations-and-operational-hygiene-with-popeye/)
