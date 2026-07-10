---
name: "Kubernetes Pod Crash Analyzer"
slug: "kubernetes-pod-crash-analyzer-3"
description: "Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically."
github_stars: 121700
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Analyzer

Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/)
