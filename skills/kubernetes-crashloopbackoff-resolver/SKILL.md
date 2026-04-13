---
title: "Kubernetes CrashLoopBackOff Resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/"
category: ["Runbooks &amp; Diagnostics"]
framework: ["Cursor"]
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
