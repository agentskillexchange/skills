---
name: "WordPress MCP Adapter Model Context Protocol Bridge"
slug: "wordpress-mcp-adapter-model-context-protocol-bridge"
description: "An agent skill built on the official WordPress MCP Adapter plugin, which bridges the WordPress Abilities API to the Model Context Protocol. Enables MCP-compatible AI clients to discover and invoke WordPress plugin, theme, and core abilities programmatically through a standardized transport layer."
github_stars: 792
verification: "listed"
source: "https://github.com/WordPress/mcp-adapter"
category: "WordPress & CMS"
framework: "MCP"
tool_ecosystem:
  github_repo: "WordPress/mcp-adapter"
  github_stars: 792
---

# WordPress MCP Adapter Model Context Protocol Bridge

An agent skill built on the official WordPress MCP Adapter plugin, which bridges the WordPress Abilities API to the Model Context Protocol. Enables MCP-compatible AI clients to discover and invoke WordPress plugin, theme, and core abilities programmatically through a standardized transport layer.

## Installation

Use the upstream install or setup path that matches your environment:
- composer require wordpress/mcp-adapter
- composer require automattic/jetpack-autoloader
- git clone https://github.com/WordPress/mcp-adapter.git wp-content/plugins/mcp-adapter
- composer install

Requirements and caveats from upstream:
- Since WordPress 6.9, the [Abilities API](https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/) is a core API and does not require a separate plugin.
- **Note:** On WordPress 6.8, you must also install the Abilities API separately: composer require wordpress/abilities-api wordpress/mcp-adapter. On WordPress 6.9+, the Abilities API is built into core and does not need...

Basic usage or getting-started notes:
- ### With Composer (Primary Installation Method)
- The MCP Adapter is designed to be installed as a Composer package. This is the primary and recommended installation method:
- bash

- Source: https://github.com/WordPress/mcp-adapter
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/mcp-adapter/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-mcp-adapter-model-context-protocol-bridge/)
