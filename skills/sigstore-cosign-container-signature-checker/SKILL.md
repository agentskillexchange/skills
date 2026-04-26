---
title: "Sigstore Cosign Container Signature Checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
verification: "security_reviewed"
source: "https://github.com/sigstore/cosign"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sigstore/cosign"
  github_stars: 5776
---

# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sigstore-cosign-container-signature-checker
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sigstore-cosign-container-signature-checker`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/)
