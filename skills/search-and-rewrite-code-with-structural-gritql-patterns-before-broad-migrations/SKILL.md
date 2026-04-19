---
title: "Search and rewrite code with structural GritQL patterns before broad migrations"
description: "Tool: GritQL. This skill is for agents that need a structural query-and-rewrite workflow: express the old and new code patterns declaratively, run them over a repository, and inspect the resulting diff before shipping a large migration. When to use it: invoke this when the change is too broad for manual edits but too syntax-sensitive for grep or naive find-and-replace. It fits dependency migrations, API swaps, lint remediation, and repeated code cleanup where the operator wants a named pattern, reproducible application, and reviewable output. Scope boundary: this is not a generic code-search language listing and not just another broad CLI card. Its boundary is the structural migration workflow itself: pattern definition, batch application, and reviewable rewrites across real source code. If the task does not require structural rewrites, a simpler tool is enough."
source: "https://github.com/biomejs/gritql"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "biomejs/gritql"
  github_stars: 4482
---

# Search and rewrite code with structural GritQL patterns before broad migrations

Tool: GritQL. This skill is for agents that need a structural query-and-rewrite workflow: express the old and new code patterns declaratively, run them over a repository, and inspect the resulting diff before shipping a large migration. When to use it: invoke this when the change is too broad for manual edits but too syntax-sensitive for grep or naive find-and-replace. It fits dependency migrations, API swaps, lint remediation, and repeated code cleanup where the operator wants a named pattern, reproducible application, and reviewable output. Scope boundary: this is not a generic code-search language listing and not just another broad CLI card. Its boundary is the structural migration workflow itself: pattern definition, batch application, and reviewable rewrites across real source code. If the task does not require structural rewrites, a simpler tool is enough.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations/)
