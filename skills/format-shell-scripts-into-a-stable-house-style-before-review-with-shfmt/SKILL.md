---
title: "Format shell scripts into a stable house style before review with shfmt"
description: "Normalize Bash, POSIX shell, and Zsh scripts before review or CI so style noise stops hiding the real changes."
verification: "listed"
source: "https://github.com/mvdan/sh"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mvdan/sh"
  github_stars: 8700
---

# Format shell scripts into a stable house style before review with shfmt

Use shfmt when an agent needs one repeatable formatting pass for shell scripts before code review, lint cleanup, or automated refactors land. This should be invoked instead of editing shell style manually or treating a generic shell toolkit as the answer, because the job here is narrow: take existing shell source and rewrite it into a consistent canonical format. That scope boundary—shell formatting for reviewable diffs and team consistency—keeps this skill distinct from the broader mvdan/sh parser and interpreter project.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt/)
