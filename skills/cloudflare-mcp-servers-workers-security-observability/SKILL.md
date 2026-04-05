---
name: "Cloudflare MCP Servers for Workers, Security, and Observability"
description: "Official Cloudflare MCP servers that enable AI assistants to manage Workers applications, debug logs, analyze Radar traffic data, configure security settings, and interact with the full Cloudflare platform through natural language via the Model Context Protocol."
category: "Integrations &amp; Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/cloudflare/mcp-server-cloudflare"
tool_ecosystem:
  github_repo: "cloudflare/mcp-server-cloudflare"
  github_stars: 3579
---
# Cloudflare MCP Servers for Workers, Security, and Observability

Official Cloudflare MCP servers that enable AI assistants to manage Workers applications, debug logs, analyze Radar traffic data, configure security settings, and interact with the full Cloudflare platform through natural language via the Model Context Protocol.

The Cloudflare MCP Servers are a collection of official Model Context Protocol integrations maintained by Cloudflare at github.com/cloudflare/mcp-server-cloudflare. Rather than a single monolithic server, Cloudflare provides specialized MCP servers for different service domains: Workers Bindings for application development, Observability for debugging, Radar for traffic intelligence, Documentation for reference lookups, and several more.

Each server exposes domain-specific tools through MCP. The Workers Bindings server lets AI agents build and deploy Workers applications with KV, R2, D1, Queues, and AI bindings. The Observability server enables querying application logs and analytics data. The Radar server provides global Internet traffic insights, trend analysis, and URL scanning capabilities. Additional servers cover Browser Rendering (page screenshots and markdown conversion), Logpush job management, AI Gateway log inspection, AutoRAG document search, audit log querying, and DNS analytics.

All servers support both streamable-http and SSE transports, and they use OAuth for authentication against your Cloudflare account. Remote MCP clients like the Cloudflare AI Playground can connect directly via server URLs (e.g., bindings.mcp.cloudflare.com/mcp). For clients that don’t support remote servers natively, the mcp-remote npm package provides a bridge.

With 3,600+ GitHub stars and active development from the Cloudflare team, this is one of the most comprehensive MCP server suites available. It demonstrates how a platform vendor can expose their entire service surface to AI agents while maintaining proper authentication and access controls. The modular architecture — separate servers per domain — is a design pattern worth studying for anyone building MCP integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudflare-mcp-servers-workers-security-observability
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudflare-mcp-servers-workers-security-observability -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudflare-mcp-servers-workers-security-observability -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudflare-mcp-servers-workers-security-observability -a codex
```

### OpenClaw

```bash
clawhub install cloudflare-mcp-servers-workers-security-observability
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudflare-mcp-servers-workers-security-observability/)
