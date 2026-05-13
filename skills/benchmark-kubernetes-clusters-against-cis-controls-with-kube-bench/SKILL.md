---
title: "Benchmark Kubernetes clusters against CIS controls with kube-bench"
slug: "benchmark-kubernetes-clusters-against-cis-controls-with-kube-bench"
description: "Run CIS benchmark checks against cluster nodes and control planes when an agent needs a narrow Kubernetes hardening audit, not a general platform listing."
github_stars: 8022
verification: "security_reviewed"
source: "https://github.com/aquasecurity/kube-bench"
author: "Aqua Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-bench"
  github_stars: 8022
---

# Benchmark Kubernetes clusters against CIS controls with kube-bench

Run CIS benchmark checks against cluster nodes and control planes when an agent needs a narrow Kubernetes hardening audit, not a general platform listing.

## Prerequisites

kube-bench binary or container image, access to target Kubernetes nodes or cluster context

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kube-bench from releases, Homebrew, or its container image, then run it on a target node or cluster context, for example with `kube-bench run --targets master,node` or the equivalent containerized invocation from the upstream README.
```

## Documentation

- https://github.com/aquasecurity/kube-bench#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-kubernetes-clusters-against-cis-controls-with-kube-bench/)
