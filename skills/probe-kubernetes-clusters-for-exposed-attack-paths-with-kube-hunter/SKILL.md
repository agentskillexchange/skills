---
name: "Probe Kubernetes clusters for exposed attack paths with kube-hunter"
slug: "probe-kubernetes-clusters-for-exposed-attack-paths-with-kube-hunter"
description: "Assess a Kubernetes cluster from the attacker viewpoint when an agent needs exposure-focused findings instead of a general cluster scanner listing."
github_stars: 5040
verification: "security_reviewed"
source: "https://github.com/aquasecurity/kube-hunter"
author: "Aqua Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-hunter"
  github_stars: 5040
---

# Probe Kubernetes clusters for exposed attack paths with kube-hunter

Assess a Kubernetes cluster from the attacker viewpoint when an agent needs exposure-focused findings instead of a general cluster scanner listing.

## Prerequisites

kube-hunter binary or container image and network or cluster access to the target environment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kube-hunter from release artifacts or run the published container image, then execute an appropriate scan mode such as remote probing or in-cluster discovery and review the reported findings before any remediation step.
```

## Documentation

- https://github.com/aquasecurity/kube-hunter#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-kubernetes-clusters-for-exposed-attack-paths-with-kube-hunter/)
