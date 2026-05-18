---
name: "Plan and preview warehouse SQL model changes before rollout with SQLMesh"
slug: "plan-and-preview-warehouse-sql-model-changes-before-rollout-with-sqlmesh"
description: "Compare SQL model changes, preview backfills and downstream impact, and stage safer warehouse rollouts before execution."
github_stars: 3034
verification: "listed"
source: "https://github.com/SQLMesh/sqlmesh"
author: "SQLMesh"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SQLMesh/sqlmesh"
  github_stars: 3034
---

# Plan and preview warehouse SQL model changes before rollout with SQLMesh

Compare SQL model changes, preview backfills and downstream impact, and stage safer warehouse rollouts before execution.

## Prerequisites

Python 3.9+, pip, SQLMesh, warehouse connection

## Installation

Use the upstream install or setup path that matches your environment:
- pip install 'sqlmesh[lsp]' # install the sqlmesh package with extensions to work with VSCode

Requirements and caveats from upstream:
- SQLMesh is a next-generation data transformation framework designed to ship data quickly, efficiently, and without error. Data teams can run and deploy data transformations written in SQL or Python with visibility and...
- python -m venv .venv
- Note: You may need to run python3 or pip3 instead of python or pip, depending on your python installation.

Basic usage or getting-started notes:
- # run the unit test
- 'new_column' AS new_column, /* non-breaking change example */
- Track what data’s been modified and run only the necessary transformations for [incremental models](https://tobikodata.com/correctly-loading-incremental-data-at-scale.html)

- Source: https://github.com/SQLMesh/sqlmesh
- Extracted from upstream docs: https://raw.githubusercontent.com/SQLMesh/sqlmesh/HEAD/README.md

## Documentation

- https://sqlmesh.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plan-and-preview-warehouse-sql-model-changes-before-rollout-with-sqlmesh/)
