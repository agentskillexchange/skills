---
title: WordPress MCP Adapter Model Context Protocol Bridge
description: 'The WordPress MCP Adapter is the official plugin maintained under the
  WordPress GitHub organization that bridges the WordPress Abilities API to the Model
  Context Protocol (MCP). It enables any MCP-compatible AI client — including Claude,
  Cursor, and other coding agents — to discover and invoke WordPress abilities programmatically.
  How It Works The adapter registers two transport endpoints on the WordPress REST
  API: a stdio transport at /wp/v2/wpmcp and a streamable HTTP transport at /wp/v2/wpmcp/streamable
  . When an MCP client connects, the adapter translates MCP tool discovery requests
  into WordPress Abilities API queries, and MCP tool invocation requests into Abilities
  API execution calls. This means any WordPress plugin that registers abilities becomes
  automatically accessible to AI agents. Authentication The adapter uses JWT-based
  authentication. Site administrators generate tokens through the React-based admin
  interface at WP Admin > MCP Adapter. Tokens are scoped to specific abilities and
  can be revoked at any time. The admin panel provides token management, connection
  status monitoring, and usage analytics. Supported MCP Methods The adapter implements
  the full MCP specification including tools/list for ability discovery, tools/call
  for ability execution, resources/list and resources/read for content access, and
  prompts/list and prompts/get for retrieving prompt templates. System initialization
  and capability negotiation follow the MCP handshake protocol. Integration with the
  Abilities API WordPress plugins register abilities using wp_register_ability() with
  defined parameters, permissions, and execution handlers. The MCP Adapter automatically
  exposes these as MCP tools with JSON Schema parameter definitions. Categories registered
  via wp_register_ability_category() are mapped to MCP resource namespaces for organized
  discovery. Setup and Configuration Install the plugin from the WordPress plugin
  directory or clone from github.com/WordPress/mcp-adapter . Activate it, navigate
  to WP Admin > MCP Adapter, generate an authentication token, and configure your
  MCP client with the site URL and token. The plugin requires WordPress 6.5+ and PHP
  8.0+. Licensed under GPL-2.0.'
verification: security_reviewed
source: https://github.com/WordPress/mcp-adapter
category:
- WordPress &amp; CMS
framework:
- MCP
tool_ecosystem:
  github_repo: WordPress/mcp-adapter
  github_stars: 792
---

# WordPress MCP Adapter Model Context Protocol Bridge

The WordPress MCP Adapter is the official plugin maintained under the WordPress GitHub organization that bridges the WordPress Abilities API to the Model Context Protocol (MCP). It enables any MCP-compatible AI client — including Claude, Cursor, and other coding agents — to discover and invoke WordPress abilities programmatically. How It Works The adapter registers two transport endpoints on the WordPress REST API: a stdio transport at /wp/v2/wpmcp and a streamable HTTP transport at /wp/v2/wpmcp/streamable . When an MCP client connects, the adapter translates MCP tool discovery requests into WordPress Abilities API queries, and MCP tool invocation requests into Abilities API execution calls. This means any WordPress plugin that registers abilities becomes automatically accessible to AI agents. Authentication The adapter uses JWT-based authentication. Site administrators generate tokens through the React-based admin interface at WP Admin > MCP Adapter. Tokens are scoped to specific abilities and can be revoked at any time. The admin panel provides token management, connection status monitoring, and usage analytics. Supported MCP Methods The adapter implements the full MCP specification including tools/list for ability discovery, tools/call for ability execution, resources/list and resources/read for content access, and prompts/list and prompts/get for retrieving prompt templates. System initialization and capability negotiation follow the MCP handshake protocol. Integration with the Abilities API WordPress plugins register abilities using wp_register_ability() with defined parameters, permissions, and execution handlers. The MCP Adapter automatically exposes these as MCP tools with JSON Schema parameter definitions. Categories registered via wp_register_ability_category() are mapped to MCP resource namespaces for organized discovery. Setup and Configuration Install the plugin from the WordPress plugin directory or clone from github.com/WordPress/mcp-adapter . Activate it, navigate to WP Admin > MCP Adapter, generate an authentication token, and configure your MCP client with the site URL and token. The plugin requires WordPress 6.5+ and PHP 8.0+. Licensed under GPL-2.0.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-mcp-adapter-model-context-protocol-bridge/)
