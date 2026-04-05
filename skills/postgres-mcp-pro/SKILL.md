---
name: "Postgres MCP Pro"
description: "Query, analyze, and tune PostgreSQL databases through your AI agent with safe access controls. Beyond basic SQL execution, it provides index tuning recommendations, query plan analysis, database health monitoring, and schema intelligence."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgres-mcp-pro/"
---
# Postgres MCP Pro

Query, analyze, and tune PostgreSQL databases through your AI agent with safe access controls. Beyond basic SQL execution, it provides index tuning recommendations, query plan analysis, database health monitoring, and schema intelligence.

## Overview

Postgres MCP Pro is an open-source MCP server by Crystal DBA that goes beyond wrapping a database connection. It provides deep database intelligence including index tuning, EXPLAIN plan analysis, health diagnostics, and configurable access controls.

Best for

- Running queries with configurable read-only or full-access modes

- Diagnosing database performance problems with EXPLAIN plan analysis

- Getting industrial-strength index tuning recommendations

- Monitoring database health: connection utilization, buffer cache, vacuum health, replication lag

Access modes

Three modes: `read-only` (safe for production monitoring), `restricted` (allows writes with SQL parsing), and `unrestricted` (full access for development).

Install notes

Pull the Docker image: `docker pull crystaldba/postgres-mcp`. Or install via pip: `pipx install postgres-mcp`. Configure in your MCP client with your database URI and desired access mode. Supports both stdio and SSE transports.

Source: github.com/crystaldba/postgres-mcp

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro -a codex
```

### OpenClaw

```bash
clawhub install postgres-mcp-pro
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgres-mcp-pro/)
