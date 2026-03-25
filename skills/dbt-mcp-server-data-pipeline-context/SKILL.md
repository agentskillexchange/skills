---
name: "dbt MCP Server for Data Pipeline Context"
description: "The official dbt MCP Server by dbt Labs provides Model Context Protocol tools for AI agents to interact with dbt projects, query the Semantic Layer, execute SQL, generate SQL from natural language, and explore data model lineage across dbt Core, Fusion, and Platform environments."
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-mcp-server-data-pipeline-context/"
tool_ecosystem:
  tool: "dbt"
  github_stars: 12460
  github_repo: "dbt-labs/dbt-core"
  maintained: true
---

# dbt MCP Server for Data Pipeline Context

The official dbt MCP Server by dbt Labs provides Model Context Protocol tools for AI agents to interact with dbt projects, query the Semantic Layer, execute SQL, generate SQL from natural language, and explore data model lineage across dbt Core, Fusion, and Platform environments.

## Overview

The dbt MCP Server is an official Model Context Protocol server built by dbt Labs that enables AI agents to interact with dbt projects, the dbt Semantic Layer, and dbt Platform infrastructure. It provides a standardized interface for AI assistants to discover data models, execute SQL queries, generate SQL from natural language, and explore data lineage within dbt-managed analytics environments.

The server exposes a rich set of tools organized into several categories. SQL tools include execute_sql for running queries on dbt Platform infrastructure with Semantic Layer support, and text_to_sql for generating SQL from natural language using project context. Semantic Layer tools provide access to metrics, dimensions, entities, saved queries, and compiled SQL. Discovery API tools allow agents to retrieve models, sources, macros, tests, and explore model lineage.

The dbt MCP Server supports three deployment modes: dbt Platform (connecting to dbt Cloud with full access to Semantic Layer and Discovery API), dbt Core (working with local dbt projects via the manifest and catalog files), and dbt Fusion (using the new Fusion runtime). Each mode exposes the appropriate subset of tools for that environment.

Integration is straightforward using standard MCP client configuration. The server runs via uvx (Python) and accepts configuration for API keys, project IDs, and environment settings. It follows the OpenSSF Best Practices badge requirements and publishes experimental MCP Bundle (mcpb) files with each release for clients that support bundle-based installation.

This server is particularly valuable for data teams using dbt who want to give AI assistants rich context about their data warehouse: model definitions, column descriptions, test results, freshness checks, and metric definitions. By exposing the dbt knowledge graph through MCP, agents can answer complex data questions, debug pipeline issues, and assist with SQL development while staying grounded in the actual project metadata. The project is maintained by dbt Labs with an Apache 2.0 license.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-mcp-server-data-pipeline-context
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-mcp-server-data-pipeline-context -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-mcp-server-data-pipeline-context -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-mcp-server-data-pipeline-context -a codex
```

### OpenClaw

```bash
clawhub install dbt-mcp-server-data-pipeline-context
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dbt-mcp-server-data-pipeline-context/
