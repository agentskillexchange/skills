---
title: "Push, pull, and attach non-container OCI artifacts in registries with ORAS"
description: "Use ORAS to move SBOMs, model bundles, provenance, and other non-container artifacts through OCI registries without wrapping them as conventional images."
verification: "listed"
source: "https://github.com/oras-project/oras"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oras-project/oras"
  github_stars: 2213
---

# Push, pull, and attach non-container OCI artifacts in registries with ORAS

ORAS gives an agent a clean workflow for pushing, pulling, and attaching non-container artifacts to OCI registries. Invoke this when you need to store or retrieve SBOMs, attestations, model bundles, or related metadata in the same registry ecosystem as container delivery, but the job is not traditional image build or runtime management.

The scope boundary is specific: registry-native artifact packaging and attachment workflows for OCI-compatible registries. This is not a generic registry product listing or a full container platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/push-pull-and-attach-non-container-oci-artifacts-in-registries-with-oras/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/push-pull-and-attach-non-container-oci-artifacts-in-registries-with-oras
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/push-pull-and-attach-non-container-oci-artifacts-in-registries-with-oras`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/push-pull-and-attach-non-container-oci-artifacts-in-registries-with-oras/)
