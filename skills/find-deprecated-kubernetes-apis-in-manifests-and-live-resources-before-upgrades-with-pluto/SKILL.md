---
title: "Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto"
description: "Use Pluto when an agent needs to answer a very specific upgrade-safety question: which Kubernetes resources still rely on APIs that are deprecated or removed in newer cluster versions. The agent can inspect raw manifests, Helm output, or live resources and convert the findings into a migration checklist before maintenance begins. Invoke this instead of using the product normally when the job is pre-upgrade compatibility review, not generic Kubernetes management or policy enforcement. The scope boundary is tight: deprecated-API detection for upgrade readiness."
source: "https://github.com/FairwindsOps/pluto"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "FairwindsOps/pluto"
  github_stars: 2494
---

# Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto

Use Pluto when an agent needs to answer a very specific upgrade-safety question: which Kubernetes resources still rely on APIs that are deprecated or removed in newer cluster versions. The agent can inspect raw manifests, Helm output, or live resources and convert the findings into a migration checklist before maintenance begins. Invoke this instead of using the product normally when the job is pre-upgrade compatibility review, not generic Kubernetes management or policy enforcement. The scope boundary is tight: deprecated-API detection for upgrade readiness.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-deprecated-kubernetes-apis-in-manifests-and-live-resources-before-upgrades-with-pluto/)
