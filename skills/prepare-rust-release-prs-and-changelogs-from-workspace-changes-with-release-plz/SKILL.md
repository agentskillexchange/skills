---
title: "Prepare Rust Release PRs and Changelogs from Workspace Changes with release-plz"
description: "Inspect Rust workspace changes, draft release PRs, bump versions, and assemble changelogs before publishing."
verification: "security_reviewed"
source: "https://github.com/release-plz/release-plz"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "release-plz/release-plz"
  github_stars: 1345
---

# Prepare Rust Release PRs and Changelogs from Workspace Changes with release-plz

This skill wraps release-plz as a bounded Rust release-preparation workflow. The agent inspects workspace changes, determines release-worthy crates, drafts version bumps, prepares changelog updates, and opens the handoff point as a release PR before any publish step happens.

Invoke it when a Rust workspace is approaching release and maintainers need a reproducible pre-publish pass. Use Cargo or hosting-platform release tools normally for simple manual releases. Use this skill when the job is specifically release PR preparation and changelog assembly from actual workspace deltas.

The scope boundary is release preparation for Rust crates and workspaces. It is not a generic CI/CD platform, package registry, or universal release automation product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/prepare-rust-release-prs-and-changelogs-from-workspace-changes-with-release-plz/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prepare-rust-release-prs-and-changelogs-from-workspace-changes-with-release-plz
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/prepare-rust-release-prs-and-changelogs-from-workspace-changes-with-release-plz`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-rust-release-prs-and-changelogs-from-workspace-changes-with-release-plz/)
