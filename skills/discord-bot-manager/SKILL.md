---
name: "Discord Bot Manager"
description: "Discord Bot Manager is built around Discord bot and moderation platform. The underlying ecosystem is represented by discordjs/discord.js (26,650+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like gateway events, slash commands, REST API, webhooks, intents, role actions […]"
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/discord-bot-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "discord"  # from ase_tool_match
  github_stars: 26650  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 508798  # from ase_npm_downloads
  github_repo: "discordjs/discord.js"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Discord Bot Manager

Discord Bot Manager is built around Discord bot and moderation platform. The underlying ecosystem is represented by discordjs/discord.js (26,650+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like gateway events, slash commands, REST API, webhooks, intents, role actions […]

## Overview

**Discord Bot Manager** is built around Discord bot and moderation platform. The underlying ecosystem is represented by `discordjs/discord.js` (26,650+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like gateway events, slash commands, REST API, webhooks, intents, role actions and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to discord so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on gateway events, slash commands, REST API, webhooks, intents, role actions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses gateway events, slash commands, REST API, webhooks, intents, role actions instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as community bots, moderation, logging, and workflow notifications.

Key integration points include community bots, moderation, logging, and workflow notifications. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill discord-bot-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill discord-bot-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill discord-bot-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill discord-bot-manager -a codex
```

### OpenClaw

```bash
clawhub install discord-bot-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/discord-bot-manager/
