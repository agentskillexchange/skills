---
name: "dbt MCP Server for Data Pipeline Context"
slug: "dbt-mcp-server-data-pipeline-context"
description: "The official dbt MCP Server by dbt Labs provides Model Context Protocol tools for AI agents to interact with dbt projects, query the Semantic Layer, execute SQL, generate SQL from natural language, and explore data model lineage across dbt Core, Fusion, and Platform environments."
github_stars: 526
verification: "security_reviewed"
source: "https://github.com/dbt-labs/dbt-mcp"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-mcp"
  github_stars: 526
---

# dbt MCP Server for Data Pipeline Context

The official dbt MCP Server by dbt Labs provides Model Context Protocol tools for AI agents to interact with dbt projects, query the Semantic Layer, execute SQL, generate SQL from natural language, and explore data model lineage across dbt Core, Fusion, and Platform environments.

## Installation

Requirements and caveats from upstream:
- get_node_details_dev: Retrieves node details from local manifest.json (models, seeds, snapshots, sources).
- get_column_lineage: Traces column-level lineage locally (requires dbt-lsp via dbt Labs VSCE).

Basic usage or getting-started notes:
- get_model_health: Gets health signals: run status, test results, and upstream source freshness.
- run: Executes models to materialize them in the database.
- get_job_run_details: Gets run details including status, timing, steps, and artifacts.

- Source: https://github.com/dbt-labs/dbt-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/dbt-labs/dbt-mcp/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-mcp-server-data-pipeline-context/)
