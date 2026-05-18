---
name: "Kubernetes Pod Diagnostics"
slug: "kubernetes-pod-diagnostics-skill"
description: "Diagnoses Kubernetes pod failures using kubectl describe, logs --previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations."
github_stars: 121700
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostics

Diagnoses Kubernetes pod failures using kubectl describe, logs --previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-skill/)
