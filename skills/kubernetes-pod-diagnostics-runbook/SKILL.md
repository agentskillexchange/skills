---
name: "Kubernetes Pod Diagnostics Runbook"
slug: "kubernetes-pod-diagnostics-runbook"
description: "Automates Kubernetes troubleshooting using kubectl and the Kubernetes Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states. Collects pod logs, events, node conditions, and resource quotas systematically."
github_stars: 121700
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostics Runbook

Automates Kubernetes troubleshooting using kubectl and the Kubernetes Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states. Collects pod logs, events, node conditions, and resource quotas systematically.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/kubernetes/kubernetes
- make
- make quick-release

Requirements and caveats from upstream:
- ##### You have a working [Docker environment].
- [Docker environment]: https://docs.docker.com/engine

- Source: https://github.com/kubernetes/kubernetes
- Extracted from upstream docs: https://raw.githubusercontent.com/kubernetes/kubernetes/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/)
