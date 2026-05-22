---
name: "MCP WordPress Server by docdyhr"
slug: "mcp-wordpress-server-docdyhr"
description: "An ASE skill built around docdyhr/mcp-wordpress, a WordPress MCP server that exposes site management tools through the Model Context Protocol. It is useful when an agent needs natural-language control over posts, pages, taxonomies, media, users, plugins, and multisite WordPress operations via a real MCP server."
github_stars: 81
verification: "security_reviewed"
source: "https://github.com/docdyhr/mcp-wordpress"
author: "docdyhr"
publisher_type: "Individual Developer"
category: "WordPress & CMS"
framework: "MCP"
tool_ecosystem:
  github_repo: "docdyhr/mcp-wordpress"
  github_stars: 81
  npm_package: "mcp-wordpress"
  npm_weekly_downloads: 358
---

# MCP WordPress Server by docdyhr

An ASE skill built around docdyhr/mcp-wordpress, a WordPress MCP server that exposes site management tools through the Model Context Protocol. It is useful when an agent needs natural-language control over posts, pages, taxonomies, media, users, plugins, and multisite WordPress operations via a real MCP server.

## Prerequisites

Node.js, npm, a WordPress site with REST API enabled, and a WordPress application password

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g mcp-wordpress
- npx -y mcp-wordpress
- npm run setup
- RUN npm ci --only=production

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/docdyhr/mcp-wordpress?logo=docker&logoColor=white)](https://hub.docker.com/r/docdyhr/mcp-wordpress)
- [![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker&logoColor=white)](https://hub.docker.com/r/docdyhr/mcp-wordpress)
- 🐳 **[Docker Setup](docs/user-guides/DOCKER_SETUP.md)** - Production deployment

Basic usage or getting-started notes:
- [Quick Start](#-quick-start) • [Why This MCP Server?](#-why-this-mcp-server)
- ## 🚀 Quick Start
- **WordPress**: Version 5.6+ with REST API enabled

- Source: https://github.com/docdyhr/mcp-wordpress
- Extracted from upstream docs: https://raw.githubusercontent.com/docdyhr/mcp-wordpress/HEAD/README.md

## Documentation

- https://github.com/docdyhr/mcp-wordpress

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mcp-wordpress-server-docdyhr/)
