---
name: "Aident Loadout"
slug: "aident-loadout"
description: "Give Claude Code, Codex, Cursor, ChatGPT and other MCP clients 1,000+ apps and 400+ expert-built Skills through one reusable Aident Loadout setup, with credentials kept in Aident Vault and every action recorded in Audit."
github_stars: 6
verification: "listed"
source: "https://github.com/Aident-AI/aident-skill"
author: "Aident-AI"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "aident-ai/aident-skill"
  github_stars: 6
  npm_package: "@aident-ai/cli"
  npm_weekly_downloads: 3114
---

# Aident Loadout

Use this skill when an agent needs to act in real apps (for example Gmail, Slack, GitHub, Linear, Notion, Google Sheets or HubSpot) and you want one setup that works across every agent instead of wiring each tool separately. [Aident Loadout](https://aident.ai) is a capability layer for AI agents: you connect your accounts once and any supported client (Claude Code, Codex, Cursor, ChatGPT, Claude Desktop, OpenCode, OpenClaw or any MCP-compatible client) can use them.

The agent searches 1,000+ apps and their actions by intent, reads the live input schema, and then runs the action through the remote MCP server or the `aident` CLI. It can also start from 400+ expert-built Skills for research, outreach, content and operations work. OAuth connections are authorized in the browser, and API keys stay in Aident Vault, so the model receives results rather than raw credentials. Before an action runs, Loadout reports what it will cost; afterwards, Audit records what ran, which agent started it, whether it succeeded and what it cost. More than 50 built-in services such as search, scraping and media generation run on one Aident balance. A missing app can be requested or connected as a custom app from its API.

## When to use it

- An agent task needs authenticated actions in third-party apps and you do not want to manage per-app MCP servers.
- The same connected accounts should be reused across several agents or machines.
- You need a cost check before an action and an audit trail after it.

## Installation

Install or set up from the source-backed instructions:

npx -y @aident-ai/cli@latest update --skill-only
Then follow https://aident.ai/SETUP.md to complete Aident Loadout setup.

- Source: https://github.com/Aident-AI/aident-skill

## Verify

Ask the agent to list its Aident tools. You should see tools for auth, capability search, capability execute, and Vault/integrations.

- Website: https://aident.ai
- Docs: https://docs.aident.ai/loadout/overview
- Source: https://github.com/Aident-AI/aident-skill
