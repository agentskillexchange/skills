---
title: Gotify Self-Hosted Push Notification Server and API
description: Gotify is an open-source push notification server for teams that want
  a simple, self-hosted way to send and receive messages in real time. The upstream
  gotify/server project exposes a REST API for publishing notifications, a WebSocket
  stream for receiving them, a web UI for managing users and applications, and documented
  plugin support. Official documentation covers installation, configuration, API usage,
  and development setup. This skill is built for operational and automation workflows
  where an agent needs to turn events into notifications. It can create or manage
  Gotify applications, post alerts from scripts or monitoring pipelines, route important
  state changes into a notification feed, and use the WebSocket stream for live updates.
  That makes it suitable for uptime alerts, deployment messages, cron summaries, build
  notifications, and private system messages where self-hosting and data control matter.
  From an integration standpoint, Gotify works especially well with REST-driven tools,
  shell scripts, servers, monitoring jobs, and internal dashboards. Agents can pair
  it with background tasks, diagnostics, CI systems, or custom services that emit
  status events. The project has an official GitHub repo, official docs, tags and
  releases, and an explicit MIT license in the upstream README, so it satisfies the
  evidence and adoption gate for ASE publication.
verification: security_reviewed
source: https://github.com/gotify/server
category:
- Monitoring &amp; Alerts
framework:
- Multi-Framework
---

# Gotify Self-Hosted Push Notification Server and API

Gotify is an open-source push notification server for teams that want a simple, self-hosted way to send and receive messages in real time. The upstream gotify/server project exposes a REST API for publishing notifications, a WebSocket stream for receiving them, a web UI for managing users and applications, and documented plugin support. Official documentation covers installation, configuration, API usage, and development setup. This skill is built for operational and automation workflows where an agent needs to turn events into notifications. It can create or manage Gotify applications, post alerts from scripts or monitoring pipelines, route important state changes into a notification feed, and use the WebSocket stream for live updates. That makes it suitable for uptime alerts, deployment messages, cron summaries, build notifications, and private system messages where self-hosting and data control matter. From an integration standpoint, Gotify works especially well with REST-driven tools, shell scripts, servers, monitoring jobs, and internal dashboards. Agents can pair it with background tasks, diagnostics, CI systems, or custom services that emit status events. The project has an official GitHub repo, official docs, tags and releases, and an explicit MIT license in the upstream README, so it satisfies the evidence and adoption gate for ASE publication.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gotify-self-hosted-push-notification-server-and-api/)
