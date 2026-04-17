---
title: "Linear MCP Server for Issue Tracking and Project Management"
description: "The Linear MCP Server is a Model Context Protocol integration that connects Linear’s issue tracking and project management system to AI assistants. Originally built by jerhadf at github.com/jerhadf/linear-mcp-server, this server enables LLMs to interact with Linear issues, projects, teams, and workflows through natural language commands. Linear also provides an official remote MCP endpoint at mcp.linear.app for direct integration.\nThe server exposes a comprehensive set of tools for issue management: creating new issues with title, description, priority, labels, and assignees; searching issues with flexible filtering by team, status, assignee, or free-text query; updating issue properties including status transitions through Linear’s workflow states; and adding comments to existing issues. Additional tools cover project listing, team management, and label operations.\nAuthentication uses a Linear API key, which can be generated from Linear’s Settings > API section. The server runs as a standard MCP server via npx or direct Node.js execution, supporting stdio transport for local clients. Configuration follows the standard MCP client pattern — add the server entry to your Claude Desktop, Cursor, or other MCP client configuration file with the API key as an environment variable.\nThis integration is particularly valuable for development teams that use Linear as their primary issue tracker. AI agents can triage incoming bugs by creating and categorizing issues, provide status updates by querying current sprint progress, link code changes to issues during PR reviews, and automate workflow transitions. With 287 stars and MIT license, the community server remains actively maintained, while Linear’s official remote MCP endpoint at mcp.linear.app provides an alternative for teams preferring vendor-hosted integrations."
verification: security_reviewed
source: "https://github.com/jerhadf/linear-mcp-server"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jerhadf/linear-mcp-server"
  github_stars: 346
---

# Linear MCP Server for Issue Tracking and Project Management

The Linear MCP Server is a Model Context Protocol integration that connects Linear’s issue tracking and project management system to AI assistants. Originally built by jerhadf at github.com/jerhadf/linear-mcp-server, this server enables LLMs to interact with Linear issues, projects, teams, and workflows through natural language commands. Linear also provides an official remote MCP endpoint at mcp.linear.app for direct integration.
The server exposes a comprehensive set of tools for issue management: creating new issues with title, description, priority, labels, and assignees; searching issues with flexible filtering by team, status, assignee, or free-text query; updating issue properties including status transitions through Linear’s workflow states; and adding comments to existing issues. Additional tools cover project listing, team management, and label operations.
Authentication uses a Linear API key, which can be generated from Linear’s Settings > API section. The server runs as a standard MCP server via npx or direct Node.js execution, supporting stdio transport for local clients. Configuration follows the standard MCP client pattern — add the server entry to your Claude Desktop, Cursor, or other MCP client configuration file with the API key as an environment variable.
This integration is particularly valuable for development teams that use Linear as their primary issue tracker. AI agents can triage incoming bugs by creating and categorizing issues, provide status updates by querying current sprint progress, link code changes to issues during PR reviews, and automate workflow transitions. With 287 stars and MIT license, the community server remains actively maintained, while Linear’s official remote MCP endpoint at mcp.linear.app provides an alternative for teams preferring vendor-hosted integrations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/linear-mcp-server-issue-tracking-project-management
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/linear-mcp-server-issue-tracking-project-management` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linear-mcp-server-issue-tracking-project-management/)
