---
title: "Neon MCP Server for Serverless Postgres Management"
description: "The Neon MCP Server enables AI agents to manage serverless PostgreSQL databases through natural language via the Model Context Protocol. Create projects, run queries, manage branches, and perform database migrations conversationally."
verification: security_reviewed
source: "https://github.com/neondatabase/mcp-server-neon"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "neondatabase/mcp-server-neon"
  github_stars: 567
---

# Neon MCP Server for Serverless Postgres Management

The Neon MCP Server is an official Model Context Protocol server built by the Neon team that bridges natural language requests to the Neon serverless PostgreSQL API. It allows AI agents in Claude Code, Cursor, VS Code, and any MCP-compatible client to create databases, run SQL queries, manage branches, and perform schema migrations through conversational commands instead of direct API calls or SQL scripts.

This skill teaches agents how to interact with Neon’s serverless Postgres infrastructure using the MCP protocol. The server exposes tools for project management (create, list, delete projects), branch operations (create branches for testing migrations, compare schemas between branches, merge changes), SQL execution (run queries against any branch or database), and connection string management. Agents learn to leverage Neon’s unique branching model that creates instant, copy-on-write database copies for safe migration testing.

The MCP server supports two authentication modes: a remote hosted server at mcp.neon.tech with OAuth 2.0 authentication (zero local setup), and a local npm-based installation using a Neon API key. The remote server is the recommended approach as it receives updates automatically and eliminates key management. Agents can configure the server in their MCP client settings with a single URL and authenticate through the browser-based OAuth flow.

Practical use cases include spinning up isolated database branches for feature development, running migration scripts against a branch before merging to production, querying database contents to answer questions about application data, and provisioning new Postgres instances for prototyping. The server integrates with Neon’s scale-to-zero compute that suspends idle databases to save costs. The Neon MCP Server is MIT-licensed, actively maintained with 565+ GitHub stars, and is part of Neon’s broader agent-skills ecosystem for AI-native database management.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/neon-mcp-server-serverless-postgres/)
