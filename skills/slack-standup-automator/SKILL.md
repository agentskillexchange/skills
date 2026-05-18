---
name: "Slack Standup Automator"
slug: "slack-standup-automator"
description: "Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage."
github_stars: 2900
verification: "listed"
source: "https://github.com/slackapi/bolt-js"
category: "Calendar, Email & Productivity"
framework: "Codex"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Standup Automator

Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-automator/)
