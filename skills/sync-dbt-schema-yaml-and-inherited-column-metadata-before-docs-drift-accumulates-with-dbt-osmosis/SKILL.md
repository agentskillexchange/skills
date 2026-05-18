---
name: "Sync dbt schema YAML and inherited column metadata before docs drift accumulates with dbt-osmosis"
slug: "sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis"
description: "Keep dbt schema YAML and column documentation aligned with the project so stale metadata does not pile up between model changes."
github_stars: 622
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- uv tool install --with="dbt-<adapter>" dbt-osmosis
- pip install "dbt-osmosis" "dbt-<adapter>"
- npm --prefix docs run start
- npm --prefix docs run build

Requirements and caveats from upstream:
- dbt-osmosis is a Python CLI and package for dbt development workflows.
- Python 3.10-3.13
- Docs-site commands use the Node toolchain under docs/:

Basic usage or getting-started notes:
- ad-hoc SQL compile/run helpers
- With uv:
- bash

- Source: https://github.com/z3z1ma/dbt-osmosis
- Extracted from upstream docs: https://raw.githubusercontent.com/z3z1ma/dbt-osmosis/HEAD/README.md

## Documentation

- https://z3z1ma.github.io/dbt-osmosis/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sync-dbt-schema-yaml-and-inherited-column-metadata-before-docs-drift-accumulates-with-dbt-osmosis/)
