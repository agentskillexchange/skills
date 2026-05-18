---
name: "Kubernetes CrashLoop Diagnoser"
slug: "kubernetes-crashloop-diagnoser-agent"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
github_stars: 121700
verification: "listed"
source: "https://github.com/kubernetes/kubernetes"
author: "kubernetes"
category: "Runbooks & Diagnostics"
framework: "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.

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

## Documentation

- https://kubernetes.io/docs/home/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
