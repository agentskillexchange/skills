---
title: "Gotify Self-Hosted Push Notification Server and API"
description: "Run self-hosted push notifications with Gotify, including a REST API, WebSocket stream, web UI, plugins, and mobile clients. This skill helps agents send alerts, manage applications, and connect monitored events to a private notification channel instead of relying on third-party push vendors."
slug: "gotify-self-hosted-push-notification-server-and-api"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/gotify/server"
---

# Gotify Self-Hosted Push Notification Server and API

Run self-hosted push notifications with Gotify, including a REST API, WebSocket stream, web UI, plugins, and mobile clients. This skill helps agents send alerts, manage applications, and connect monitored events to a private notification channel instead of relying on third-party push vendors.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install gotify-self-hosted-push-notification-server-and-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Gotify is an open-source push notification server for teams that want a simple, self-hosted way to send and receive messages in real time. The upstream gotify/server project exposes a REST API for publishing notifications, a WebSocket stream for receiving them, a web UI for managing users and applications, and documented plugin support. Official documentation covers installation, configuration, API usage, and development setup.
This skill is built for operational and automation workflows where an agent needs to turn events into notifications. It can create or manage Gotify applications, post alerts from scripts or monitoring pipelines, route important state changes into a notification feed, and use the WebSocket stream for live updates. That makes it suitable for uptime alerts, deployment messages, cron summaries, build notifications, and private system messages where self-hosting and data control matter.
From an integration standpoint, Gotify works especially well with REST-driven tools, shell scripts, servers, monitoring jobs, and internal dashboards. Agents can pair it with background tasks, diagnostics, CI systems, or custom services that emit status events. The project has an official GitHub repo, official docs, tags and releases, and an explicit MIT license in the upstream README, so it satisfies the evidence and adoption gate for ASE publication.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gotify-self-hosted-push-notification-server-and-api/)
