---
title: "Kubernetes CrashLoop Diagnoser"
slug: "kubernetes-crashloop-diagnoser-agent"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
