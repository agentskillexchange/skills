---
title: "Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto"
description: "Scan Helm charts, YAML, or live clusters for Kubernetes API versions scheduled for removal before an upgrade window."
verification: "listed"
source: "https://github.com/FairwindsOps/pluto"
author: "FairwindsOps"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "FairwindsOps/pluto"
  github_stars: 2494
---

# Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto

Scan Helm charts, YAML, or live clusters for Kubernetes API versions scheduled for removal before an upgrade window.

## Prerequisites

Kubernetes manifests or cluster access, Pluto binary

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Pluto from a release or package manager, then run commands such as `pluto detect-files`, `pluto detect-helm`, or `pluto detect` for live cluster checks.
```

## Documentation

- https://pluto.docs.fairwinds.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-deprecated-kubernetes-apis-in-manifests-and-live-resources-before-upgrades-with-pluto/)
