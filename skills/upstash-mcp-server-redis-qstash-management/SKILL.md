---
title: "Upstash MCP Server for Redis and QStash Management"
description: "An official MCP server from Upstash that lets AI agents manage Redis databases, QStash message queues, and Vector stores through natural language. Supports database creation, key operations, backups, and throughput analytics via the Model Context Protocol."
slug: "upstash-mcp-server-redis-qstash-management"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/upstash/mcp-server"
tool_ecosystem:
  github_repo: "upstash/mcp-server"
  github_stars: 52
---

# Upstash MCP Server for Redis and QStash Management

An official MCP server from Upstash that lets AI agents manage Redis databases, QStash message queues, and Vector stores through natural language. Supports database creation, key operations, backups, and throughput analytics via the Model Context Protocol.

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
clawhub install upstash-mcp-server-redis-qstash-management
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Upstash MCP Server is an official Model Context Protocol integration that connects AI assistants to the Upstash serverless data platform. Available at github.com/upstash/mcp-server and published as the npm package @upstash/mcp-server, this server enables natural-language management of Upstash Redis databases, QStash message queues, and Vector stores.
Through MCP tool calls, AI agents can perform a wide range of operations: create new Redis databases in specific regions, list existing databases, browse and manipulate keys with pattern matching, create backups, and analyze throughput metrics over time. The server translates conversational commands like “Create a new Redis database in us-east-1” or “Show me the throughput spikes for the last 7 days” into Upstash Developer API calls.
Setup is minimal — the server can be launched with a single npx command (npx -y @upstash/mcp-server run EMAIL API_KEY) and integrates with Cursor, Claude Desktop, and other MCP clients through standard configuration. Authentication requires an Upstash account email and API key, which are passed as command-line arguments.
The server covers the three core Upstash services. For Redis, it handles database lifecycle management and key-value operations. For QStash, it manages message publishing, scheduling, and queue inspection. For Vector, it supports index creation and semantic search operations. This makes it a one-stop integration for teams using Upstash’s serverless data infrastructure, allowing AI agents to manage and query data stores without switching between dashboards or CLI tools. The npm package is actively maintained with regular releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upstash-mcp-server-redis-qstash-management/)
