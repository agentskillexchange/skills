---
name: "Buildkite Agent Monitor"
description: "Monitors Buildkite agent pools via the Buildkite REST API v3 and GraphQL API. Tracks agent connectivity, queue depth, job wait times, and dispatches Slack alerts for stalled or disconnected agents."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/buildkite-agent-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20332  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Buildkite Agent Monitor

Monitors Buildkite agent pools via the Buildkite REST API v3 and GraphQL API. Tracks agent connectivity, queue depth, job wait times, and dispatches Slack alerts for stalled or disconnected agents.

## Overview

The Buildkite Agent Monitor skill provides real-time visibility into your Buildkite CI infrastructure by querying the Buildkite REST API v3 and GraphQL API endpoints. It tracks agent pool health including connectivity status, queue depth trends, and job wait time percentiles.

The skill polls the /v2/organizations/{org}/agents endpoint to detect agents that have gone offline or become unresponsive, comparing last-seen timestamps against configurable thresholds. Queue depth monitoring queries the GraphQL pipeline.jobs connection to compute real-time backlog sizes per queue name, triggering alerts when depth exceeds configured limits.

Job wait time analysis uses the Buildkite Builds API to compute p50, p95, and p99 wait times over sliding windows. When any metric crosses threshold, the skill formats detailed alert messages and dispatches them via the Slack Web API chat.postMessage method, including direct links to the Buildkite dashboard. Historical metrics are stored locally for trend analysis, enabling the agent to identify recurring bottlenecks in specific queues or time windows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-monitor -a codex
```

### OpenClaw

```bash
clawhub install buildkite-agent-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/buildkite-agent-monitor/
