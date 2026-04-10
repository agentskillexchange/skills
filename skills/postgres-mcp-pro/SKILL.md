---
title: "Postgres MCP Pro"
description: "Query, analyze, and tune PostgreSQL databases through your AI agent with safe access controls. Beyond basic SQL execution, it provides index tuning recommendations, query plan analysis, database health monitoring, and schema intelligence."
slug: "postgres-mcp-pro"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/crystaldba/postgres-mcp"
tool_ecosystem:
  github_repo: "crystaldba/postgres-mcp"
  github_stars: 2499
---

# Postgres MCP Pro

Query, analyze, and tune PostgreSQL databases through your AI agent with safe access controls. Beyond basic SQL execution, it provides index tuning recommendations, query plan analysis, database health monitoring, and schema intelligence.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install postgres-mcp-pro
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

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

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgres-mcp-pro/)
