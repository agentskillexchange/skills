---
title: ntfy Self-Hosted Push Notification Server
description: 'What is ntfy? ntfy (pronounced “notify”) is a lightweight, open-source
  push notification server written in Go. It implements a simple HTTP-based publish-subscribe
  pattern that lets any script, application, or service send real-time notifications
  to phones and desktops without requiring accounts, API keys, or complex configuration.
  How It Works At its core, ntfy exposes HTTP endpoints where you publish messages
  with a simple PUT or POST request. Subscribers receive these messages in real-time
  via the ntfy web app, Android app (Google Play and F-Droid), or iOS app. The entire
  interaction model is based on topics — named channels that anyone can publish to
  or subscribe to. A basic notification is as simple as: curl -d "Backup completed
  successfully" ntfy.sh/my-alerts . That single command sends a push notification
  to any device subscribed to the “my-alerts” topic. No authentication required for
  the public instance, though self-hosted instances support access control, user management,
  and token-based auth. Key Features ntfy supports rich notifications with titles,
  priorities (urgent, high, default, low, min), tags and emojis, click actions, file
  attachments up to 15MB, scheduled delivery with delay headers, and end-to-end encryption.
  The server can also forward notifications via email, making it a bridge between
  HTTP events and traditional notification channels. For agent integration, ntfy provides
  a clean REST API for both publishing and subscribing. Messages can include structured
  JSON payloads, making it suitable for automation pipelines where downstream consumers
  need to parse notification content programmatically. Self-Hosting and Deployment
  ntfy is distributed as a single static binary, a Docker image, and Debian/RPM packages.
  Self-hosting requires minimal resources — it runs comfortably on a Raspberry Pi.
  The server stores messages in a SQLite database with configurable retention, supports
  WebSocket connections for real-time subscriptions, and provides a built-in web UI
  for monitoring topics. Integration Points Common integrations include monitoring
  alerts from Prometheus or Grafana, CI/CD pipeline notifications from GitHub Actions
  or Jenkins, cron job status reports, home automation events, and any script that
  needs to notify a human. The simplicity of the HTTP API means any language or tool
  that can make HTTP requests can use ntfy as a notification backend.'
verification: listed
source: https://github.com/binwiederhier/ntfy
category:
- Integrations &amp; Connectors
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: binwiederhier/ntfy
  github_stars: 29493
---

# ntfy Self-Hosted Push Notification Server

What is ntfy? ntfy (pronounced “notify”) is a lightweight, open-source push notification server written in Go. It implements a simple HTTP-based publish-subscribe pattern that lets any script, application, or service send real-time notifications to phones and desktops without requiring accounts, API keys, or complex configuration. How It Works At its core, ntfy exposes HTTP endpoints where you publish messages with a simple PUT or POST request. Subscribers receive these messages in real-time via the ntfy web app, Android app (Google Play and F-Droid), or iOS app. The entire interaction model is based on topics — named channels that anyone can publish to or subscribe to. A basic notification is as simple as: curl -d "Backup completed successfully" ntfy.sh/my-alerts . That single command sends a push notification to any device subscribed to the “my-alerts” topic. No authentication required for the public instance, though self-hosted instances support access control, user management, and token-based auth. Key Features ntfy supports rich notifications with titles, priorities (urgent, high, default, low, min), tags and emojis, click actions, file attachments up to 15MB, scheduled delivery with delay headers, and end-to-end encryption. The server can also forward notifications via email, making it a bridge between HTTP events and traditional notification channels. For agent integration, ntfy provides a clean REST API for both publishing and subscribing. Messages can include structured JSON payloads, making it suitable for automation pipelines where downstream consumers need to parse notification content programmatically. Self-Hosting and Deployment ntfy is distributed as a single static binary, a Docker image, and Debian/RPM packages. Self-hosting requires minimal resources — it runs comfortably on a Raspberry Pi. The server stores messages in a SQLite database with configurable retention, supports WebSocket connections for real-time subscriptions, and provides a built-in web UI for monitoring topics. Integration Points Common integrations include monitoring alerts from Prometheus or Grafana, CI/CD pipeline notifications from GitHub Actions or Jenkins, cron job status reports, home automation events, and any script that needs to notify a human. The simplicity of the HTTP API means any language or tool that can make HTTP requests can use ntfy as a notification backend.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ntfy-self-hosted-push-notification-server/)
