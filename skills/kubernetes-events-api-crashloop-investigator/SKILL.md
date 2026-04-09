---
title: "Kubernetes Events API CrashLoop Investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
slug: "kubernetes-events-api-crashloop-investigator"
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
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
2. Add as a local skill folder
3. Install from a Git repository
4. Install via package manager if supported
5. Copy the skill into your OpenClaw skills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
