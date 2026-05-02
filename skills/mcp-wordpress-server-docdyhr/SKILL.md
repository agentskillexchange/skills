---
title: "MCP WordPress Server by docdyhr"
description: "An ASE skill built around docdyhr/mcp-wordpress, a WordPress MCP server that exposes site management tools through the Model Context Protocol. It is useful when an agent needs natural-language control over posts, pages, taxonomies, media, users, plugins, and multisite WordPress operations via a real MCP server."
verification: "security_reviewed"
source: "https://github.com/docdyhr/mcp-wordpress"
category:
  - "WordPress & CMS"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "docdyhr/mcp-wordpress"
  github_stars: 81
---

# MCP WordPress Server by docdyhr

MCP WordPress Server by docdyhr is a source-backed ASE skill for WordPress management through the Model Context Protocol. The upstream project is docdyhr/mcp-wordpress, an actively maintained TypeScript MCP server with an npm package, tagged releases, and a detailed README. Its purpose is straightforward: expose WordPress content and administrative actions as MCP tools so an MCP-compatible client can manage a site through structured tool calls instead of manual wp-admin navigation.

The job-to-be-done is agent-driven WordPress operations. An agent can list and update posts, pages, and custom post types, manage taxonomies and terms, work with media, inspect or edit users and comments, and coordinate tasks across multiple WordPress sites from a single MCP server. The README also highlights installation options including a downloadable desktop extension and a global npm install, which makes it practical for both local desktop workflows and scripted MCP setups.

Integration points include Claude Desktop or any MCP-compatible client, WordPress REST API access, WordPress application passwords, npm-based installation, and multisite content automation. Because the project has a real GitHub repository, npm distribution, releases, visible maintenance, and a concrete operational scope, it comfortably clears ASE intake. For the marketplace, this gives users a real WordPress MCP option that is distinct from the existing Automattic remote connector and WordPress core adapter entries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/mcp-wordpress-server-docdyhr/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mcp-wordpress-server-docdyhr
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/mcp-wordpress-server-docdyhr`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mcp-wordpress-server-docdyhr/)
