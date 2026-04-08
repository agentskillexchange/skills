---
title: Slack Standup Summarizer
description: 'The Slack Standup Summarizer skill monitors designated Slack channels
  for daily standup messages using the conversations.history Web API endpoint. It
  identifies standup entries by timestamp windows, thread patterns, or bot-prompted
  responses and extracts structured data from free-form updates. The summarizer parses
  standup messages to identify three components: completed work, planned work, and
  blockers. Natural language processing detects blocker keywords and escalation signals
  even when not explicitly formatted. Cross-referencing with Jira or Linear ticket
  numbers provides automatic status linking. Digest generation produces formatted
  Slack Block Kit messages with sections for each team member, highlighted blockers
  with suggested owners, and sprint progress indicators. Digests post to configurable
  channels via Incoming Webhooks with optional threading under a daily parent message.
  Historical data aggregation tracks individual velocity trends, recurring blockers,
  and team completion rates over configurable time windows.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/slack-standup-summarizer/
category:
- Calendar, Email &amp; Productivity
framework:
- Claude Agents
---

# Slack Standup Summarizer

The Slack Standup Summarizer skill monitors designated Slack channels for daily standup messages using the conversations.history Web API endpoint. It identifies standup entries by timestamp windows, thread patterns, or bot-prompted responses and extracts structured data from free-form updates. The summarizer parses standup messages to identify three components: completed work, planned work, and blockers. Natural language processing detects blocker keywords and escalation signals even when not explicitly formatted. Cross-referencing with Jira or Linear ticket numbers provides automatic status linking. Digest generation produces formatted Slack Block Kit messages with sections for each team member, highlighted blockers with suggested owners, and sprint progress indicators. Digests post to configurable channels via Incoming Webhooks with optional threading under a daily parent message. Historical data aggregation tracks individual velocity trends, recurring blockers, and team completion rates over configurable time windows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-summarizer/)
