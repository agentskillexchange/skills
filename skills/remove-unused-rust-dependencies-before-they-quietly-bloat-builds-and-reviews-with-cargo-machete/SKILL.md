---
title: "Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete"
slug: "remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete"
description: "Use cargo-machete when an agent needs to find and remove unused Rust dependencies before they keep inflating build time, review noise, and manifest drift."
verification: "security_reviewed"
source: "https://github.com/bnjbvr/cargo-machete"
author: "bnjbvr"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bnjbvr/cargo-machete"
  github_stars: 1280
  npm_package: "cargo-machete"
  npm_weekly_downloads: 2073590
---

# Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete

Use cargo-machete when an agent needs to find and remove unused Rust dependencies before they keep inflating build time, review noise, and manifest drift.

## Prerequisites

Rust toolchain, Cargo project, and shell access for dependency scans and cleanup edits.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install cargo-machete with the Rust toolchain using the method documented by the project, run it against the target Cargo project, review the unused-dependency findings, and then remove confirmed dead entries from the manifest before re-running tests.
```

## Documentation

- https://github.com/bnjbvr/cargo-machete#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete/)
