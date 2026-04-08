---
title: Postgres MCP Pro
description: 'Postgres MCP Pro is an open-source MCP server by Crystal DBA that goes
  beyond wrapping a database connection. It provides deep database intelligence including
  index tuning, EXPLAIN plan analysis, health diagnostics, and configurable access
  controls. Best for Running queries with configurable read-only or full-access modes
  Diagnosing database performance problems with EXPLAIN plan analysis Getting industrial-strength
  index tuning recommendations Monitoring database health: connection utilization,
  buffer cache, vacuum health, replication lag Access modes Three modes: read-only
  (safe for production monitoring), restricted (allows writes with SQL parsing), and
  unrestricted (full access for development). Install notes Pull the Docker image:
  docker pull crystaldba/postgres-mcp . Or install via pip: pipx install postgres-mcp
  . Configure in your MCP client with your database URI and desired access mode. Supports
  both stdio and SSE transports. Source: github.com/crystaldba/postgres-mcp'
verification: security_reviewed
source: https://github.com/crystaldba/postgres-mcp
category:
- Data Extraction &amp; Transformation
framework:
- MCP
tool_ecosystem:
  github_repo: crystaldba/postgres-mcp
  github_stars: 2464
---

# Postgres MCP Pro

Postgres MCP Pro is an open-source MCP server by Crystal DBA that goes beyond wrapping a database connection. It provides deep database intelligence including index tuning, EXPLAIN plan analysis, health diagnostics, and configurable access controls. Best for Running queries with configurable read-only or full-access modes Diagnosing database performance problems with EXPLAIN plan analysis Getting industrial-strength index tuning recommendations Monitoring database health: connection utilization, buffer cache, vacuum health, replication lag Access modes Three modes: read-only (safe for production monitoring), restricted (allows writes with SQL parsing), and unrestricted (full access for development). Install notes Pull the Docker image: docker pull crystaldba/postgres-mcp . Or install via pip: pipx install postgres-mcp . Configure in your MCP client with your database URI and desired access mode. Supports both stdio and SSE transports. Source: github.com/crystaldba/postgres-mcp

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgres-mcp-pro/)
