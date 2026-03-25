---
name: "Slack Status API PTO Sync Assistant"
description: "Syncs away-state updates through Slack users.profile APIs, status fields, and directory lookups so agents can keep status text aligned with calendar-based time off. Useful for teams that want cleaner presence signals without manually editing every Slack profile."
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/slack-status-api-pto-sync-assistant/"
tool_ecosystem:
  tool: "slack"
  github_stars: 2899
  npm_weekly_downloads: 2433529
  github_repo: "slackapi/bolt-js"
  license: "MIT"
  maintained: true
---

# Slack Status API PTO Sync Assistant

Syncs away-state updates through Slack users.profile APIs, status fields, and directory lookups so agents can keep status text aligned with calendar-based time off. Useful for teams that want cleaner presence signals without manually editing every Slack profile.

## Overview

Slack Status API PTO Sync Assistant is for organizations that rely on Slack presence as a lightweight operating signal and want agents to keep it accurate during vacations, holidays, and planned absences. It uses Slack profile and users endpoints, including status text and expiration fields, to update presence information in a way that matches team availability. That is especially useful when calendar systems already know who is out but Slack status remains stale and teammates end up pinging the wrong people.

The workflow can compare current status values against planned absences, suggest a status update, and standardize phrasing across a team or department. It also helps avoid inconsistent or forgotten manual edits that make PTO harder to respect. Because it works with Slack’s own profile model rather than an external overlay, the status remains visible where people already look first.

Use this skill when you want cleaner away-state hygiene, more reliable availability signals, and a simple bridge between time-off data and Slack presence.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-status-api-pto-sync-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-status-api-pto-sync-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-status-api-pto-sync-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-status-api-pto-sync-assistant -a codex
```

### OpenClaw

```bash
clawhub install slack-status-api-pto-sync-assistant
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-status-api-pto-sync-assistant/
