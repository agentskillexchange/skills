---
title: "Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto"
description: "Scan Helm charts, YAML, or live clusters for Kubernetes API versions scheduled for removal before an upgrade window."
verification: "listed"
source: "https://github.com/FairwindsOps/pluto"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "FairwindsOps/pluto"
  github_stars: 2494
---

# Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto

Use Pluto when an agent needs to answer a very specific upgrade-safety question: which Kubernetes resources still rely on APIs that are deprecated or removed in newer cluster versions. The agent can inspect raw manifests, Helm output, or live resources and convert the findings into a migration checklist before maintenance begins. Invoke this instead of using the product normally when the job is pre-upgrade compatibility review, not generic Kubernetes management or policy enforcement. The scope boundary is tight: deprecated-API detection for upgrade readiness.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-deprecated-kubernetes-apis-in-manifests-and-live-resources-before-upgrades-with-pluto/)
