---
title: "Upstash MCP Server for Redis and QStash Management"
description: "The Upstash MCP Server is an official Model Context Protocol integration that connects AI assistants to the Upstash serverless data platform. Available at github.com/upstash/mcp-server and published as the npm package @upstash/mcp-server, this server enables natural-language management of Upstash Redis databases, QStash message queues, and Vector stores. Through MCP tool calls, AI agents can perform a wide range of operations: create new Redis databases in specific regions, list existing databases, browse and manipulate keys with pattern matching, create backups, and analyze throughput metrics over time. The server translates conversational commands like &#8220;Create a new Redis database in us-east-1&#8221; or &#8220;Show me the throughput spikes for the last 7 days&#8221; into Upstash Developer API calls. Setup is minimal — the server can be launched with a single npx command (npx -y @upstash/mcp-server run EMAIL API_KEY) and integrates with Cursor, Claude Desktop, and other MCP clients through standard configuration. Authentication requires an Upstash account email and API key, which are passed as command-line arguments. The server covers the three core Upstash services. For Redis, it handles database lifecycle management and key-value operations. For QStash, it manages message publishing, scheduling, and queue inspection. For Vector, it supports index creation and semantic search operations. This makes it a one-stop integration for teams using Upstash&#8217;s serverless data infrastructure, allowing AI agents to manage and query data stores without switching between dashboards or CLI tools. The npm package is actively maintained with regular releases."
source: "https://github.com/upstash/mcp-server"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "upstash/mcp-server"
  github_stars: 52
---

# Upstash MCP Server for Redis and QStash Management

The Upstash MCP Server is an official Model Context Protocol integration that connects AI assistants to the Upstash serverless data platform. Available at github.com/upstash/mcp-server and published as the npm package @upstash/mcp-server, this server enables natural-language management of Upstash Redis databases, QStash message queues, and Vector stores. Through MCP tool calls, AI agents can perform a wide range of operations: create new Redis databases in specific regions, list existing databases, browse and manipulate keys with pattern matching, create backups, and analyze throughput metrics over time. The server translates conversational commands like &#8220;Create a new Redis database in us-east-1&#8221; or &#8220;Show me the throughput spikes for the last 7 days&#8221; into Upstash Developer API calls. Setup is minimal — the server can be launched with a single npx command (npx -y @upstash/mcp-server run EMAIL API_KEY) and integrates with Cursor, Claude Desktop, and other MCP clients through standard configuration. Authentication requires an Upstash account email and API key, which are passed as command-line arguments. The server covers the three core Upstash services. For Redis, it handles database lifecycle management and key-value operations. For QStash, it manages message publishing, scheduling, and queue inspection. For Vector, it supports index creation and semantic search operations. This makes it a one-stop integration for teams using Upstash&#8217;s serverless data infrastructure, allowing AI agents to manage and query data stores without switching between dashboards or CLI tools. The npm package is actively maintained with regular releases.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upstash-mcp-server-redis-qstash-management/)
