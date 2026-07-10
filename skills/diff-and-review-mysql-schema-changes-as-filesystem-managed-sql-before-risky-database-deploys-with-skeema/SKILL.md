---
title: "Diff and review MySQL schema changes as filesystem-managed SQL before risky database deploys with Skeema"
description: "Pull live MySQL schema into files, inspect diffs, and push reviewed changes back with a repeatable workflow."
verification: "security_reviewed"
source: "https://github.com/skeema/skeema"
author: "skeema"
publisher_type: "organization"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "skeema/skeema"
  github_stars: 1361
---

# Diff and review MySQL schema changes as filesystem-managed SQL before risky database deploys with Skeema

Pull live MySQL schema into files, inspect diffs, and push reviewed changes back with a repeatable workflow.

## Prerequisites

Skeema CLI, network access to the target MySQL or MariaDB instances, credentials with schema review privileges, and a repository or filesystem location for schema files

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Skeema from the upstream binary or package instructions, configure credentials and the .skeema settings for the target databases, then use the documented pull, diff, lint, and push commands to manage reviewed schema changes.
```

## Documentation

- https://www.skeema.io/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-and-review-mysql-schema-changes-as-filesystem-managed-sql-before-risky-database-deploys-with-skeema/)
