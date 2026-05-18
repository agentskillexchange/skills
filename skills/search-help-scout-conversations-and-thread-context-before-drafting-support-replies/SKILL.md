---
name: "Search Help Scout conversations and thread context before drafting support replies"
slug: "search-help-scout-conversations-and-thread-context-before-drafting-support-replies"
description: "Lets an MCP-compatible agent search Help Scout inboxes, customers, organizations, and full thread history so support replies start with the right account and ticket context."
github_stars: 36
verification: "listed"
source: "https://github.com/drewburchfield/help-scout-mcp-server"
author: "drewburchfield"
publisher_type: "individual"
category: "Calendar, Email & Productivity"
framework: "MCP"
tool_ecosystem:
  github_repo: "drewburchfield/help-scout-mcp-server"
  github_stars: 36
  npm_package: "help-scout-mcp-server"
  npm_weekly_downloads: 184
---

# Search Help Scout conversations and thread context before drafting support replies

Lets an MCP-compatible agent search Help Scout inboxes, customers, organizations, and full thread history so support replies start with the right account and ticket context.

## Prerequisites

MCP-compatible client and Help Scout private app credentials with read access to Mailboxes, Conversations, Customers, and Organizations. Optional Docker or Claude Desktop/Claude Code plugin install.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -e HELPSCOUT_APP_ID="your-app-id" \
- git clone https://github.com/drewburchfield/help-scout-mcp-server.git
- npm install && npm run build
- npm start

Requirements and caveats from upstream:
- [![npm version](https://badge.fury.io/js/help-scout-mcp-server.svg)](https://badge.fury.io/js/help-scout-mcp-server) [![Docker](https://img.shields.io/docker/v/drewburchfield/help-scout-mcp-server?logo=docker&label=do...
- ### Docker

Basic usage or getting-started notes:
- ### Claude Cowork (Recommended)
- Open Cowork and go to **Customize** > **Browse plugins** > **Personal**
- Click **+** > **Add marketplace from GitHub** and enter drewburchfield/help-scout-mcp-server

- Source: https://github.com/drewburchfield/help-scout-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/drewburchfield/help-scout-mcp-server/HEAD/README.md

## Documentation

- https://github.com/drewburchfield/help-scout-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-help-scout-conversations-and-thread-context-before-drafting-support-replies/)
