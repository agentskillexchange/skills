---
title: "Autofix common Nix anti-patterns before style drift spreads with Statix"
description: "Lint Nix expressions and automatically rewrite common anti-patterns before review or refactor work."
verification: "listed"
source: "https://github.com/oppiliappan/statix"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oppiliappan/statix"
  github_stars: 872
---

# Autofix common Nix anti-patterns before style drift spreads with Statix

Use Statix when an agent needs to clean up Nix expressions by finding and rewriting common anti-patterns before review or larger refactors. The agent can run a focused lint pass, apply safe autofixes, and return a smaller diff for human review. Invoke this instead of using the product normally when the job is Nix hygiene remediation, not general Nix package management or system orchestration. The boundary is anti-pattern detection and autofix in Nix code, not a generic Nix ecosystem listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/autofix-common-nix-anti-patterns-before-style-drift-spreads-with-statix/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/autofix-common-nix-anti-patterns-before-style-drift-spreads-with-statix
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/autofix-common-nix-anti-patterns-before-style-drift-spreads-with-statix`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/autofix-common-nix-anti-patterns-before-style-drift-spreads-with-statix/)
