---
title: "Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete"
description: "Use cargo-machete when an agent needs to find and remove unused Rust dependencies before they keep inflating build time, review noise, and manifest drift."
verification: "security_reviewed"
source: "https://github.com/bnjbvr/cargo-machete"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bnjbvr/cargo-machete"
  github_stars: 1280
  npm_package: "cargo-machete"
  npm_weekly_downloads: 2073590
---

# Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete

Tool: cargo-machete. This skill gives an agent a narrow maintenance job: inspect a Rust project for dependencies that are declared but no longer used, then produce a cleanup candidate list for safe manifest pruning. When to use it: invoke this before release, dependency refreshes, or cleanup passes when a Rust repository may have accumulated stale crates over time. Using this skill is different from using the product normally because the workflow is targeted: scan for unused dependencies, verify the findings, and hand back a minimal cleanup patch instead of generic package-management advice. Scope boundary: this is not a generic Cargo listing and not a broad dependency-management platform card. Its boundary is specific: detect unused Rust dependencies so the repository can be slimmed down with cargo-machete.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete/)
