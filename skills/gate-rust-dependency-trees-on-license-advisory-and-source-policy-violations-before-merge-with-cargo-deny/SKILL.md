---
title: "Gate Rust dependency trees on license, advisory, and source-policy violations before merge with cargo-deny"
description: "Use cargo-deny when an agent needs to enforce Rust dependency policy before merge by checking advisories, licenses, bans, and source rules in one repeatable gate instead of doing ad hoc manifest review."
verification: "security_reviewed"
source: "https://github.com/EmbarkStudios/cargo-deny"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "EmbarkStudios/cargo-deny"
  github_stars: 2263
  ase_npm_package: "cargo-deny"
  npm_weekly_downloads: 3315365
---

# Gate Rust dependency trees on license, advisory, and source-policy violations before merge with cargo-deny

Tool: cargo-deny. This skill gives an agent a narrow compliance job: inspect a Rust dependency graph and fail the workflow when license policy, security advisories, banned crates, or allowed-source rules are violated.

When to use it: invoke this before merge, release, or dependency approval when a repository needs an auditable Rust supply-chain gate that is stricter than manual review or a plain cargo build. Using this skill is different from using the product normally because the operator workflow is explicit: run the policy checks, interpret the failing rule set, and hand back a merge-blocking report with concrete remediation targets.

Scope boundary: this is not a generic Rust package manager listing and not a broad security platform card. Its boundary is tighter: enforce dependency-policy rules on a Rust project with cargo-deny as a pre-merge or pre-release gate.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-rust-dependency-trees-on-license-advisory-and-source-policy-violations-before-merge-with-cargo-deny/)
