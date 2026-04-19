---
title: "Gotify Self-Hosted Push Notification Server and API"
description: "Gotify is an open-source push notification server for teams that want a simple, self-hosted way to send and receive messages in real time. The upstream gotify/server project exposes a REST API for publishing notifications, a WebSocket stream for receiving them, a web UI for managing users and applications, and documented plugin support. Official documentation covers installation, configuration, API usage, and development setup. This skill is built for operational and automation workflows where an agent needs to turn events into notifications. It can create or manage Gotify applications, post alerts from scripts or monitoring pipelines, route important state changes into a notification feed, and use the WebSocket stream for live updates. That makes it suitable for uptime alerts, deployment messages, cron summaries, build notifications, and private system messages where self-hosting and data control matter. From an integration standpoint, Gotify works especially well with REST-driven tools, shell scripts, servers, monitoring jobs, and internal dashboards. Agents can pair it with background tasks, diagnostics, CI systems, or custom services that emit status events. The project has an official GitHub repo, official docs, tags and releases, and an explicit MIT license in the upstream README, so it satisfies the evidence and adoption gate for ASE publication."
source: "https://github.com/gotify/server"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gotify/server"
  github_stars: 14868
---

# Gotify Self-Hosted Push Notification Server and API

Gotify is an open-source push notification server for teams that want a simple, self-hosted way to send and receive messages in real time. The upstream gotify/server project exposes a REST API for publishing notifications, a WebSocket stream for receiving them, a web UI for managing users and applications, and documented plugin support. Official documentation covers installation, configuration, API usage, and development setup. This skill is built for operational and automation workflows where an agent needs to turn events into notifications. It can create or manage Gotify applications, post alerts from scripts or monitoring pipelines, route important state changes into a notification feed, and use the WebSocket stream for live updates. That makes it suitable for uptime alerts, deployment messages, cron summaries, build notifications, and private system messages where self-hosting and data control matter. From an integration standpoint, Gotify works especially well with REST-driven tools, shell scripts, servers, monitoring jobs, and internal dashboards. Agents can pair it with background tasks, diagnostics, CI systems, or custom services that emit status events. The project has an official GitHub repo, official docs, tags and releases, and an explicit MIT license in the upstream README, so it satisfies the evidence and adoption gate for ASE publication.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gotify-self-hosted-push-notification-server-and-api/)
