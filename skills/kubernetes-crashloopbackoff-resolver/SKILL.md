---
title: "Kubernetes CrashLoopBackOff Resolver"
slug: "kubernetes-crashloopbackoff-resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs &#8211;previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs &#8211;previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
