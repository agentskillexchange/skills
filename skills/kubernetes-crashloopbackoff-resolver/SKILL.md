---
title: "Kubernetes CrashLoopBackOff Resolver"
slug: "kubernetes-crashloopbackoff-resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs --previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
github_stars: 121700
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs --previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
