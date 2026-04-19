---
title: "Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete"
description: "Tool: cargo-machete. This skill gives an agent a narrow maintenance job: inspect a Rust project for dependencies that are declared but no longer used, then produce a cleanup candidate list for safe manifest pruning. When to use it: invoke this before release, dependency refreshes, or cleanup passes when a Rust repository may have accumulated stale crates over time. Using this skill is different from using the product normally because the workflow is targeted: scan for unused dependencies, verify the findings, and hand back a minimal cleanup patch instead of generic package-management advice. Scope boundary: this is not a generic Cargo listing and not a broad dependency-management platform card. Its boundary is specific: detect unused Rust dependencies so the repository can be slimmed down with cargo-machete."
source: "https://github.com/bnjbvr/cargo-machete"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete/)
