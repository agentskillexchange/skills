---
name: "Sentry Issue Spike Detection Agent"
description: "Analyzes Sentry project event streams via the Sentry Issues API to detect sudden spikes in error frequency. Computes rolling baselines and triggers alerts through configurable notification channels."
category: "40"
framework: "23"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sentry-issue-spike-detection-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sentry"  # from ase_tool_match
  github_stars: 43437  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16379655  # from ase_npm_downloads
  github_repo: "getsentry/sentry"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Sentry Issue Spike Detection Agent

Analyzes Sentry project event streams via the Sentry Issues API to detect sudden spikes in error frequency. Computes rolling baselines and triggers alerts through configurable notification channels.

## Overview

The Sentry Issue Spike Detection Agent connects to your Sentry organization using the Sentry Web API and continuously monitors issue event frequency across projects. It fetches recent events via the /api/0/organizations/{org}/issues/ endpoint with statsperiod and query parameters, computing rolling averages and standard deviations over configurable windows. When event frequency exceeds the baseline by a configurable multiplier, the agent classifies it as a spike and generates a structured alert containing the issue title, stack trace summary, affected users count, and first/last seen timestamps. Alerts can be routed to Slack via the Slack Web API, email via SMTP, or custom webhooks. The agent also groups related spikes using Sentry’s issue grouping metadata and suppresses duplicate notifications within a cooldown period. It supports Sentry DSN-based project filtering and can query the Sentry Releases API to correlate spikes with recent deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sentry-issue-spike-detection-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sentry-issue-spike-detection-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sentry-issue-spike-detection-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sentry-issue-spike-detection-agent -a codex
```

### OpenClaw

```bash
clawhub install sentry-issue-spike-detection-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sentry-issue-spike-detection-agent/
