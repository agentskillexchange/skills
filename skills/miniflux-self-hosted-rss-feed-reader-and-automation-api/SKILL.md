---
title: "Miniflux Self-Hosted RSS Feed Reader and Automation API"
description: "Miniflux is a self-hosted feed reader built for people who want a fast, opinionated, and low-noise way to follow websites and feeds. The upstream project supports Atom, RSS, and JSON Feed, exposes a REST API, offers webhooks, and includes integrations with services such as Slack, Telegram, Notion, and ntfy. It is maintained in the miniflux/v2 repository and documented on miniflux.app.\nThis skill is useful when an agent needs to monitor many feeds without depending on a hosted dashboard. It can create categories, import OPML files, subscribe to feeds, process unread entries, filter content, and forward selected items into downstream systems. Because Miniflux includes an API and webhook model, it also works well for automation jobs like daily briefings, article classification, research inboxes, and lightweight alerting flows.\nThe technical integration points are straightforward: deploy Miniflux with its documented setup, connect the application to its supported database and web interface, then use the REST API or webhook triggers to automate retrieval and follow-up actions. This makes it a good fit for agents that need structured feed ingestion, human-readable review queues, and integrations with chat, bookmarking, or personal knowledge tools. Between the official GitHub repository, official docs, Apache-licensed source, and active maintenance, Miniflux passes the intake gate as a real and adoptable upstream tool."
verification: security_reviewed
source: "https://github.com/miniflux/v2"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "miniflux/v2"
  github_stars: 9064
---

# Miniflux Self-Hosted RSS Feed Reader and Automation API

Miniflux is a self-hosted feed reader built for people who want a fast, opinionated, and low-noise way to follow websites and feeds. The upstream project supports Atom, RSS, and JSON Feed, exposes a REST API, offers webhooks, and includes integrations with services such as Slack, Telegram, Notion, and ntfy. It is maintained in the miniflux/v2 repository and documented on miniflux.app.
This skill is useful when an agent needs to monitor many feeds without depending on a hosted dashboard. It can create categories, import OPML files, subscribe to feeds, process unread entries, filter content, and forward selected items into downstream systems. Because Miniflux includes an API and webhook model, it also works well for automation jobs like daily briefings, article classification, research inboxes, and lightweight alerting flows.
The technical integration points are straightforward: deploy Miniflux with its documented setup, connect the application to its supported database and web interface, then use the REST API or webhook triggers to automate retrieval and follow-up actions. This makes it a good fit for agents that need structured feed ingestion, human-readable review queues, and integrations with chat, bookmarking, or personal knowledge tools. Between the official GitHub repository, official docs, Apache-licensed source, and active maintenance, Miniflux passes the intake gate as a real and adoptable upstream tool.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/miniflux-self-hosted-rss-feed-reader-and-automation-api
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/miniflux-self-hosted-rss-feed-reader-and-automation-api` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/miniflux-self-hosted-rss-feed-reader-and-automation-api/)
