---
name: "Delegate scoped coding tasks to T3 Code threads over MCP"
slug: "delegate-scoped-coding-tasks-to-t3-code-threads-over-mcp"
description: "Launch a bounded coding task from an outside MCP assistant, follow its T3 Code thread, and return the result and changes for operator review."
github_stars: 58085
verification: "security_reviewed"
source: "https://github.com/pingdotgg/t3code"
author: "pingdotgg / T3 Tools"
publisher_type: "community"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "pingdotgg/t3code"
  github_stars: 58085
  npm_package: "t3"
  npm_weekly_downloads: 0
---

# Delegate scoped coding tasks to T3 Code threads over MCP

Launch a bounded coding task from an outside MCP assistant, follow its T3 Code thread, and return the result and changes for operator review.

## Prerequisites

Node.js >=20.11 for npx, T3 Code v0.1.9 server, configured coding-provider CLI, Git repository, HTTP/OAuth-capable MCP client

## Installation

Install or set up from the source-backed instructions:

With Node.js >=20.11, run npx t3@0.1.9 to start the upstream server, or install the v0.1.9 desktop release. Configure a coding provider, copy the environment MCP URL from Settings > Environments, register it in an HTTP/OAuth-capable MCP client, and have the operator approve the required access level. Follow the pinned release documentation and project/toolkit schemas.

- Source: https://github.com/pingdotgg/t3code

## Documentation

- https://github.com/pingdotgg/t3code/blob/24e77473ecf41bc1f7142529c7911c1c1aae1d76/docs/user/outside-agents.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/delegate-scoped-coding-tasks-to-t3-code-threads-over-mcp/)
