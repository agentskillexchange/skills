---
name: "Connect agents to governed data and code graphs with GraphJin"
slug: "connect-agents-to-governed-data-and-code-graphs-with-graphjin"
description: "Expose databases, files, code indexes, workflows, and policy-aware GraphQL through GraphJin's MCP and agent endpoints for governed discovery and action."
github_stars: 3087
verification: "security_reviewed"
source: "https://github.com/dosco/graphjin"
author: "GraphJin"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "dosco/graphjin"
  github_stars: 3087
  npm_package: "graphjin"
  npm_weekly_downloads: 866
---

# Connect agents to governed data and code graphs with GraphJin

Expose databases, files, code indexes, workflows, and policy-aware GraphQL through GraphJin's MCP and agent endpoints for governed discovery and action.

## Prerequisites

GraphJin CLI or server; approved database/file/code sources; Codex, Claude Code, or another MCP-capable client; optional Docker, Homebrew, npm, or Scoop install path

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g graphjin
- brew install dosco/graphjin/graphjin
- docker pull dosco/graphjin
- git clone https://github.com/dosco/graphjin

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/dosco/graphjin?style=for-the-badge)](https://hub.docker.com/r/dosco/graphjin/tags)
- **Docker**
- One command, no clone, no Docker. The binary ships with a built-in demo — a

Basic usage or getting-started notes:
- **Durable memory and standing questions** - Saved queries, fragments, and workflows live in the owner-scoped gj_artifacts store; cursor-backed watches (gj_watch) run standing questions under the owner's permissions, r...
- **npm (all platforms)**
- **macOS (Homebrew)**

- Source: https://github.com/dosco/graphjin
- Extracted from upstream docs: https://raw.githubusercontent.com/dosco/graphjin/HEAD/README.md

## Documentation

- https://graphjin.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-agents-to-governed-data-and-code-graphs-with-graphjin/)
