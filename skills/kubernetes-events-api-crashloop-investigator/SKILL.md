---
title: "Kubernetes Events API CrashLoop Investigator"
slug: "kubernetes-events-api-crashloop-investigator"
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121439
---
# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
