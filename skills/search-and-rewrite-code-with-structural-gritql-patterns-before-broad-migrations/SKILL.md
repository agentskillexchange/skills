---
title: "Search and rewrite code with structural GritQL patterns before broad migrations"
description: "Use GritQL when an agent needs reviewable structural search and rewrite passes across a large codebase before a migration, policy cleanup, or API change, instead of relying on regex or hand edits."
verification: "security_reviewed"
source: "https://github.com/biomejs/gritql"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "biomejs/gritql"
  github_stars: 4482
---

# Search and rewrite code with structural GritQL patterns before broad migrations

Tool: GritQL. This skill is for agents that need a structural query-and-rewrite workflow: express the old and new code patterns declaratively, run them over a repository, and inspect the resulting diff before shipping a large migration.

When to use it: invoke this when the change is too broad for manual edits but too syntax-sensitive for grep or naive find-and-replace. It fits dependency migrations, API swaps, lint remediation, and repeated code cleanup where the operator wants a named pattern, reproducible application, and reviewable output.

Scope boundary: this is not a generic code-search language listing and not just another broad CLI card. Its boundary is the structural migration workflow itself: pattern definition, batch application, and reviewable rewrites across real source code. If the task does not require structural rewrites, a simpler tool is enough.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations/)
