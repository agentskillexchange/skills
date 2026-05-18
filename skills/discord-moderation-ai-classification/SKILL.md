---
name: "Discord Moderation Bot with AI Classification"
slug: "discord-moderation-ai-classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
github_stars: 26668
verification: "listed"
source: "https://github.com/discordjs/discord.js"
category: "Security & Verification"
framework: "Cursor"
tool_ecosystem:
  github_repo: "discordjs/discord.js"
  github_stars: 26668
  npm_package: "discord.js"
  npm_weekly_downloads: 563530
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

Requirements and caveats from upstream:
- This repository contains multiple packages with separate [releases][github-releases]. You can find the assembled Discord API wrapper at [discord.js][source]. It is a powerful [Node.js](https://nodejs.org/en) module th...
- discord.js ([source][source]) - A powerful Node.js module for interacting with the Discord API

- Source: https://github.com/discordjs/discord.js
- Extracted from upstream docs: https://raw.githubusercontent.com/discordjs/discord.js/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
