---
title: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
verification: "security_reviewed"
source: "https://github.com/discordjs/discord.js"
category:
  - "Security & Verification"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "discordjs/discord.js"
  github_stars: 26668
  ase_npm_package: "discord.js"
  npm_weekly_downloads: 563530
  license: "Apache-2.0"
---

# Discord Moderation Bot with AI Classification

Discord Moderation Bot with AI Classification is built around Discord bot and moderation platform. The underlying ecosystem is represented by discordjs/discord.js (26,650+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like gateway events, slash commands, REST API, webhooks, intents, role actions and preserving the operational context that matters for real tasks.


In practice, the skill gives an agent a stable interface to discord so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart. The implementation typically relies on gateway events, slash commands, REST API, webhooks, intents, role actions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.



Accesses gateway events, slash commands, REST API, webhooks, intents, role actions instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as community bots, moderation, logging, and workflow notifications.

 Key integration points include community bots, moderation, logging, and workflow notifications. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
