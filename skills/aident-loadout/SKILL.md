---
name: "Aident Loadout"
slug: "aident-loadout"
description: "Give Claude Code, Codex, Cursor, ChatGPT and other MCP clients 1,000+ apps and 400+ expert-built Skills through one reusable Aident Loadout setup, with credentials kept in Aident Vault and every action recorded in Audit."
verification: listed
source: "https://github.com/Aident-AI/aident-skill"
author: "Aident-AI"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "Aident-AI/aident-skill"
---

# Aident Loadout

Use this skill when an agent needs to act in real apps (for example Gmail, Slack, GitHub, Linear, Notion, Google Sheets or HubSpot) and you want one setup that works across every agent instead of wiring each tool separately. [Aident Loadout](https://aident.ai) is a capability layer for AI agents: you connect your accounts once and any supported client (Claude Code, Codex, Cursor, ChatGPT, Claude Desktop, OpenCode, OpenClaw or any MCP-compatible client) can use them.

The agent searches 1,000+ apps and their actions by intent, reads the live input schema, and then runs the action through the remote MCP server or the `aident` CLI. It can also start from 400+ expert-built Skills for research, outreach, content and operations work. OAuth connections are authorized in the browser, and API keys stay in Aident Vault, so the model receives results rather than raw credentials. Before an action runs, Loadout reports what it will cost; afterwards, Audit records what ran, which agent started it, whether it succeeded and what it cost. More than 50 built-in services such as search, scraping and media generation run on one Aident balance. A missing app can be requested or connected as a custom app from its API.

## When to use it

- An agent task needs authenticated actions in third-party apps and you do not want to manage per-app MCP servers.
- The same connected accounts should be reused across several agents or machines.
- You need a cost check before an action and an audit trail after it.

## Installation

### Remote MCP server (Claude Code)

```bash
claude mcp add --transport http aident https://loadout.aident.ai/mcp
```

The server uses Streamable HTTP and asks you to sign in with OAuth on first use. ChatGPT and Claude Desktop can add the same URL as a custom app or connector.

### Coding agents

Paste this setup prompt into Codex, Claude Code, Cursor, OpenCode or OpenClaw:

```text
Follow https://aident.ai/SETUP.md
```

### CLI and static skill

```bash
npm i -g @aident-ai/cli
aident login
npx -y @aident-ai/cli@latest update --skill-only
```

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/aident-loadout ~/.agent-skills/aident-loadout
```

## Verify

Ask the agent to list its Aident tools. You should see tools for auth, capability search, capability execute, and Vault/integrations.

- Website: https://aident.ai
- Docs: https://docs.aident.ai/loadout/overview
- Source: https://github.com/Aident-AI/aident-skill
