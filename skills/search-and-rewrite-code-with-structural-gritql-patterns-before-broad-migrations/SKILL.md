---
title: "Search and rewrite code with structural GritQL patterns before broad migrations"
description: "Use GritQL when an agent needs reviewable structural search and rewrite passes across a large codebase before a migration, policy cleanup, or API change, instead of relying on regex or hand edits."
verification: "security_reviewed"
source: "https://github.com/biomejs/gritql"
author: "biomejs"
publisher_type: "community"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "biomejs/gritql"
  github_stars: 4482
---

# Search and rewrite code with structural GritQL patterns before broad migrations

Use GritQL when an agent needs reviewable structural search and rewrite passes across a large codebase before a migration, policy cleanup, or API change, instead of relying on regex or hand edits.

## Prerequisites

Grit CLI, a local repository to search or rewrite, and a review loop for inspecting the diffs produced by structural patterns.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the Grit CLI using the method documented by the project, write or reuse the GritQL patterns that describe the search or rewrite you want, run the apply or check workflow against the target repository, and review the resulting changes before merging.
```

## Documentation

- https://docs.grit.io/language/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations/)
