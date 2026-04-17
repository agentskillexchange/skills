---
title: "Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto"
description: "Use Pluto when an agent needs to answer a very specific upgrade-safety question: which Kubernetes resources still rely on APIs that are deprecated or removed in newer cluster versions. The agent can inspect raw manifests, Helm output, or live resources and convert the findings into a migration checklist before maintenance begins. Invoke this instead of using the product normally when the job is pre-upgrade compatibility review, not generic Kubernetes management or policy enforcement. The scope boundary is tight: deprecated-API detection for upgrade readiness."
verification: listed
source: "https://github.com/FairwindsOps/pluto"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "FairwindsOps/pluto"
  github_stars: 2494
---

# Find deprecated Kubernetes APIs in manifests and live resources before upgrades with Pluto

Use Pluto when an agent needs to answer a very specific upgrade-safety question: which Kubernetes resources still rely on APIs that are deprecated or removed in newer cluster versions. The agent can inspect raw manifests, Helm output, or live resources and convert the findings into a migration checklist before maintenance begins. Invoke this instead of using the product normally when the job is pre-upgrade compatibility review, not generic Kubernetes management or policy enforcement. The scope boundary is tight: deprecated-API detection for upgrade readiness.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/find-deprecated-kubernetes-apis-in-manifests-and-live-resources-before-upgrades-with-pluto
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/find-deprecated-kubernetes-apis-in-manifests-and-live-resources-before-upgrades-with-pluto` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-deprecated-kubernetes-apis-in-manifests-and-live-resources-before-upgrades-with-pluto/)
