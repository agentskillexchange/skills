---
title: "Find deprecated Kubernetes APIs before cluster upgrades with kubent"
slug: "find-deprecated-kubernetes-apis-before-cluster-upgrades-with-kubent"
description: "Scan manifests and live clusters for removed or deprecated Kubernetes APIs before an upgrade window turns into an outage."
github_stars: 3658
verification: "security_reviewed"
source: "https://github.com/doitintl/kube-no-trouble"
author: "doitintl"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "doitintl/kube-no-trouble"
  github_stars: 3658
---

# Find deprecated Kubernetes APIs before cluster upgrades with kubent

Scan manifests and live clusters for removed or deprecated Kubernetes APIs before an upgrade window turns into an outage.

## Prerequisites

kubent binary, access to target Kubernetes manifests or cluster, target Kubernetes version context for upgrade analysis

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kubent from the upstream release or package instructions, point it at the target manifests or cluster, and run the documented scan mode to surface deprecated or removed APIs before the upgrade window.
```

## Documentation

- https://github.com/doitintl/kube-no-trouble#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-deprecated-kubernetes-apis-before-cluster-upgrades-with-kubent/)
