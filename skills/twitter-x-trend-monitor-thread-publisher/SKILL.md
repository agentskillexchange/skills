---
title: "Twitter/X Trend Monitor &amp; Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
slug: "twitter-x-trend-monitor-thread-publisher"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
category:
  - "Templates &amp; Workflows"
---

# Twitter/X Trend Monitor &amp; Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

You can install this skill in any of these ways:

1. Install from Agent Skill Exchange in the OpenClaw UI
2. Clone or copy the skill folder into your local skills directory
3. Add it to your workspace-managed skills collection
4. Install via any compatible skill package manager or sync workflow
5. Copy the `SKILL.md` and any referenced files into a compatible AgentSkills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
