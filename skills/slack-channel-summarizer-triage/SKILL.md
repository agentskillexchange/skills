---
name: "Slack Channel Summarizer & Triage Bot"
description: "Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel."
category: "Integrations & Connectors"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/slack-channel-summarizer-triage/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Slack Channel Summarizer & Triage Bot

Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel.

## Overview

Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-triage
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-triage -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-triage -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-triage -a codex
```

### OpenClaw

```bash
clawhub install slack-channel-summarizer-triage
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-channel-summarizer-triage/
