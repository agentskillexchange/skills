---
title: "Linear MCP Server for Issue Tracking and Project Management"
description: "The Linear MCP Server is a Model Context Protocol integration that connects Linear&#8217;s issue tracking and project management system to AI assistants. Originally built by jerhadf at github.com/jerhadf/linear-mcp-server , this server enables LLMs to interact with Linear issues, projects, teams, and workflows through natural language commands. Linear also provides an official remote MCP endpoint at mcp.linear.app for direct integration. The server exposes a comprehensive set of tools for issue management: creating new issues with title, description, priority, labels, and assignees; searching issues with flexible filtering by team, status, assignee, or free-text query; updating issue properties including status transitions through Linear&#8217;s workflow states; and adding comments to existing issues. Additional tools cover project listing, team management, and label operations. Authentication uses a Linear API key, which can be generated from Linear&#8217;s Settings > API section. The server runs as a standard MCP server via npx or direct Node.js execution, supporting stdio transport for local clients. Configuration follows the standard MCP client pattern — add the server entry to your Claude Desktop, Cursor, or other MCP client configuration file with the API key as an environment variable. This integration is particularly valuable for development teams that use Linear as their primary issue tracker. AI agents can triage incoming bugs by creating and categorizing issues, provide status updates by querying current sprint progress, link code changes to issues during PR reviews, and automate workflow transitions. With 287 stars and MIT license, the community server remains actively maintained, while Linear&#8217;s official remote MCP endpoint at mcp.linear.app provides an alternative for teams preferring vendor-hosted integrations."
source: "https://github.com/jerhadf/linear-mcp-server"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jerhadf/linear-mcp-server"
  github_stars: 346
---

# Linear MCP Server for Issue Tracking and Project Management

The Linear MCP Server is a Model Context Protocol integration that connects Linear&#8217;s issue tracking and project management system to AI assistants. Originally built by jerhadf at github.com/jerhadf/linear-mcp-server , this server enables LLMs to interact with Linear issues, projects, teams, and workflows through natural language commands. Linear also provides an official remote MCP endpoint at mcp.linear.app for direct integration. The server exposes a comprehensive set of tools for issue management: creating new issues with title, description, priority, labels, and assignees; searching issues with flexible filtering by team, status, assignee, or free-text query; updating issue properties including status transitions through Linear&#8217;s workflow states; and adding comments to existing issues. Additional tools cover project listing, team management, and label operations. Authentication uses a Linear API key, which can be generated from Linear&#8217;s Settings > API section. The server runs as a standard MCP server via npx or direct Node.js execution, supporting stdio transport for local clients. Configuration follows the standard MCP client pattern — add the server entry to your Claude Desktop, Cursor, or other MCP client configuration file with the API key as an environment variable. This integration is particularly valuable for development teams that use Linear as their primary issue tracker. AI agents can triage incoming bugs by creating and categorizing issues, provide status updates by querying current sprint progress, link code changes to issues during PR reviews, and automate workflow transitions. With 287 stars and MIT license, the community server remains actively maintained, while Linear&#8217;s official remote MCP endpoint at mcp.linear.app provides an alternative for teams preferring vendor-hosted integrations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linear-mcp-server-issue-tracking-project-management/)
