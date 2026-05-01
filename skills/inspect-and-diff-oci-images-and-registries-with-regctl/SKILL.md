---
title: "Inspect and diff OCI images and registries with regctl"
description: "Use regctl when an agent needs to inspect manifests, compare image contents, or debug registry state without pulling whole images locally first."
verification: "listed"
source: "https://github.com/regclient/regclient"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "regclient/regclient"
  github_stars: 1813
---

# Inspect and diff OCI images and registries with regctl

regctl gives agents an operator-grade registry workflow: inspect OCI image metadata, diff tags or manifests, copy artifacts, and debug registry state with explicit commands. Invoke it when the job is image and registry inspection, not when you just need to build containers or browse a registry UI. The boundary is clear: OCI registry diagnostics and artifact comparison, not a generic container platform or broad DevOps product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/inspect-and-diff-oci-images-and-registries-with-regctl/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inspect-and-diff-oci-images-and-registries-with-regctl
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/inspect-and-diff-oci-images-and-registries-with-regctl`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-diff-oci-images-and-registries-with-regctl/)
