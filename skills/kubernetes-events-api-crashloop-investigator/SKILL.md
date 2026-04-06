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

Choose the installation path that fits your setup:

1. Install from Agent Skill Exchange in the OpenClaw UI.
2. Copy the skill folder into your local skills directory.
3. Add it to your shared workspace skills collection.
4. Install it through a compatible agent skill manager.
5. Clone or download the upstream source and wire it into your agent runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
