---
name: "Apprise Universal Push Notification Library and CLI"
description: "Apprise is a Python library and CLI that sends push notifications to over 100 services including Telegram, Discord, Slack, Amazon SNS, Gotify, email, and more through a single unified API. It supports attachments, images, and asynchronous delivery."
category: "Monitoring &amp; Alerts"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/caronc/apprise"
---
# Apprise Universal Push Notification Library and CLI

Apprise is a Python library and CLI that sends push notifications to over 100 services including Telegram, Discord, Slack, Amazon SNS, Gotify, email, and more through a single unified API. It supports attachments, images, and asynchronous delivery.

## Overview

What is Apprise?
Apprise is a Python-based notification library and command-line tool that provides a single interface for sending push notifications to virtually every major notification platform available today. With support for over 100 notification services, it eliminates the need to integrate with individual service APIs. Developers include one library and gain access to Telegram, Discord, Slack, Microsoft Teams, Amazon SNS, Gotify, Pushover, ntfy, email (SMTP), webhooks, and dozens more.

How It Works
Apprise uses a URL-based notification syntax where each service is represented by a URL scheme. For example, tgram://bottoken/ChatID sends to Telegram, discord://WebhookID/WebhookToken sends to Discord, and slack://TokenA/TokenB/TokenC sends to Slack. You can specify multiple notification URLs and Apprise delivers to all of them asynchronously for fast response times. The CLI accepts notification URLs directly or reads them from configuration files (YAML or text format).

Key Features
The library handles file attachments and images for services that support them, provides both synchronous and asynchronous APIs, supports persistent storage for notification state, and allows custom notification plugins via a hook system. Configuration files let you define named groups of notification targets, making it easy to route different types of alerts to different channels. The CLI ships with the Python package and provides immediate command-line access to all supported services.

Installation
Install via pip (pip install apprise) or from the GitHub repository. Docker images are also available. The library requires Python 3.8 or higher and has minimal dependencies.

Integration Points
Apprise integrates with CI/CD pipelines for build notifications, monitoring systems for alert routing, cron jobs for scheduled notifications, and any Python application needing multi-channel notification delivery. It works as a drop-in replacement for single-service notification scripts. The Apprise API companion project provides a lightweight REST API wrapper for non-Python environments. Agents can use it as a universal notification gateway, sending alerts to whatever channels users configure without needing service-specific integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apprise-universal-push-notification-library-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apprise-universal-push-notification-library-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apprise-universal-push-notification-library-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apprise-universal-push-notification-library-cli -a codex
```

### OpenClaw

```bash
clawhub install apprise-universal-push-notification-library-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apprise-universal-push-notification-library-cli/)
