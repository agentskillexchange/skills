---
title: "Kubernetes CrashLoopBackOff Resolver"
slug: "kubernetes-crashloopbackoff-resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs -previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/"
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs -previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
