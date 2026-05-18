---
name: "Slack Bolt Event Subscription Debugger"
slug: "slack-bolt-event-subscription-debugger"
description: "Debugs Slack app event flows with the Bolt SDK, signature verification, `app.event()` handlers, and `ack()` timing. Useful for tracing why Events API deliveries, slash commands, or interactive callbacks are failing in real integration environments."
github_stars: 2898
verification: "listed"
source: "https://github.com/slackapi/bolt-js"
category: "Integrations & Connectors"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2898
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2474841
---

# Slack Bolt Event Subscription Debugger

Debugs Slack app event flows with the Bolt SDK, signature verification, `app.event()` handlers, and `ack()` timing. Useful for tracing why Events API deliveries, slash commands, or interactive callbacks are failing in real integration environments.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @slack/bolt

Requirements and caveats from upstream:
- [![Node.js CI](https://github.com/slackapi/bolt-js/actions/workflows/ci-build.yml/badge.svg)](https://github.com/slackapi/bolt-js/actions/workflows/ci-build.yml)
- The Slack **Request URL** for a Bolt app must have the path set to /slack/events.
- | payload | Contents of the incoming event. The payload structure depends on the listener. For example, for an Events API event, payload will be the [event type structure](https://docs.slack.dev/apis/events-api#event-...

Basic usage or getting-started notes:
- A JavaScript framework to build Slack apps in a flash with the latest platform features. Read the [getting started guide](https://docs.slack.dev/tools/bolt-js/getting-started) to set-up and run your first Bolt app.
- bash
- ## Initialization

- Source: https://github.com/slackapi/bolt-js
- Extracted from upstream docs: https://raw.githubusercontent.com/slackapi/bolt-js/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-bolt-event-subscription-debugger/)
