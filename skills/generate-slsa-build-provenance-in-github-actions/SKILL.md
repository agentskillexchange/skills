---
title: "Generate SLSA build provenance in GitHub Actions"
description: "Attach signed SLSA provenance to GitHub Actions builds so release artifacts ship with verifiable supply-chain metadata."
verification: listed
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

Use this skill when an agent needs to harden a GitHub Actions release pipeline by generating provenance attestations for build artifacts. It fits teams that already build in GitHub Actions and want downstream verification or policy enforcement.

Invoke it instead of using the SLSA GitHub Generator as a raw project when the task is operational: add the workflow step, choose the supported generator path, produce provenance, and confirm the emitted attestation matches the built artifact.

This is skill-shaped because the scope is narrowly about provenance generation inside GitHub Actions. It is not a generic SLSA framework listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-slsa-build-provenance-in-github-actions
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-slsa-build-provenance-in-github-actions` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-slsa-build-provenance-in-github-actions/)
