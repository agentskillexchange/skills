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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/score-kubernetes-manifests-for-reliability-and-security-risks-before-deploy-with-kube-score/)
