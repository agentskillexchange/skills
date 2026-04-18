---
title: "Sync dbt schema YAML and inherited column metadata before docs drift accumulates with dbt-osmosis"
description: "Keep dbt schema YAML and column documentation aligned with the project so stale metadata does not pile up between model changes."
verification: listed
source: "https://github.com/z3z1ma/dbt-osmosis"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "z3z1ma/dbt-osmosis"
  github_stars: 622
---

# Sync dbt schema YAML and inherited column metadata before docs drift accumulates with dbt-osmosis

Use dbt-osmosis when an agent needs to maintain schema YAML, inherited column documentation, and related dbt metadata across an existing dbt project instead of treating dbt as a general transformation framework. The operator workflow is specific: inspect models, organize or document schema YAML, and write the synchronized metadata back into the project. That scope boundary, metadata synchronization for dbt project upkeep, is narrow enough to be a publishable skill rather than a plain package card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis/)
