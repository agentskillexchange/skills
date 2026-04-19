---
title: "MetaMCP Unified MCP Server Aggregator and Gateway"
description: "MetaMCP is an open-source Model Context Protocol (MCP) aggregator and gateway that solves the N×M integration problem of connecting multiple AI clients to multiple MCP servers. Maintained at github.com/metatool-ai/metamcp with 2,100+ GitHub stars, it acts as a single unified MCP server that proxies requests to any number of downstream MCP servers. The core problem MetaMCP addresses is MCP server management at scale. As teams adopt more MCP servers — for GitHub, databases, file systems, APIs, and other integrations — managing the connections, credentials, and tool availability becomes complex. MetaMCP provides a web-based GUI where you can add, configure, and organize MCP servers, then expose them as a single endpoint that any MCP client can connect to. MetaMCP introduces the concept of namespaces for organizing MCP servers into logical groups. You can create different namespaces for different projects or teams, each with its own set of available tools and servers. Endpoints can be assigned to namespaces and switched with one click. The middleware system allows applying cross-cutting concerns like observability, security policies, and tool overrides across all proxied servers. For production deployments, MetaMCP includes rate limiting per MCP server, OpenID Connect (OIDC) authentication with support for Google, GitHub, Microsoft, Okta, and other providers, registration controls, and API key authentication. It runs as a Docker Compose stack with PostgreSQL for persistence and supports both SSE and Streamable HTTP transport. A skill built on MetaMCP gives an AI agent a centralized control plane for all its MCP integrations. The agent could dynamically enable or disable tools based on context, route requests through appropriate middleware, and manage access across different tool namespaces. MetaMCP connects to any MCP client including Claude Desktop, Cursor, and custom clients via standard mcp.json configuration. The project is MIT-licensed with active development and comprehensive documentation at docs.metamcp.com."
source: "https://github.com/metatool-ai/metamcp"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "metatool-ai/metamcp"
  github_stars: 2175
---

# MetaMCP Unified MCP Server Aggregator and Gateway

MetaMCP is an open-source Model Context Protocol (MCP) aggregator and gateway that solves the N×M integration problem of connecting multiple AI clients to multiple MCP servers. Maintained at github.com/metatool-ai/metamcp with 2,100+ GitHub stars, it acts as a single unified MCP server that proxies requests to any number of downstream MCP servers. The core problem MetaMCP addresses is MCP server management at scale. As teams adopt more MCP servers — for GitHub, databases, file systems, APIs, and other integrations — managing the connections, credentials, and tool availability becomes complex. MetaMCP provides a web-based GUI where you can add, configure, and organize MCP servers, then expose them as a single endpoint that any MCP client can connect to. MetaMCP introduces the concept of namespaces for organizing MCP servers into logical groups. You can create different namespaces for different projects or teams, each with its own set of available tools and servers. Endpoints can be assigned to namespaces and switched with one click. The middleware system allows applying cross-cutting concerns like observability, security policies, and tool overrides across all proxied servers. For production deployments, MetaMCP includes rate limiting per MCP server, OpenID Connect (OIDC) authentication with support for Google, GitHub, Microsoft, Okta, and other providers, registration controls, and API key authentication. It runs as a Docker Compose stack with PostgreSQL for persistence and supports both SSE and Streamable HTTP transport. A skill built on MetaMCP gives an AI agent a centralized control plane for all its MCP integrations. The agent could dynamically enable or disable tools based on context, route requests through appropriate middleware, and manage access across different tool namespaces. MetaMCP connects to any MCP client including Claude Desktop, Cursor, and custom clients via standard mcp.json configuration. The project is MIT-licensed with active development and comprehensive documentation at docs.metamcp.com.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metamcp-unified-mcp-server-aggregator-gateway/)
