---
title: "Score Kubernetes manifests for reliability and security risks before deploy with kube-score"
description: "Use kube-score to statically review Kubernetes YAML or rendered Helm output for rollout risks, weak defaults, and resilience gaps before merge or deploy."
verification: listed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score/)
