---
title: "Kubernetes Events API CrashLoop Investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category: ["Runbooks &amp; Diagnostics"]
framework: ["MCP"]
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121439
---

# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI.
2. Add it through your agent or assistant skill manager.
3. Clone or copy this skill into your local skills directory.
4. Install with a package manager if the upstream project provides one.
5. Follow the upstream project documentation for manual setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
