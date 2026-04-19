---
title: "Autofix common Nix anti-patterns before style drift spreads with Statix"
description: "Use Statix when an agent needs to clean up Nix expressions by finding and rewriting common anti-patterns before review or larger refactors. The agent can run a focused lint pass, apply safe autofixes, and return a smaller diff for human review. Invoke this instead of using the product normally when the job is Nix hygiene remediation, not general Nix package management or system orchestration. The boundary is anti-pattern detection and autofix in Nix code, not a generic Nix ecosystem listing."
source: "https://github.com/oppiliappan/statix"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oppiliappan/statix"
  github_stars: 872
---

# Autofix common Nix anti-patterns before style drift spreads with Statix

Use Statix when an agent needs to clean up Nix expressions by finding and rewriting common anti-patterns before review or larger refactors. The agent can run a focused lint pass, apply safe autofixes, and return a smaller diff for human review. Invoke this instead of using the product normally when the job is Nix hygiene remediation, not general Nix package management or system orchestration. The boundary is anti-pattern detection and autofix in Nix code, not a generic Nix ecosystem listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/autofix-common-nix-anti-patterns-before-style-drift-spreads-with-statix/)
