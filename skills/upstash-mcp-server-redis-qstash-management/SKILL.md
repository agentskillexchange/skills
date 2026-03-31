---
name: "Upstash MCP Server for Redis and QStash Management"
description: "An official MCP server from Upstash that lets AI agents manage Redis databases, QStash message queues, and Vector stores through natural language. Supports database creation, key operations, backups, and throughput analytics via the Model Context Protocol."
category: "Integrations & Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/upstash/mcp-server"
---
# Upstash MCP Server for Redis and QStash Management

An official MCP server from Upstash that lets AI agents manage Redis databases, QStash message queues, and Vector stores through natural language. Supports database creation, key operations, backups, and throughput analytics via the Model Context Protocol.

## Overview

The Upstash MCP Server is an official Model Context Protocol integration that connects AI assistants to the Upstash serverless data platform. Available at github.com/upstash/mcp-server and published as the npm package @upstash/mcp-server, this server enables natural-language management of Upstash Redis databases, QStash message queues, and Vector stores.

Through MCP tool calls, AI agents can perform a wide range of operations: create new Redis databases in specific regions, list existing databases, browse and manipulate keys with pattern matching, create backups, and analyze throughput metrics over time. The server translates conversational commands like “Create a new Redis database in us-east-1” or “Show me the throughput spikes for the last 7 days” into Upstash Developer API calls.

Setup is minimal — the server can be launched with a single npx command (npx -y @upstash/mcp-server run EMAIL API_KEY) and integrates with Cursor, Claude Desktop, and other MCP clients through standard configuration. Authentication requires an Upstash account email and API key, which are passed as command-line arguments.

The server covers the three core Upstash services. For Redis, it handles database lifecycle management and key-value operations. For QStash, it manages message publishing, scheduling, and queue inspection. For Vector, it supports index creation and semantic search operations. This makes it a one-stop integration for teams using Upstash’s serverless data infrastructure, allowing AI agents to manage and query data stores without switching between dashboards or CLI tools. The npm package is actively maintained with regular releases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill upstash-mcp-server-redis-qstash-management
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill upstash-mcp-server-redis-qstash-management -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill upstash-mcp-server-redis-qstash-management -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill upstash-mcp-server-redis-qstash-management -a codex
```

### OpenClaw

```bash
clawhub install upstash-mcp-server-redis-qstash-management
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upstash-mcp-server-redis-qstash-management/)
