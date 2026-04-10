---
title: "Cloudflare MCP Servers for Workers, Security, and Observability"
description: "Official Cloudflare MCP servers that enable AI assistants to manage Workers applications, debug logs, analyze Radar traffic data, configure security settings, and interact with the full Cloudflare platform through natural language via the Model Context Protocol."
slug: "cloudflare-mcp-servers-workers-security-observability"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/cloudflare/mcp-server-cloudflare"
tool_ecosystem:
  github_repo: "cloudflare/mcp-server-cloudflare"
  github_stars: 3579
---

# Cloudflare MCP Servers for Workers, Security, and Observability

Official Cloudflare MCP servers that enable AI assistants to manage Workers applications, debug logs, analyze Radar traffic data, configure security settings, and interact with the full Cloudflare platform through natural language via the Model Context Protocol.

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
clawhub install cloudflare-mcp-servers-workers-security-observability
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cloudflare MCP Servers are a collection of official Model Context Protocol integrations maintained by Cloudflare at github.com/cloudflare/mcp-server-cloudflare. Rather than a single monolithic server, Cloudflare provides specialized MCP servers for different service domains: Workers Bindings for application development, Observability for debugging, Radar for traffic intelligence, Documentation for reference lookups, and several more.
Each server exposes domain-specific tools through MCP. The Workers Bindings server lets AI agents build and deploy Workers applications with KV, R2, D1, Queues, and AI bindings. The Observability server enables querying application logs and analytics data. The Radar server provides global Internet traffic insights, trend analysis, and URL scanning capabilities. Additional servers cover Browser Rendering (page screenshots and markdown conversion), Logpush job management, AI Gateway log inspection, AutoRAG document search, audit log querying, and DNS analytics.
All servers support both streamable-http and SSE transports, and they use OAuth for authentication against your Cloudflare account. Remote MCP clients like the Cloudflare AI Playground can connect directly via server URLs (e.g., bindings.mcp.cloudflare.com/mcp). For clients that don’t support remote servers natively, the mcp-remote npm package provides a bridge.
With 3,600+ GitHub stars and active development from the Cloudflare team, this is one of the most comprehensive MCP server suites available. It demonstrates how a platform vendor can expose their entire service surface to AI agents while maintaining proper authentication and access controls. The modular architecture — separate servers per domain — is a design pattern worth studying for anyone building MCP integrations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudflare-mcp-servers-workers-security-observability/)
