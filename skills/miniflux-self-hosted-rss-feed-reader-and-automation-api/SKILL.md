---
name: "Miniflux Self-Hosted RSS Feed Reader and Automation API"
description: "Use Miniflux to run a minimalist self-hosted feed reader with a clean web UI, webhooks, and API integrations. This skill helps agents subscribe to sources, organize categories, and automate article triage or downstream alerting from RSS, Atom, and JSON feeds."
verification: security_reviewed
source: "https://github.com/miniflux/v2"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
---

# Miniflux Self-Hosted RSS Feed Reader and Automation API

Miniflux is a self-hosted feed reader built for people who want a fast, opinionated, and low-noise way to follow websites and feeds. The upstream project supports Atom, RSS, and JSON Feed, exposes a REST API, offers webhooks, and includes integrations with services such as Slack, Telegram, Notion, and ntfy. It is maintained in the miniflux/v2 repository and documented on miniflux.app.
This skill is useful when an agent needs to monitor many feeds without depending on a hosted dashboard. It can create categories, import OPML files, subscribe to feeds, process unread entries, filter content, and forward selected items into downstream systems. Because Miniflux includes an API and webhook model, it also works well for automation jobs like daily briefings, article classification, research inboxes, and lightweight alerting flows.
The technical integration points are straightforward: deploy Miniflux with its documented setup, connect the application to its supported database and web interface, then use the REST API or webhook triggers to automate retrieval and follow-up actions. This makes it a good fit for agents that need structured feed ingestion, human-readable review queues, and integrations with chat, bookmarking, or personal knowledge tools. Between the official GitHub repository, official docs, Apache-licensed source, and active maintenance, Miniflux passes the intake gate as a real and adoptable upstream tool.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/miniflux-self-hosted-rss-feed-reader-and-automation-api/)
