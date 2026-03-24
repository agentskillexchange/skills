---
name: "Slack Workflow Automation Builder"
description: "Creates Slack Workflow Builder automations using the Slack Web API and Block Kit. Builds approval flows, standup collectors, and incident response channels with interactive message components."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/slack-workflow-automation-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Slack Workflow Automation Builder

Creates Slack Workflow Builder automations using the Slack Web API and Block Kit. Builds approval flows, standup collectors, and incident response channels with interactive message components.

## Overview

The Slack Workflow Automation Builder programmatically creates and deploys Slack workflows using the Slack Web API and Bolt SDK framework. It constructs interactive workflows using Block Kit components—modal dialogs with input fields, multi-select menus, date pickers, and overflow menus for complex data collection. The skill builds approval workflows that route requests through configurable chains using Slack message actions and button callbacks, tracking approval state in a Redis-backed store. For standup automation, it deploys scheduled messages via chat.scheduleMessage that collect team updates through threaded responses, then aggregates and formats summaries into designated channels. Incident response workflows automatically create dedicated channels with conversations.create, invite on-call responders using usergroups.users.list integration with PagerDuty, pin runbook links, and set channel topics with incident metadata. The skill manages OAuth scopes and bot token permissions, handles rate limiting with the Slack retry headers (Retry-After), and implements event subscription verification for the Events API challenge handshake. Interactive component payloads are processed through the Bolt middleware chain with proper acknowledgment within the 3-second Slack timeout requirement.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-automation-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-automation-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-automation-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-automation-builder -a codex
```

### OpenClaw

```bash
clawhub install slack-workflow-automation-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-workflow-automation-builder/
