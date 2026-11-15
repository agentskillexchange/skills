---
name: "Maintain a Git-versioned codebase index for coding agents with AOCI-CODE"
slug: "maintain-a-git-versioned-codebase-index-for-coding-agents-with-aoci-code"
description: "Initialize a local MCP server and repository-owned index so coding agents can read durable code and database context before making changes."
github_stars: 443
verification: "security_reviewed"
source: "https://github.com/aoci-spec/aoci-code"
author: "aoci-spec"
publisher_type: "organization"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "aoci-spec/aoci-code"
  github_stars: 443
---

# Maintain a Git-versioned codebase index for coding agents with AOCI-CODE

Initialize a local MCP server and repository-owned index so coding agents can read durable code and database context before making changes.

## Prerequisites

AOCI-CODE binary, Git repository, MCP-compatible coding host such as Codex, Claude Code, Cursor, or OpenCode, optional MySQL/PostgreSQL/openGauss schema access

## Installation

Install or set up from the source-backed instructions:

Download a signed AOCI-CODE release from GitHub, verify it using the upstream installation guide, run aoci init for the target repository, restart or reconnect the MCP host, then ask the agent to confirm the AOCI MCP server is connected and build the project index.

- Source: https://github.com/aoci-spec/aoci-code

## Documentation

- https://github.com/aoci-spec/aoci-code

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maintain-a-git-versioned-codebase-index-for-coding-agents-with-aoci-code/)
