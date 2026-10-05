---
name: "Give agents persistent shared memory with mcp-memory-service"
slug: "give-agents-persistent-shared-memory-with-mcp-memory-service"
description: "Run a self-hosted MCP and REST memory layer so agents can store decisions, retrieve project context, and share knowledge across sessions and runtimes."
github_stars: 1983
verification: "security_reviewed"
source: "https://github.com/doobidoo/mcp-memory-service"
author: "doobidoo"
publisher_type: "individual"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "doobidoo/mcp-memory-service"
  github_stars: 1983
---

# Give agents persistent shared memory with mcp-memory-service

Run a self-hosted MCP and REST memory layer so agents can store decisions, retrieve project context, and share knowledge across sessions and runtimes.

## Prerequisites

Python, pip, MCP-compatible client or HTTP-capable agent framework

## Installation

Install or set up from the source-backed instructions:

Install with `pip install mcp-memory-service`, then run `memory server` for local MCP stdio use or `MCP_ALLOW_ANONYMOUS_ACCESS=true memory server --http` for HTTP/REST agent pipelines. Connect the documented MCP client or REST agent framework and use the memory store/search tools for durable project context.

- Source: https://github.com/doobidoo/mcp-memory-service

## Documentation

- https://github.com/doobidoo/mcp-memory-service

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-agents-persistent-shared-memory-with-mcp-memory-service/)
