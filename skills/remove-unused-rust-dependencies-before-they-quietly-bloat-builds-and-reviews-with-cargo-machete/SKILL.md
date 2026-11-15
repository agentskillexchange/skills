---
name: "Remove unused Rust dependencies before they quietly bloat builds and reviews with cargo-machete"
slug: "remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete"
description: "Use cargo-machete when an agent needs to find and remove unused Rust dependencies before they keep inflating build time, review noise, and manifest drift."
github_stars: 1280
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

Use the upstream install or setup path that matches your environment:
- cargo-machete is a Cargo tool that detects unused dependencies in Rust
- cargo install cargo-machete
- Run cargo-machete in a directory that contains one or more Rust projects (using Cargo for
- cargo machete /absolute/path/to/my/directory

Requirements and caveats from upstream:
- ## Docker Image
- A docker image for cargo machete.

Basic usage or getting-started notes:
- dependency management):
- bash
- cd my-directory && cargo machete

- Source: https://github.com/bnjbvr/cargo-machete
- Extracted from upstream docs: https://raw.githubusercontent.com/bnjbvr/cargo-machete/HEAD/README.md

## Documentation

- https://github.com/bnjbvr/cargo-machete#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/remove-unused-rust-dependencies-before-they-quietly-bloat-builds-and-reviews-with-cargo-machete/)
