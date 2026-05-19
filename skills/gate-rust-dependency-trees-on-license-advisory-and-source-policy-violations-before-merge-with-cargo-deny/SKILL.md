---
name: "Gate Rust dependency trees on license, advisory, and source-policy violations before merge with cargo-deny"
slug: "gate-rust-dependency-trees-on-license-advisory-and-source-policy-violations-before-merge-with-cargo-deny"
description: "Use cargo-deny when an agent needs to enforce Rust dependency policy before merge by checking advisories, licenses, bans, and source rules in one repeatable gate instead of doing ad hoc manifest review."
github_stars: 2263
verification: "security_reviewed"
source: "https://github.com/EmbarkStudios/cargo-deny"
author: "Embark Studios"
publisher_type: "company"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "EmbarkStudios/cargo-deny"
  github_stars: 2263
  npm_package: "cargo-deny"
  npm_weekly_downloads: 3315365
---

# Gate Rust dependency trees on license, advisory, and source-policy violations before merge with cargo-deny

Use cargo-deny when an agent needs to enforce Rust dependency policy before merge by checking advisories, licenses, bans, and source rules in one repeatable gate instead of doing ad hoc manifest review.

## Prerequisites

Rust toolchain, Cargo project, cargo-deny configuration file, and CI or local shell access.

## Installation

Use the upstream install or setup path that matches your environment:
- cargo install --locked cargo-deny && cargo deny init && cargo deny check
- If you want to use cargo-deny without having cargo installed, build cargo-deny with the standalone feature. This can be useful in Docker Images.
- cargo install --locked cargo-deny
- cargo deny init

Basic usage or getting-started notes:
- To run on CI as a GitHub Action, see [cargo-deny-action](https://github.com/EmbarkStudios/cargo-deny-action).
- <a href="https://repology.org/project/cargo-deny/versions"><img align="right" src="https://repology.org/badge/vertical-allrepos/cargo-deny.svg" alt="Packaging status"></a>
- ### [Install](https://embarkstudios.github.io/cargo-deny/cli/index.html) cargo-deny

- Source: https://github.com/EmbarkStudios/cargo-deny
- Extracted from upstream docs: https://raw.githubusercontent.com/EmbarkStudios/cargo-deny/HEAD/README.md

## Documentation

- https://github.com/EmbarkStudios/cargo-deny#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-rust-dependency-trees-on-license-advisory-and-source-policy-violations-before-merge-with-cargo-deny/)
