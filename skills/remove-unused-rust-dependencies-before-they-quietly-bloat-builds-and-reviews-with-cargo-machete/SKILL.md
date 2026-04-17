---
title: "Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete"
description: "Tool: cargo-machete. This skill gives an agent a narrow maintenance job: inspect a Rust project for dependencies that are declared but no longer used, then produce a cleanup candidate list for safe manifest pruning.\nWhen to use it: invoke this before release, dependency refreshes, or cleanup passes when a Rust repository may have accumulated stale crates over time. Using this skill is different from using the product normally because the workflow is targeted: scan for unused dependencies, verify the findings, and hand back a minimal cleanup patch instead of generic package-management advice.\nScope boundary: this is not a generic Cargo listing and not a broad dependency-management platform card. Its boundary is specific: detect unused Rust dependencies so the repository can be slimmed down with cargo-machete."
verification: security_reviewed
source: "https://github.com/bnjbvr/cargo-machete"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bnjbvr/cargo-machete"
  github_stars: 1280
  ase_npm_package: "cargo-machete"
  npm_weekly_downloads: 2073590
---

# Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete

Tool: cargo-machete. This skill gives an agent a narrow maintenance job: inspect a Rust project for dependencies that are declared but no longer used, then produce a cleanup candidate list for safe manifest pruning.
When to use it: invoke this before release, dependency refreshes, or cleanup passes when a Rust repository may have accumulated stale crates over time. Using this skill is different from using the product normally because the workflow is targeted: scan for unused dependencies, verify the findings, and hand back a minimal cleanup patch instead of generic package-management advice.
Scope boundary: this is not a generic Cargo listing and not a broad dependency-management platform card. Its boundary is specific: detect unused Rust dependencies so the repository can be slimmed down with cargo-machete.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete/)
