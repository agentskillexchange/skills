---
title: "Atlassian Rovo MCP Server"
description: "The Atlassian Rovo MCP Server bridges your Atlassian Cloud workspace with any MCP-compatible client. Search and summarize Jira issues, create tickets from natural language, update Confluence pages, and query Compass services."
verification: security_reviewed
source: "https://github.com/atlassian/atlassian-mcp-server"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "atlassian/atlassian-mcp-server"
  github_stars: 569
---

# Atlassian Rovo MCP Server

The Atlassian Rovo MCP Server is maintained by Atlassian and provides a cloud-based bridge between your Atlassian Cloud site and MCP-compatible tools including Claude Code, Cursor, VS Code, GitHub Copilot CLI, Gemini CLI, and more.

Best for

Creating Jira tickets from specs or meeting notes without context switching
Searching and summarizing Confluence documentation through your agent
Querying Compass service metadata
Automating cross-product workflows spanning Jira and Confluence

Key capabilities

Jira: Search issues, create and update tickets, view project status, manage workflows
Confluence: Search pages, create and edit content, summarize documentation
Compass: Query service information and component metadata

Security model
All traffic encrypted via HTTPS (TLS 1.2+). OAuth 2.1 or API token authentication. Data access respects existing Jira, Confluence, and Compass user permissions.

Install notes
Remote endpoint: https://mcp.atlassian.com/v1/mcp — complete OAuth 2.1 in your browser. Local proxy: npx -y mcp-remote https://mcp.atlassian.com/v1/sse. Requires an Atlassian Cloud site.

Source: github.com/atlassian/atlassian-mcp-server

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/atlassian-rovo-mcp-server/)
