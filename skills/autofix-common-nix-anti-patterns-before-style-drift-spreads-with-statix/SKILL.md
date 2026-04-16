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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/autofix-common-nix-anti-patterns-before-style-drift-spreads-with-statix/)
