---
title: "Supergateway MCP Transport Bridge"
description: "Supergateway enables running MCP stdio-based servers over SSE, WebSockets, or Streamable HTTP with a single command. Essential infrastructure for remote MCP server access, debugging, and connecting clients across network boundaries with Docker and OAuth support."
verification: "security_reviewed"
source: "https://github.com/supercorp-ai/supergateway"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "supercorp-ai/supergateway"
  github_stars: 2538
  ase_npm_package: "supergateway"
  npm_weekly_downloads: 88592
---

# Supergateway MCP Transport Bridge

What is Supergateway?
Supergateway is an open-source MCP transport bridge with over 2,500 GitHub stars that converts between MCP transport protocols with a single npx command. It solves the fundamental problem of MCP server deployment: most MCP servers communicate via stdio (standard input/output), but production deployments need network-accessible transports like SSE (Server-Sent Events), WebSockets, or Streamable HTTP.


How the Skill Works
A Supergateway skill enables AI agents to deploy and manage MCP servers as network services. The core functionality wraps any stdio-based MCP server and exposes it over SSE, WebSockets, or Streamable HTTP on a configurable port. The reverse mode connects to remote SSE or Streamable HTTP endpoints and exposes them locally via stdio, enabling tools like Claude Desktop to connect to remote MCP servers.


The bridge supports custom headers for authentication, OAuth2 Bearer token injection, CORS configuration with origin allowlists, health check endpoints for load balancer integration, and configurable logging levels. Stateful mode maintains session persistence with configurable timeouts for Streamable HTTP connections, enabling complex multi-turn interactions with MCP servers.


Integration Points
Supergateway works with any MCP server that uses stdio transport, including the official Model Context Protocol reference servers, community servers, and custom implementations. It integrates with Docker through official container images (supercorp/supergateway:deno), supports deployment behind reverse proxies and load balancers via health endpoints, and connects to Claude Desktop, Cursor, and other MCP clients. The npm package is available via npx -y supergateway.


What It Outputs
The skill produces a network-accessible MCP server endpoint (SSE, WebSocket, or Streamable HTTP) from any stdio-based MCP server. It outputs connection URLs, transport protocol details, session status for stateful connections, and structured logs at configurable verbosity levels.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/supergateway-mcp-transport-bridge/)
