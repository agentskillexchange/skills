---
title: "Prepare Rust Release PRs and Changelogs from Workspace Changes with release-plz"
description: "This skill wraps release-plz as a bounded Rust release-preparation workflow. The agent inspects workspace changes, determines release-worthy crates, drafts version bumps, prepares changelog updates, and opens the handoff point as a release PR before any publish step happens. Invoke it when a Rust workspace is approaching release and maintainers need a reproducible pre-publish pass. Use Cargo or hosting-platform release tools normally for simple manual releases. Use this skill when the job is specifically release PR preparation and changelog assembly from actual workspace deltas. The scope boundary is release preparation for Rust crates and workspaces. It is not a generic CI/CD platform, package registry, or universal release automation product card."
source: "https://github.com/release-plz/release-plz"
verification: "listed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "release-plz/release-plz"
  github_stars: 1345
---

# Prepare Rust Release PRs and Changelogs from Workspace Changes with release-plz

This skill wraps release-plz as a bounded Rust release-preparation workflow. The agent inspects workspace changes, determines release-worthy crates, drafts version bumps, prepares changelog updates, and opens the handoff point as a release PR before any publish step happens. Invoke it when a Rust workspace is approaching release and maintainers need a reproducible pre-publish pass. Use Cargo or hosting-platform release tools normally for simple manual releases. Use this skill when the job is specifically release PR preparation and changelog assembly from actual workspace deltas. The scope boundary is release preparation for Rust crates and workspaces. It is not a generic CI/CD platform, package registry, or universal release automation product card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-rust-release-prs-and-changelogs-from-workspace-changes-with-release-plz/)
