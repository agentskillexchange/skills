---
title: "Discord Moderation Bot with AI Classification"
slug: "discord-moderation-ai-classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
verification: security_reviewed
source: "https://github.com/discordjs/discord.js"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "discordjs/discord.js"
  github_stars: 26668
  npm_package: "discord.js"
  npm_weekly_downloads: 563530
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
