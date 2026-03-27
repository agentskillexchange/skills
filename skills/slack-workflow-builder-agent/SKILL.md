---
name: "Slack Workflow Builder Agent"
description: "Creates and manages Slack workflows using @slack/bolt and @slack/web-api. Builds interactive modals with Block Kit, handles slash commands, and orchestrates multi-step approval flows via Slack Events API."
category: "Calendar, Email & Productivity"
framework: "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-workflow-builder-agent/"
tool_ecosystem:
  tool: slack
  github_stars: 2899
  npm_weekly_downloads: 2433529
  github_repo: slackapi/bolt-js
  license: MIT
  maintained: true
---

# Slack Workflow Builder Agent

Creates and manages Slack workflows using @slack/bolt and @slack/web-api. Builds interactive modals with Block Kit, handles slash commands, and orchestrates multi-step approval flows via Slack Events API.

## Overview

The Slack Workflow Builder Agent automates complex team workflows using @slack/bolt for event handling and @slack/web-api for programmatic Slack interaction. It creates rich interactive experiences using Block Kit components including modals, message attachments, and action buttons.

The agent handles slash command registration and processing, building multi-step approval workflows where each step triggers the next based on user interaction. It manages channel creation, archival, and topic updates programmatically, and supports threaded conversation management for organized team discussions.

Advanced features include scheduled message delivery using chat.scheduleMessage, user group management via usergroups API methods, and file sharing automation through files.upload v2. The agent implements Slack Events API subscriptions for real-time message monitoring, reaction tracking, and channel membership changes. It also builds custom Home Tab experiences using the views.publish endpoint for personalized dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-builder-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-builder-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-builder-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-builder-agent -a codex
```

### OpenClaw

```bash
clawhub install slack-workflow-builder-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-workflow-builder-agent/
