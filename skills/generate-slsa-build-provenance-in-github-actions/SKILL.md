---
title: "Generate SLSA build provenance in GitHub Actions"
description: "Use this skill when an agent needs to harden a GitHub Actions release pipeline by generating provenance attestations for build artifacts. It fits teams that already build in GitHub Actions and want downstream verification or policy enforcement. Invoke it instead of using the SLSA GitHub Generator as a raw project when the task is operational: add the workflow step, choose the supported generator path, produce provenance, and confirm the emitted attestation matches the built artifact. This is skill-shaped because the scope is narrowly about provenance generation inside GitHub Actions. It is not a generic SLSA framework listing."
source: "https://github.com/slsa-framework/slsa-github-generator"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "slsa-framework/slsa-github-generator"
  github_stars: 566
---

# Generate SLSA build provenance in GitHub Actions

Use this skill when an agent needs to harden a GitHub Actions release pipeline by generating provenance attestations for build artifacts. It fits teams that already build in GitHub Actions and want downstream verification or policy enforcement. Invoke it instead of using the SLSA GitHub Generator as a raw project when the task is operational: add the workflow step, choose the supported generator path, produce provenance, and confirm the emitted attestation matches the built artifact. This is skill-shaped because the scope is narrowly about provenance generation inside GitHub Actions. It is not a generic SLSA framework listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-slsa-build-provenance-in-github-actions/)
