---
title: "Inspect and diff OCI images and registries with regctl"
description: "regctl gives agents an operator-grade registry workflow: inspect OCI image metadata, diff tags or manifests, copy artifacts, and debug registry state with explicit commands. Invoke it when the job is image and registry inspection, not when you just need to build containers or browse a registry UI. The boundary is clear: OCI registry diagnostics and artifact comparison, not a generic container platform or broad DevOps product card."
verification: listed
source: "https://github.com/regclient/regclient"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "regclient/regclient"
  github_stars: 1813
---

# Inspect and diff OCI images and registries with regctl

regctl gives agents an operator-grade registry workflow: inspect OCI image metadata, diff tags or manifests, copy artifacts, and debug registry state with explicit commands. Invoke it when the job is image and registry inspection, not when you just need to build containers or browse a registry UI. The boundary is clear: OCI registry diagnostics and artifact comparison, not a generic container platform or broad DevOps product card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inspect-and-diff-oci-images-and-registries-with-regctl
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/inspect-and-diff-oci-images-and-registries-with-regctl` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-diff-oci-images-and-registries-with-regctl/)
