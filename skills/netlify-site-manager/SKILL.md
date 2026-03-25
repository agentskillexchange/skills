---
name: "Netlify Site Manager"
description: "Netlify Site Manager is built around Netlify deployment platform. The underlying ecosystem is represented by netlify/cli (1,837+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like sites API, deploy previews, functions, env vars, build hooks, edge functions and […]"
category: "Templates & Workflows"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/netlify-site-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "netlify"  # from ase_tool_match
  github_stars: 1837  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 383701  # from ase_npm_downloads
  github_repo: "netlify/cli"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Netlify Site Manager

Netlify Site Manager is built around Netlify deployment platform. The underlying ecosystem is represented by netlify/cli (1,837+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like sites API, deploy previews, functions, env vars, build hooks, edge functions and […]

## Overview

**Netlify Site Manager** is built around Netlify deployment platform. The underlying ecosystem is represented by `netlify/cli` (1,837+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like sites API, deploy previews, functions, env vars, build hooks, edge functions and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to netlify so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on sites API, deploy previews, functions, env vars, build hooks, edge functions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses sites API, deploy previews, functions, env vars, build hooks, edge functions instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as frontend hosting, preview environments, and Jamstack deployment automation.

Key integration points include frontend hosting, preview environments, and Jamstack deployment automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill netlify-site-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill netlify-site-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill netlify-site-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill netlify-site-manager -a codex
```

### OpenClaw

```bash
clawhub install netlify-site-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/netlify-site-manager/
