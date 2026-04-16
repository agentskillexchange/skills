---
title: "Netlify Site Manager"
description: "Netlify Site Manager is built around Netlify deployment platform. The underlying ecosystem is represented by netlify/cli (1,837+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like sites API, deploy previews, functions, env vars, build hooks, edge functions and […]"
verification: "security_reviewed"
source: "https://github.com/netlify/cli"
category:
  - "Templates &amp; Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "netlify/cli"
  github_stars: 1843
  ase_npm_package: "netlify-cli"
  npm_weekly_downloads: 266782
---

# Netlify Site Manager

Netlify Site Manager is built around Netlify deployment platform. The underlying ecosystem is represented by netlify/cli (1,837+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like sites API, deploy previews, functions, env vars, build hooks, edge functions and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to netlify so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on sites API, deploy previews, functions, env vars, build hooks, edge functions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses sites API, deploy previews, functions, env vars, build hooks, edge functions instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as frontend hosting, preview environments, and Jamstack deployment automation.

Key integration points include frontend hosting, preview environments, and Jamstack deployment automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/netlify-site-manager/)
