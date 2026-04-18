---
title: "Draft release notes continuously with Release Drafter"
description: "Keep a living release draft in GitHub so merged pull requests are organized into release notes before ship day."
verification: security_reviewed
source: "https://github.com/release-drafter/release-drafter"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "release-drafter/release-drafter"
  github_stars: 3869
---

# Draft release notes continuously with Release Drafter

Use this skill when an agent needs to keep release notes current throughout a development cycle instead of assembling them manually at the end. It fits repos that already use GitHub pull requests and labels to organize changes.

Invoke it instead of using Release Drafter as a raw product when the operator task is to configure the workflow, shape categories, update templates, and verify that merged pull requests flow into a usable release draft.

This is skill-shaped because the boundary is tight: continuously draft release notes from merged PR metadata. It is not a generic GitHub Actions or release management listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/draft-release-notes-continuously-with-release-drafter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/draft-release-notes-continuously-with-release-drafter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/draft-release-notes-continuously-with-release-drafter/)
