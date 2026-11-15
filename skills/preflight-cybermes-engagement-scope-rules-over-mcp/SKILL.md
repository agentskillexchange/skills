---
name: "Preflight Cybermes engagement scope rules over MCP"
slug: "preflight-cybermes-engagement-scope-rules-over-mcp"
description: "Test existing engagement scope rules against allowed and excluded fixtures, check local tool readiness, and return a preflight record before target activity."
github_stars: 1026
verification: "security_reviewed"
source: "https://github.com/Zyrexnn/Cybermes"
author: "Zyrexnn"
publisher_type: "individual"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "Zyrexnn/Cybermes"
  github_stars: 1026
---

# Preflight Cybermes engagement scope rules over MCP

Test existing engagement scope rules against allowed and excluded fixtures, check local tool readiness, and return a preflight record before target activity.

## Prerequisites

Go 1.26.0 or compatible newer toolchain; Git; native Cybermes MCP server; MCP client; existing reviewed scope files and fixture expectations

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/Zyrexnn/Cybermes.git, check out a908afc2afc279e53dc4bd1bc07087157bd55b4e, and from its root run go build -o tools/bin/cybermes-mcp ./cmd/cybermes-mcp using Go 1.26.0 or compatible newer tooling. Configure the MCP client with the absolute binary path and arguments --workspace /absolute/path/to/Cybermes. Review the existing scope files before starting. This source-build route avoids assuming an npm package version matches the inspected code.

- Source: https://github.com/Zyrexnn/Cybermes

## Documentation

- https://github.com/Zyrexnn/Cybermes/blob/a908afc2afc279e53dc4bd1bc07087157bd55b4e/docs/MCP_SETUP.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/preflight-cybermes-engagement-scope-rules-over-mcp/)
