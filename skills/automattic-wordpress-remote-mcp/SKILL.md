---
title: "Automattic WordPress Remote MCP"
description: "Automattic WordPress Remote MCP connects MCP clients to live WordPress sites using OAuth, JWT, or application passwords. It is aimed at agents that need to read or operate against WordPress content and site features through a maintained remote MCP bridge."
verification: "security_reviewed"
source: "https://github.com/Automattic/mcp-wordpress-remote"
category:
  - "WordPress & CMS"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "Automattic/mcp-wordpress-remote"
  github_stars: 131
  npm_package: "@automattic/mcp-wordpress-remote"
  npm_weekly_downloads: 2468
---

# Automattic WordPress Remote MCP

Automattic WordPress Remote MCP is a WordPress-focused MCP server maintained by Automattic. Its job is to let an MCP-compatible client connect to a remote WordPress site and work with site content through supported authentication methods including OAuth 2.1 with PKCE, JWT tokens, and legacy WordPress application passwords. That makes it especially useful for editorial workflows, content operations, WooCommerce reporting, and site administration tasks where an agent needs controlled access to a live WordPress environment.

The project is published as the npm package @automattic/mcp-wordpress-remote and the README documents a standard npx -y @automattic/mcp-wordpress-remote launch path with WP_API_URL in the environment. The upstream repository also points users to the WordPress MCP adapter plugin for the site side of the connection. That integration model is important: the remote MCP server runs with the client, while the WordPress site exposes the capabilities the server can use.

This entry belongs in WordPress & CMS because its concrete job-to-be-done is connecting AI assistants to WordPress instances in a supported way. It also maps directly to the MCP framework because the server exposes tools and resources through the MCP protocol rather than through a custom agent-only format. The repository is active, licensed, and backed by a recognized WordPress company, which clears the verified metadata intake gate for a source-backed listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/automattic-wordpress-remote-mcp/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/automattic-wordpress-remote-mcp
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/automattic-wordpress-remote-mcp`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automattic-wordpress-remote-mcp/)
