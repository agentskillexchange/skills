---
name: "Slack Bolt Event Subscription Debugger"
description: "Debugs Slack app event flows with the Bolt SDK, signature verification, `app.event()` handlers, and `ack()` timing. Useful for tracing why Events API deliveries, slash commands, or interactive callbacks are failing in real integration environments."
category: "Integrations & Connectors"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/slack-bolt-event-subscription-debugger/"
tool_ecosystem:
  tool: "slack"
  github_stars: 2899
  npm_weekly_downloads: 2433529
  github_repo: "slackapi/bolt-js"
  license: "MIT"
  maintained: true
---

# Slack Bolt Event Subscription Debugger

Debugs Slack app event flows with the Bolt SDK, signature verification, `app.event()` handlers, and `ack()` timing. Useful for tracing why Events API deliveries, slash commands, or interactive callbacks are failing in real integration environments.

## Overview

Slack Bolt Event Subscription Debugger is focused on one of the most frustrating parts of Slack app development: knowing whether an event actually arrived, was verified correctly, and was acknowledged within Slack’s deadline. The skill works with core Bolt concepts such as `app.event()`, `app.command()`, `ack()`, and signature verification based on the Slack signing secret. It is equally useful for classic Events API subscriptions, slash commands, and interactive payloads from buttons or modals.

The workflow helps isolate common failure modes, including slow acknowledgements, malformed request bodies, mismatched routes, and middleware that rewrites headers before Bolt sees them. That matters because many Slack integration bugs look like “nothing happened” when the real problem is a failed verification step or a handler that never reached `ack()` in time. This skill pushes those issues into the open.

Use it when building or maintaining Slack integrations that need dependable event handling, better diagnostic visibility, and a cleaner path from incoming callbacks to business logic.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-bolt-event-subscription-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-bolt-event-subscription-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-bolt-event-subscription-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-bolt-event-subscription-debugger -a codex
```

### OpenClaw

```bash
clawhub install slack-bolt-event-subscription-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-bolt-event-subscription-debugger/
