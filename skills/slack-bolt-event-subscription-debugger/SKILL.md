---
name: "Slack Bolt Event Subscription Debugger"
description: "Debugs Slack app event flows with the Bolt SDK, signature verification, `app.event()` handlers, and `ack()` timing. Useful for tracing why Events API deliveries, slash commands, or interactive callbacks are failing in real integration environments."
verification: security_reviewed
source: "https://github.com/slackapi/bolt-js"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2898
  ase_npm_package: "@slack/bolt"
  npm_weekly_downloads: 1953184
---

# Slack Bolt Event Subscription Debugger

Slack Bolt Event Subscription Debugger is focused on one of the most frustrating parts of Slack app development: knowing whether an event actually arrived, was verified correctly, and was acknowledged within Slack’s deadline. The skill works with core Bolt concepts such as app.event(), app.command(), ack(), and signature verification based on the Slack signing secret. It is equally useful for classic Events API subscriptions, slash commands, and interactive payloads from buttons or modals.
The workflow helps isolate common failure modes, including slow acknowledgements, malformed request bodies, mismatched routes, and middleware that rewrites headers before Bolt sees them. That matters because many Slack integration bugs look like “nothing happened” when the real problem is a failed verification step or a handler that never reached ack() in time. This skill pushes those issues into the open.
Use it when building or maintaining Slack integrations that need dependable event handling, better diagnostic visibility, and a cleaner path from incoming callbacks to business logic.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-bolt-event-subscription-debugger/)
