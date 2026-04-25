---
title: "Generate SLSA build provenance in GitHub Actions"
description: "Attach signed SLSA provenance to GitHub Actions builds so release artifacts ship with verifiable supply-chain metadata."
verification: "listed"
source: "https://github.com/slsa-framework/slsa-github-generator"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "slsa-framework/slsa-github-generator"
  github_stars: 566
---

# Generate SLSA build provenance in GitHub Actions

Use this skill when an agent needs to harden a GitHub Actions release pipeline by generating provenance attestations for build artifacts. It fits teams that already build in GitHub Actions and want downstream verification or policy enforcement. Invoke it instead of using the SLSA GitHub Generator as a raw project when the task is operational: add the workflow step, choose the supported generator path, produce provenance, and confirm the emitted attestation matches the built artifact. This is skill-shaped because the scope is narrowly about provenance generation inside GitHub Actions. It is not a generic SLSA framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/generate-slsa-build-provenance-in-github-actions/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-slsa-build-provenance-in-github-actions
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/generate-slsa-build-provenance-in-github-actions`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-slsa-build-provenance-in-github-actions/)
