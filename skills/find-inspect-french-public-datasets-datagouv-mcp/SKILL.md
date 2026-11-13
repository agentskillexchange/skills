---
name: "Find and inspect French public datasets through data.gouv.fr MCP"
slug: "find-inspect-french-public-datasets-datagouv-mcp"
description: "Search data.gouv.fr, check dataset provenance and resource metadata, then preview supported tabular rows and return a cited research handoff."
github_stars: 1609
verification: "security_reviewed"
source: "https://github.com/datagouv/datagouv-mcp"
author: "datagouv"
publisher_type: "Community"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "datagouv/datagouv-mcp"
  github_stars: 1609
---

# Find and inspect French public datasets through data.gouv.fr MCP

Search data.gouv.fr, check dataset provenance and resource metadata, then preview supported tabular rows and return a cited research handoff.

## Prerequisites

MCP client supporting Streamable HTTP; network access to mcp.data.gouv.fr

## Installation

Install or set up from the source-backed instructions:

Configure a remote Streamable HTTP MCP connection to https://mcp.data.gouv.fr/mcp using your client configuration. The official README states no API key is required for its read-only tools. For Claude Code the documented example is: claude mcp add --transport http datagouv https://mcp.data.gouv.fr/mcp. Reconnect and inspect available tools before starting the dataset research pass.

- Source: https://github.com/datagouv/datagouv-mcp

## Documentation

- https://github.com/datagouv/datagouv-mcp/blob/01db2a6f3052c5248ad5a7d96030c65ee61f5edd/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-inspect-french-public-datasets-datagouv-mcp/)
