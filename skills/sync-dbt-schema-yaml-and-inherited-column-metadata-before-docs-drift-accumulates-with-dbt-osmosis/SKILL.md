---
title: "Sync dbt schema YAML and inherited column metadata before docs drift accumulates with dbt-osmosis"
slug: "sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis"
description: "Keep dbt schema YAML and column documentation aligned with the project so stale metadata does not pile up between model changes."
github_stars: 622
verification: "security_reviewed"
source: "https://github.com/z3z1ma/dbt-osmosis"
author: "z3z1ma"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "z3z1ma/dbt-osmosis"
  github_stars: 622
---

# Sync dbt schema YAML and inherited column metadata before docs drift accumulates with dbt-osmosis

Keep dbt schema YAML and column documentation aligned with the project so stale metadata does not pile up between model changes.

## Prerequisites

Python, dbt Core with a compatible adapter, dbt-osmosis installation, and access to the target dbt project repository

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install dbt-osmosis with the documented Python tool or pip path together with a compatible dbt adapter, point it at the target dbt project, then run the YAML organize or document commands described in the upstream CLI reference.
```

## Documentation

- https://z3z1ma.github.io/dbt-osmosis/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis/)
