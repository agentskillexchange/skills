---
name: "MongoDB MCP Server for Database and Atlas Management"
description: "The official MongoDB MCP server connects AI agents to MongoDB databases and Atlas clusters through the Model Context Protocol, enabling structured queries, collection management, Atlas API operations, and aggregation pipelines with built-in authentication and access control."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/mongodb-js/mongodb-mcp-server"
---

# MongoDB MCP Server for Database and Atlas Management

The official MongoDB MCP server connects AI agents to MongoDB databases and Atlas clusters through the Model Context Protocol, enabling structured queries, collection management, Atlas API operations, and aggregation pipelines with built-in authentication and access control.

## Overview

The MongoDB MCP Server is an official Model Context Protocol server maintained by the MongoDB team that allows LLMs and AI agents to interact with MongoDB databases and MongoDB Atlas clusters. Published as an npm package (mongodb-mcp-server), it provides a structured interface for database operations that agents can invoke safely through MCP tool calls.

The server supports two main operational modes: direct MongoDB database operations and MongoDB Atlas cloud management. For database operations, agents can query collections, run aggregation pipelines, create indexes, inspect schemas, and manage documents. For Atlas operations, the server exposes cluster management, project listing, organization configuration, and private registry access through the Atlas API with service account authentication.

Security is a primary design consideration. The server defaults to read-only mode (–readOnly flag), ensuring agents cannot modify data unless explicitly permitted. It supports environment variable-based credential management rather than command-line arguments to prevent credential exposure in process lists. Atlas API access uses service accounts with configurable minimum-required permissions.

Integration is available for all major MCP clients including VS Code, Cursor, Windsurf, Claude Desktop, Claude Code, Codex, Copilot CLI, and Cline. The configuration follows standard MCP server patterns with npx-based invocation and environment variables for connection strings and Atlas API credentials.

The server provides MongoDB assistant tools that help agents understand collection schemas, suggest optimal query patterns, and build aggregation pipelines. It also supports proxy configurations for enterprise environments. With over 970 GitHub stars and active development from the official mongodb-js team, it represents the canonical way to give AI agents structured access to MongoDB data stores. The server requires Node.js 20.19+ and is licensed under Apache-2.0.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server-database-atlas-management
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server-database-atlas-management -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server-database-atlas-management -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mongodb-mcp-server-database-atlas-management -a codex
```

### OpenClaw

```bash
clawhub install mongodb-mcp-server-database-atlas-management
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mongodb-mcp-server-database-atlas-management/)
