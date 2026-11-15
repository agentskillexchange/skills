---
name: "Inspect and debug MCP servers visually before connecting them to agents"
slug: "inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents"
description: "Use MCP Inspector when you need to launch an MCP server, inspect its tools and resources, exercise calls manually, and troubleshoot transport or schema issues before putting that server in front of real agents."
github_stars: 9431
verification: "security_reviewed"
source: "https://github.com/modelcontextprotocol/inspector"
author: "Model Context Protocol"
publisher_type: "organization"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "modelcontextprotocol/inspector"
  github_stars: 9431
  npm_package: "@modelcontextprotocol/inspector"
  npm_weekly_downloads: 635249
---

# Inspect and debug MCP servers visually before connecting them to agents

Use MCP Inspector when you need to launch an MCP server, inspect its tools and resources, exercise calls manually, and troubleshoot transport or schema issues before putting that server in front of real agents.

## Prerequisites

Node.js or Docker, MCP Inspector, and a target MCP server command or endpoint to inspect

## Installation

Use the upstream install or setup path that matches your environment:
- npx @modelcontextprotocol/inspector
- docker run --rm \
- To inspect an MCP server implementation, there's no need to clone this repo. Instead, use npx. For example, if your server is built at build/index.js:
- npx @modelcontextprotocol/inspector node build/index.js

Requirements and caveats from upstream:
- **MCP Proxy (MCPP)**: A Node.js server that acts as a protocol bridge, connecting the web UI to MCP servers via various transport methods (stdio, SSE, streamable-http)
- Node.js: ^22.7.5
- ### Docker Container

Basic usage or getting-started notes:
- To get up and running right away with the UI, just execute the following:
- bash
- The server will start up and the UI will be accessible at http://localhost:6274.

- Source: https://github.com/modelcontextprotocol/inspector
- Extracted from upstream docs: https://raw.githubusercontent.com/modelcontextprotocol/inspector/HEAD/README.md

## Documentation

- https://modelcontextprotocol.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents/)
