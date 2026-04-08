---
title: "Kubernetes Events API CrashLoop Investigator"
slug: "kubernetes-events-api-crashloop-investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121439
---

# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
