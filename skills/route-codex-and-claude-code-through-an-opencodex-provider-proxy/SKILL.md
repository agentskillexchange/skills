---
name: "Route Codex and Claude Code through an opencodex provider proxy"
slug: "route-codex-and-claude-code-through-an-opencodex-provider-proxy"
description: "Run a local proxy that lets Codex and Claude Code use configured LLM providers, routed models, and account pools while keeping the normal coding-agent workflow."
github_stars: 1285
verification: "security_reviewed"
source: "https://github.com/lidge-jun/opencodex"
author: "lidge-jun"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "lidge-jun/opencodex"
  github_stars: 1285
  npm_package: "@bitkyc08/opencodex"
  npm_weekly_downloads: 23960
---

# Route Codex and Claude Code through an opencodex provider proxy

Run a local proxy that lets Codex and Claude Code use configured LLM providers, routed models, and account pools while keeping the normal coding-agent workflow.

## Prerequisites

Node.js 18+, @bitkyc08/opencodex, Codex CLI/App/SDK or Claude Code, provider credentials or OAuth

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @bitkyc08/opencodex
- npm install -g --allow-scripts=bun @bitkyc08/opencodex # no --ignore-scripts, no --omit=optional
- npm's own warning suggests an abbreviated command without the package name —
- npm uninstall -g @bitkyc08/opencodex

Requirements and caveats from upstream:
- <img src="https://img.shields.io/node/v/@bitkyc08/opencodex?logo=node.js&label=node" alt="node version">
- Requires [Node](https://nodejs.org) 18+. The Bun runtime is bundled automatically on npm install — no separate Bun install needed. All three platforms work natively (no WSL needed on Windows).
- opencodex bundles the Bun runtime as a dependency and runs it via a Node

Basic usage or getting-started notes:
- lowest-usage healthy account. Existing Codex threads stay pinned to the account that started them,
- quota --> pick[Pick lowest-usage<br/>healthy account]
- ocx init

- Source: https://github.com/lidge-jun/opencodex
- Extracted from upstream docs: https://raw.githubusercontent.com/lidge-jun/opencodex/HEAD/README.md

## Documentation

- https://lidge-jun.github.io/opencodex/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/route-codex-and-claude-code-through-an-opencodex-provider-proxy/)
