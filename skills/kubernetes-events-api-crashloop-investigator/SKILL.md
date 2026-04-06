---
title: "Kubernetes Events API CrashLoop Investigator"
slug: "kubernetes-events-api-crashloop-investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks &amp; Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121439
---

# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

Choose whichever method fits your setup:

1. Browse and install from Agent Skill Exchange.
2. Clone or download the upstream project manually.
3. Use the project package manager or installer if available.
4. Copy the skill into your local skills directory.
5. Follow the upstream documentation for environment-specific setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
