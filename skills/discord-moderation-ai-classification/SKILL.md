---
title: "Discord Moderation Bot with AI Classification"
slug: "discord-moderation-ai-classification"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/discord-moderation-ai-classification/"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
---
# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
