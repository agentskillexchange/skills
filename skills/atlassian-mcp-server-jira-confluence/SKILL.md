---
name: "Atlassian MCP Server for Jira and Confluence"
description: "mcp-atlassian is a Model Context Protocol server that connects AI assistants to Atlassian Jira and Confluence. It enables searching and managing Jira issues, reading and editing Confluence pages, and performing project management tasks through natural language via any MCP-compatible client."
category: "Integrations & Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/sooperset/mcp-atlassian"
tool_ecosystem:
  tool: mcp-atlassian
  github_repo: sooperset/mcp-atlassian
  github_stars: 4785
---
# Atlassian MCP Server for Jira and Confluence

mcp-atlassian is a Model Context Protocol server that connects AI assistants to Atlassian Jira and Confluence. It enables searching and managing Jira issues, reading and editing Confluence pages, and performing project management tasks through natural language via any MCP-compatible client.

## Overview

mcp-atlassian is an open-source Model Context Protocol server that provides AI assistants with full access to Atlassian Jira and Confluence. With over 4,700 GitHub stars and active maintenance, it has become the most popular community MCP integration for Atlassian products, supporting both Cloud and Server/Data Center deployments.

The server exposes a comprehensive set of tools for Jira issue management. Agents can search issues using JQL queries, create new tickets, update issue status and fields, add comments, manage sprints and boards, and view development information like linked commits and pull requests. For Confluence, the server enables searching wiki content, reading page bodies, creating and updating pages, and managing page hierarchies. All operations respect existing project and space-level permissions from the authenticated user’s Atlassian account.

Authentication supports multiple methods: API tokens for Cloud instances, Personal Access Tokens for Server/Data Center, and OAuth 2.0 for production deployments. The server installs cleanly via `uvx mcp-atlassian` (Python) or Docker, and configuration requires only environment variables for the Atlassian URL and credentials. It works with Claude Desktop, Cursor, VS Code, and any other MCP-compatible client.

The project is published on PyPI as `mcp-atlassian`, has comprehensive documentation at mcp-atlassian.soomiles.com (including llms.txt format for AI consumption), and is licensed under MIT. It supports HTTP transport for remote deployments and includes CI-tested releases. For development teams that live in Jira and Confluence, this server eliminates context switching by letting AI assistants directly interact with project management and documentation workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill atlassian-mcp-server-jira-confluence
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill atlassian-mcp-server-jira-confluence -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill atlassian-mcp-server-jira-confluence -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill atlassian-mcp-server-jira-confluence -a codex
```

### OpenClaw

```bash
clawhub install atlassian-mcp-server-jira-confluence
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/atlassian-mcp-server-jira-confluence/)
