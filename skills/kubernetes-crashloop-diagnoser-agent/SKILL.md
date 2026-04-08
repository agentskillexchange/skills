---
title: "Kubernetes CrashLoop Diagnoser"
slug: "kubernetes-crashloop-diagnoser-agent"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/"
---

# Kubernetes CrashLoop Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
