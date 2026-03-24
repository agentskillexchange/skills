---
name: "Incident Postmortem Generator"
description: "Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/incident-postmortem-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Incident Postmortem Generator

Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format.

## Overview

Incident Postmortem Generator automates the creation of blameless postmortem documents by aggregating data from your incident response toolchain.

How It Works

The skill pulls incident timeline data from PagerDuty’s REST API, conversation history from Slack incident channels, and performance graphs from Grafana dashboard snapshots. It synthesizes this data into a structured postmortem following the Google SRE template.

Key Features

Automated timeline construction from PagerDuty incident logs, Slack messages, and deployment events

Impact analysis using Grafana queries to quantify error rates, latency percentiles, and affected users

Root cause categorization aligned with categories like code change, configuration, dependency, capacity

Action item extraction with owner assignment and priority ranking

Output

Generates documents in Confluence, Google Docs, or Markdown format. Tracks action item completion status. Supports recurring incident pattern detection across historical postmortems. Templates are customizable per team or service.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill incident-postmortem-generator -a codex
```

### OpenClaw

```bash
clawhub install incident-postmortem-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/incident-postmortem-generator/
