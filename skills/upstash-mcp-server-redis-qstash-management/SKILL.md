---
title: "Upstash MCP Server for Redis and QStash Management"
description: "The Upstash MCP Server is an official Model Context Protocol integration that connects AI assistants to the Upstash serverless data platform. Available at github.com/upstash/mcp-server and published as the npm package @upstash/mcp-server, this server enables natural-language management of Upstash Redis databases, QStash message queues, and Vector stores.\nThrough MCP tool calls, AI agents can perform a wide range of operations: create new Redis databases in specific regions, list existing databases, browse and manipulate keys with pattern matching, create backups, and analyze throughput metrics over time. The server translates conversational commands like “Create a new Redis database in us-east-1” or “Show me the throughput spikes for the last 7 days” into Upstash Developer API calls.\nSetup is minimal — the server can be launched with a single npx command (npx -y @upstash/mcp-server run EMAIL API_KEY) and integrates with Cursor, Claude Desktop, and other MCP clients through standard configuration. Authentication requires an Upstash account email and API key, which are passed as command-line arguments.\nThe server covers the three core Upstash services. For Redis, it handles database lifecycle management and key-value operations. For QStash, it manages message publishing, scheduling, and queue inspection. For Vector, it supports index creation and semantic search operations. This makes it a one-stop integration for teams using Upstash’s serverless data infrastructure, allowing AI agents to manage and query data stores without switching between dashboards or CLI tools. The npm package is actively maintained with regular releases."
verification: security_reviewed
source: "https://github.com/upstash/mcp-server"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "upstash/mcp-server"
  github_stars: 52
---

# Upstash MCP Server for Redis and QStash Management

The Upstash MCP Server is an official Model Context Protocol integration that connects AI assistants to the Upstash serverless data platform. Available at github.com/upstash/mcp-server and published as the npm package @upstash/mcp-server, this server enables natural-language management of Upstash Redis databases, QStash message queues, and Vector stores.
Through MCP tool calls, AI agents can perform a wide range of operations: create new Redis databases in specific regions, list existing databases, browse and manipulate keys with pattern matching, create backups, and analyze throughput metrics over time. The server translates conversational commands like “Create a new Redis database in us-east-1” or “Show me the throughput spikes for the last 7 days” into Upstash Developer API calls.
Setup is minimal — the server can be launched with a single npx command (npx -y @upstash/mcp-server run EMAIL API_KEY) and integrates with Cursor, Claude Desktop, and other MCP clients through standard configuration. Authentication requires an Upstash account email and API key, which are passed as command-line arguments.
The server covers the three core Upstash services. For Redis, it handles database lifecycle management and key-value operations. For QStash, it manages message publishing, scheduling, and queue inspection. For Vector, it supports index creation and semantic search operations. This makes it a one-stop integration for teams using Upstash’s serverless data infrastructure, allowing AI agents to manage and query data stores without switching between dashboards or CLI tools. The npm package is actively maintained with regular releases.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/upstash-mcp-server-redis-qstash-management
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/upstash-mcp-server-redis-qstash-management` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upstash-mcp-server-redis-qstash-management/)
