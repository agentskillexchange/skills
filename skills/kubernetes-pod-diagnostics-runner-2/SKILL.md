---
name: "Kubernetes Pod Diagnostics Runner"
slug: "kubernetes-pod-diagnostics-runner-2"
description: "Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server."
github_stars: 121700
verification: "listed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostics Runner

Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/)
