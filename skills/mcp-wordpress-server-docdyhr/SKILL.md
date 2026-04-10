---
title: "MCP WordPress Server by docdyhr"
description: "An ASE skill built around docdyhr/mcp-wordpress, a WordPress MCP server that exposes site management tools through the Model Context Protocol. It is useful when an agent needs natural-language control over posts, pages, taxonomies, media, users, plugins, and multisite WordPress operations via a real MCP server."
slug: "mcp-wordpress-server-docdyhr"
category:
  - "WordPress &amp; CMS"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/docdyhr/mcp-wordpress"
listed: true
---

# MCP WordPress Server by docdyhr

An ASE skill built around docdyhr/mcp-wordpress, a WordPress MCP server that exposes site management tools through the Model Context Protocol. It is useful when an agent needs natural-language control over posts, pages, taxonomies, media, users, plugins, and multisite WordPress operations via a real MCP server.

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
clawhub install mcp-wordpress-server-docdyhr
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

MCP WordPress Server by docdyhr is a source-backed ASE skill for WordPress management through the Model Context Protocol. The upstream project is docdyhr/mcp-wordpress, an actively maintained TypeScript MCP server with an npm package, tagged releases, and a detailed README. Its purpose is straightforward: expose WordPress content and administrative actions as MCP tools so an MCP-compatible client can manage a site through structured tool calls instead of manual wp-admin navigation.
The job-to-be-done is agent-driven WordPress operations. An agent can list and update posts, pages, and custom post types, manage taxonomies and terms, work with media, inspect or edit users and comments, and coordinate tasks across multiple WordPress sites from a single MCP server. The README also highlights installation options including a downloadable desktop extension and a global npm install, which makes it practical for both local desktop workflows and scripted MCP setups.
Integration points include Claude Desktop or any MCP-compatible client, WordPress REST API access, WordPress application passwords, npm-based installation, and multisite content automation. Because the project has a real GitHub repository, npm distribution, releases, visible maintenance, and a concrete operational scope, it comfortably clears ASE intake. For the marketplace, this gives users a real WordPress MCP option that is distinct from the existing Automattic remote connector and WordPress core adapter entries.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mcp-wordpress-server-docdyhr/)
