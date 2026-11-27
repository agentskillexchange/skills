---
name: "Retrieve permission-scoped workplace evidence through Onyx MCP"
slug: "retrieve-permission-scoped-workplace-evidence-through-onyx-mcp"
description: "Search an existing Onyx workspace within an explicit document-set or agent scope, then return source-linked evidence for a coding or operations task."
github_stars: 32798
verification: "security_reviewed"
source: "https://github.com/onyx-dot-app/onyx"
author: "Onyx (onyx-dot-app)"
publisher_type: "Organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "onyx-dot-app/onyx"
  github_stars: 32798
---

# Retrieve permission-scoped workplace evidence through Onyx MCP

Search an existing Onyx workspace within an explicit document-set or agent scope, then return source-linked evidence for a coding or operations task.

## Prerequisites

Existing indexed Onyx workspace; enabled HTTPS MCP endpoint; remote HTTP MCP client; scoped personal access token; approved secret storage

## Installation

Install or set up from the source-backed instructions:

Use an existing indexed Onyx deployment. Ask its administrator for the enabled HTTPS /mcp/ endpoint and provision a personal access token restricted to read:search. Register that URL in a remote HTTP MCP client and configure Authorization: Bearer via the client secret mechanism, following the official MCP guide. Do not put credentials in prompts or committed configuration. Verify that search_indexed_documents can retrieve a known accessible document before running the scoped evidence workflow. No standalone skill installer is asserted; this entry is an operator runbook.

- Source: https://github.com/onyx-dot-app/onyx

## Documentation

- https://docs.onyx.app/overview/onyx_anywhere/mcp_server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/retrieve-permission-scoped-workplace-evidence-through-onyx-mcp/)
