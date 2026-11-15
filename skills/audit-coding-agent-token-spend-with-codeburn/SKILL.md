---
name: "Audit coding-agent token spend with CodeBurn"
slug: "audit-coding-agent-token-spend-with-codeburn"
description: "Run CodeBurn locally or as an MCP server so agents can inspect token usage, cost, model mix, project spend, and budget waste across coding tools."
github_stars: 8722
verification: "security_reviewed"
source: "https://github.com/getagentseal/codeburn"
author: "AgentSeal"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "getagentseal/codeburn"
  github_stars: 8722
  npm_package: "codeburn"
  npm_weekly_downloads: 7621
---

# Audit coding-agent token spend with CodeBurn

Run CodeBurn locally or as an MCP server so agents can inspect token usage, cost, model mix, project spend, and budget waste across coding tools.

## Prerequisites

Node.js 22.13+; local session data from supported AI coding tools; optional Claude Code, Cursor, or another MCP client for `codeburn mcp`

## Installation

Use the upstream install or setup path that matches your environment:
- npx codeburn
- npm install -g codeburn
- git clone https://github.com/getagentseal/codeburn && cd codeburn/gnome

Requirements and caveats from upstream:
- <a href="https://github.com/getagentseal/codeburn"><img src="https://img.shields.io/badge/node-%3E%3D22-F97316.svg" alt="node version" /></a>
- Requires **Node.js 22.13+** and at least one supported tool with session data on disk. For Cursor and OpenCode, better-sqlite3 installs automatically.
- Requires a git repository. Run from your project directory.

Basic usage or getting-started notes:
- **CodeBurn is a free, open-source, local-first tool that tracks AI coding token usage and cost across 36 tools and agents (Claude Code, Cursor, Codex, Gemini, Grok and more), broken down by model, project, and task.**
- <a href="#quick-start">Quick start</a> ·
- **Run it instantly**, no install needed:

- Source: https://github.com/getagentseal/codeburn
- Extracted from upstream docs: https://raw.githubusercontent.com/getagentseal/codeburn/HEAD/README.md

## Documentation

- https://codeburn.app/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-coding-agent-token-spend-with-codeburn/)
