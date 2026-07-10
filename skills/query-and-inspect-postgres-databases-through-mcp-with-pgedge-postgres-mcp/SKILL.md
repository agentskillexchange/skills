---
name: "Query and inspect Postgres databases through MCP with pgEdge Postgres MCP"
slug: "query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp"
description: "Connect an MCP client to PostgreSQL databases for schema discovery, safe querying, and database inspection through a documented pgEdge MCP server and agent client workflow."
github_stars: 165
verification: "security_reviewed"
source: "https://github.com/pgEdge/pgedge-postgres-mcp"
author: "pgEdge"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "pgEdge/pgedge-postgres-mcp"
  github_stars: 165
---

# Query and inspect Postgres databases through MCP with pgEdge Postgres MCP

Connect an MCP client to PostgreSQL databases for schema discovery, safe querying, and database inspection through a documented pgEdge MCP server and agent client workflow.

## Prerequisites

PostgreSQL database, Python or Docker deployment environment, MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
- git clone https://github.com/pgEdge/pgedge-postgres-mcp.git
- make build
- make test

Requirements and caveats from upstream:
- [![CI - Docker](https://github.com/pgEdge/pgedge-postgres-mcp/actions/workflows/ci-docker.yml/badge.svg?branch=main)](https://github.com/pgEdge/pgedge-postgres-mcp/actions/workflows/ci-docker.yml?query=branch%3Amain)
- [Deploying on Docker](docs/guide/deploy_docker.md)
- [Python (Stdio + Claude)](docs/developers/stdio-anthropic-chatbot.md)

Basic usage or getting-started notes:
- [Quick Start](docs/guide/quickstart.md)
- The [Quick Start](docs/guide/quickstart.md) guide covers
- | Client | Transport | Best For |

- Source: https://github.com/pgEdge/pgedge-postgres-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/pgEdge/pgedge-postgres-mcp/HEAD/README.md

## Documentation

- https://docs.pgedge.com/pgedge-postgres-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp/)
