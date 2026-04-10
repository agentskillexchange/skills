---
title: "MongoDB MCP Server for Database and Atlas Management"
description: "The official MongoDB MCP server connects AI agents to MongoDB databases and Atlas clusters through the Model Context Protocol, enabling structured queries, collection management, Atlas API operations, and aggregation pipelines with built-in authentication and access control."
slug: "mongodb-mcp-server-database-atlas-management"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/mongodb-js/mongodb-mcp-server"
tool_ecosystem:
  github_repo: "mongodb-js/mongodb-mcp-server"
  github_stars: 983
  npm_package: "mongodb-mcp-server"
  npm_weekly_downloads: 33039
listed: true
---

# MongoDB MCP Server for Database and Atlas Management

The official MongoDB MCP server connects AI agents to MongoDB databases and Atlas clusters through the Model Context Protocol, enabling structured queries, collection management, Atlas API operations, and aggregation pipelines with built-in authentication and access control.

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
clawhub install mongodb-mcp-server-database-atlas-management
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The MongoDB MCP Server is an official Model Context Protocol server maintained by the MongoDB team that allows LLMs and AI agents to interact with MongoDB databases and MongoDB Atlas clusters. Published as an npm package (mongodb-mcp-server), it provides a structured interface for database operations that agents can invoke safely through MCP tool calls.
The server supports two main operational modes: direct MongoDB database operations and MongoDB Atlas cloud management. For database operations, agents can query collections, run aggregation pipelines, create indexes, inspect schemas, and manage documents. For Atlas operations, the server exposes cluster management, project listing, organization configuration, and private registry access through the Atlas API with service account authentication.
Security is a primary design consideration. The server defaults to read-only mode (–readOnly flag), ensuring agents cannot modify data unless explicitly permitted. It supports environment variable-based credential management rather than command-line arguments to prevent credential exposure in process lists. Atlas API access uses service accounts with configurable minimum-required permissions.
Integration is available for all major MCP clients including VS Code, Cursor, Windsurf, Claude Desktop, Claude Code, Codex, Copilot CLI, and Cline. The configuration follows standard MCP server patterns with npx-based invocation and environment variables for connection strings and Atlas API credentials.
The server provides MongoDB assistant tools that help agents understand collection schemas, suggest optimal query patterns, and build aggregation pipelines. It also supports proxy configurations for enterprise environments. With over 970 GitHub stars and active development from the official mongodb-js team, it represents the canonical way to give AI agents structured access to MongoDB data stores. The server requires Node.js 20.19+ and is licensed under Apache-2.0.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mongodb-mcp-server-database-atlas-management/)
