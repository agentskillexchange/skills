---
title: "Webpack Bundle Analyzer Agent"
description: "Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites."
verification: security_reviewed
source: "https://github.com/webpack/webpack"
category:
  - "Developer Tools"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "webpack/webpack"
  github_stars: 65837
  npm_package: "webpack"
  npm_weekly_downloads: 44532842
  license: "MIT"
---

# Webpack Bundle Analyzer Agent

Webpack Bundle Analyzer Agent is built around Webpack bundler for JavaScript applications. The underlying ecosystem is represented by webpack/webpack (66,013+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like bundle graphs, loaders, plugins, source maps, tree-shaking, code splitting and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to webpack so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites. The implementation typically relies on bundle graphs, loaders, plugins, source maps, tree-shaking, code splitting, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses bundle graphs, loaders, plugins, source maps, tree-shaking, code splitting instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as frontend build optimization, asset analysis, and bundle diagnostics.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include frontend build optimization, asset analysis, and bundle diagnostics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/webpack-bundle-analyzer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/webpack-bundle-analyzer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webpack-bundle-analyzer-agent/)
