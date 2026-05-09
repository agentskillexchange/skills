---
title: Kubernetes CrashLoop Diagnoser
slug: kubernetes-crashloop-diagnoser-agent
description: Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.
github_stars: 121700
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
category: Runbooks & Diagnostics
framework: Gemini
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
---
# Kubernetes CrashLoop Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
