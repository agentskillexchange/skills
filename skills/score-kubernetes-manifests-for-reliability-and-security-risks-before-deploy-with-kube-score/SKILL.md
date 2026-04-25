---
title: "Score Kubernetes manifests for reliability and security risks before deploy with kube-score"
description: "Use kube-score to statically review Kubernetes YAML or rendered Helm output for rollout risks, weak defaults, and resilience gaps before merge or deploy."
verification: "listed"
source: "https://github.com/zegl/kube-score"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "zegl/kube-score"
  github_stars: 3100
---

# Score Kubernetes manifests for reliability and security risks before deploy with kube-score

Use kube-score when an agent needs to inspect Kubernetes object definitions and surface recommendations about reliability and security before anything reaches a cluster. Invoke this instead of normal Kubernetes tooling when the job is preflight risk review of manifests or chart output, not schema validation alone and not live cluster administration. The scope boundary is specific and skill-shaped: kube-score performs recommendation-oriented static analysis on Kubernetes manifests before deployment, not general Kubernetes management or a generic platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score/)
