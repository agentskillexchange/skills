---
title: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/discord-moderation-ai-classification/"
categories:
  - "Security &amp; Verification"
frameworks:
  - "Cursor"
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

You can install this skill using one of these methods:

1. Install from Agent Skill Exchange in OpenClaw
2. Install from ClawHub
3. Copy the skill folder into your local skills directory
4. Add it as a git submodule or synced folder in your workspace
5. Use your team or org skill distribution workflow

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
