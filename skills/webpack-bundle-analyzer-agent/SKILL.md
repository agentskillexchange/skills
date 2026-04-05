---
name: "Webpack Bundle Analyzer Agent"
description: "Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/webpack-bundle-analyzer-agent/"
---
# Webpack Bundle Analyzer Agent

Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites.

Webpack Bundle Analyzer Agent is built around Webpack bundler for JavaScript applications. The underlying ecosystem is represented by webpack/webpack (66,013+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like bundle graphs, loaders, plugins, source maps, tree-shaking, code splitting and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to webpack so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites. The implementation typically relies on bundle graphs, loaders, plugins, source maps, tree-shaking, code splitting, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses bundle graphs, loaders, plugins, source maps, tree-shaking, code splitting instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as frontend build optimization, asset analysis, and bundle diagnostics.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include frontend build optimization, asset analysis, and bundle diagnostics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install webpack-bundle-analyzer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webpack-bundle-analyzer-agent/)
