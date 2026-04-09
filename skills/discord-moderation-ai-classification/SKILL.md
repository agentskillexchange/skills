---
title: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
slug: "discord-moderation-ai-classification"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/discord-moderation-ai-classification/"
category:
  - "Security & Verification"
framework:
  - "Cursor"
---
# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Add as a local skill folder
3. Install from a Git repository
4. Install via package manager if supported
5. Copy the skill into your OpenClaw skills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
