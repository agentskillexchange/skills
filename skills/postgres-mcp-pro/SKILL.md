---
title: "Postgres MCP Pro"
description: "Query, analyze, and tune PostgreSQL databases through your AI agent with safe access controls. Beyond basic SQL execution, it provides index tuning recommendations, query plan analysis, database health monitoring, and schema intelligence."
verification: "security_reviewed"
source: "https://github.com/crystaldba/postgres-mcp"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "crystaldba/postgres-mcp"
  github_stars: 2670
---

# Postgres MCP Pro

Postgres MCP Pro is an open-source MCP server by Crystal DBA that goes beyond wrapping a database connection. It provides deep database intelligence including index tuning, EXPLAIN plan analysis, health diagnostics, and configurable access controls.

Best for

- Running queries with configurable read-only or full-access modes

- Diagnosing database performance problems with EXPLAIN plan analysis

- Getting industrial-strength index tuning recommendations

- Monitoring database health: connection utilization, buffer cache, vacuum health, replication lag

Access modes
Three modes: read-only (safe for production monitoring), restricted (allows writes with SQL parsing), and unrestricted (full access for development).

Install notes
Pull the Docker image: docker pull crystaldba/postgres-mcp. Or install via pip: pipx install postgres-mcp. Configure in your MCP client with your database URI and desired access mode. Supports both stdio and SSE transports.

Source: github.com/crystaldba/postgres-mcp

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgres-mcp-pro/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgres-mcp-pro
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgres-mcp-pro`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgres-mcp-pro/)
