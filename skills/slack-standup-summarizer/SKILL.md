---
name: "Slack Standup Summarizer"
description: "Collects daily standup updates from Slack channels using the Web API and generates team summaries with blockers highlighted. Posts formatted digests via Incoming Webhooks."
category: "Calendar, Email & Productivity"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/slack-standup-summarizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Slack Standup Summarizer

Collects daily standup updates from Slack channels using the Web API and generates team summaries with blockers highlighted. Posts formatted digests via Incoming Webhooks.

## Overview

The Slack Standup Summarizer skill monitors designated Slack channels for daily standup messages using the conversations.history Web API endpoint. It identifies standup entries by timestamp windows, thread patterns, or bot-prompted responses and extracts structured data from free-form updates.

The summarizer parses standup messages to identify three components: completed work, planned work, and blockers. Natural language processing detects blocker keywords and escalation signals even when not explicitly formatted. Cross-referencing with Jira or Linear ticket numbers provides automatic status linking.

Digest generation produces formatted Slack Block Kit messages with sections for each team member, highlighted blockers with suggested owners, and sprint progress indicators. Digests post to configurable channels via Incoming Webhooks with optional threading under a daily parent message. Historical data aggregation tracks individual velocity trends, recurring blockers, and team completion rates over configurable time windows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-standup-summarizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-standup-summarizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-standup-summarizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-standup-summarizer -a codex
```

### OpenClaw

```bash
clawhub install slack-standup-summarizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-standup-summarizer/
