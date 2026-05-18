---
name: "Kubernetes Pod Crash Diagnostician"
slug: "kubernetes-pod-crash-diagnostician"
description: "Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries."
github_stars: 121700
verification: "listed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Diagnostician

Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/)
