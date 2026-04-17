---
title: "Automattic WordPress Remote MCP"
description: "Automattic WordPress Remote MCP is a WordPress-focused MCP server maintained by Automattic. Its job is to let an MCP-compatible client connect to a remote WordPress site and work with site content through supported authentication methods including OAuth 2.1 with PKCE, JWT tokens, and legacy WordPress application passwords. That makes it especially useful for editorial workflows, content operations, WooCommerce reporting, and site administration tasks where an agent needs controlled access to a live WordPress environment.\nThe project is published as the npm package @automattic/mcp-wordpress-remote and the README documents a standard npx -y @automattic/mcp-wordpress-remote launch path with WP_API_URL in the environment. The upstream repository also points users to the WordPress MCP adapter plugin for the site side of the connection. That integration model is important: the remote MCP server runs with the client, while the WordPress site exposes the capabilities the server can use.\nThis entry belongs in WordPress & CMS because its concrete job-to-be-done is connecting AI assistants to WordPress instances in a supported way. It also maps directly to the MCP framework because the server exposes tools and resources through the MCP protocol rather than through a custom agent-only format. The repository is active, licensed, and backed by a recognized WordPress company, which clears the verified metadata intake gate for a source-backed listing."
verification: security_reviewed
source: "https://github.com/Automattic/mcp-wordpress-remote"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "Automattic/mcp-wordpress-remote"
  github_stars: 131
  ase_npm_package: "@automattic/mcp-wordpress-remote"
  npm_weekly_downloads: 2468
---

# Automattic WordPress Remote MCP

Automattic WordPress Remote MCP is a WordPress-focused MCP server maintained by Automattic. Its job is to let an MCP-compatible client connect to a remote WordPress site and work with site content through supported authentication methods including OAuth 2.1 with PKCE, JWT tokens, and legacy WordPress application passwords. That makes it especially useful for editorial workflows, content operations, WooCommerce reporting, and site administration tasks where an agent needs controlled access to a live WordPress environment.
The project is published as the npm package @automattic/mcp-wordpress-remote and the README documents a standard npx -y @automattic/mcp-wordpress-remote launch path with WP_API_URL in the environment. The upstream repository also points users to the WordPress MCP adapter plugin for the site side of the connection. That integration model is important: the remote MCP server runs with the client, while the WordPress site exposes the capabilities the server can use.
This entry belongs in WordPress & CMS because its concrete job-to-be-done is connecting AI assistants to WordPress instances in a supported way. It also maps directly to the MCP framework because the server exposes tools and resources through the MCP protocol rather than through a custom agent-only format. The repository is active, licensed, and backed by a recognized WordPress company, which clears the verified metadata intake gate for a source-backed listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/automattic-wordpress-remote-mcp
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/automattic-wordpress-remote-mcp` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automattic-wordpress-remote-mcp/)
