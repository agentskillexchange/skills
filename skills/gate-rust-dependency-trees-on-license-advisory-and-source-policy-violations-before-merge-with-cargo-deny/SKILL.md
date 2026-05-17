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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install cargo-deny with the Rust toolchain using the method documented by the project, add a deny.toml policy file to the repository, then run cargo deny check locally or in CI and act on the reported policy violations before merging.
```

## Documentation

- https://github.com/EmbarkStudios/cargo-deny#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-rust-dependency-trees-on-license-advisory-and-source-policy-violations-before-merge-with-cargo-deny/)
