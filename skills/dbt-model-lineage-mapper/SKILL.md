---
title: "dbt Model Lineage Mapper"
description: "The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json, catalog.json, run_results.json) to construct comprehensive data lineage graphs from source to exposure. It leverages the dbt artifact schema to map dependencies across models, sources, seeds, snapshots, and exposures. The skill builds a complete DAG showing upstream and downstream dependencies for any node, calculates critical path analysis for pipeline optimization, and identifies orphaned models with no downstream consumers. It cross-references catalog.json to enrich lineage with actual column-level lineage where available, tracing how specific columns flow through transformations. Impact analysis features let you specify proposed model changes and see all affected downstream models, tests, and exposures. It calculates blast radius metrics and can generate PR descriptions summarizing lineage impact. The skill also validates ref() and source() function usage, detects circular dependencies, and checks model naming convention compliance. Visualization outputs include Mermaid DAG diagrams, D3-compatible JSON for interactive exploration, and formatted Markdown reports. It can compare lineage between two manifest versions to show how the DAG evolved across releases."
source: "https://github.com/dbt-labs/dbt-core"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Lineage Mapper

The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json, catalog.json, run_results.json) to construct comprehensive data lineage graphs from source to exposure. It leverages the dbt artifact schema to map dependencies across models, sources, seeds, snapshots, and exposures. The skill builds a complete DAG showing upstream and downstream dependencies for any node, calculates critical path analysis for pipeline optimization, and identifies orphaned models with no downstream consumers. It cross-references catalog.json to enrich lineage with actual column-level lineage where available, tracing how specific columns flow through transformations. Impact analysis features let you specify proposed model changes and see all affected downstream models, tests, and exposures. It calculates blast radius metrics and can generate PR descriptions summarizing lineage impact. The skill also validates ref() and source() function usage, detects circular dependencies, and checks model naming convention compliance. Visualization outputs include Mermaid DAG diagrams, D3-compatible JSON for interactive exploration, and formatted Markdown reports. It can compare lineage between two manifest versions to show how the DAG evolved across releases.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-mapper/)
