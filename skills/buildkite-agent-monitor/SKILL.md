---
title: "Buildkite Agent Monitor"
description: "The Buildkite Agent Monitor skill provides real-time visibility into your Buildkite CI infrastructure by querying the Buildkite REST API v3 and GraphQL API endpoints. It tracks agent pool health including connectivity status, queue depth trends, and job wait time percentiles.\nThe skill polls the /v2/organizations/{org}/agents endpoint to detect agents that have gone offline or become unresponsive, comparing last-seen timestamps against configurable thresholds. Queue depth monitoring queries the GraphQL pipeline.jobs connection to compute real-time backlog sizes per queue name, triggering alerts when depth exceeds configured limits.\nJob wait time analysis uses the Buildkite Builds API to compute p50, p95, and p99 wait times over sliding windows. When any metric crosses threshold, the skill formats detailed alert messages and dispatches them via the Slack Web API chat.postMessage method, including direct links to the Buildkite dashboard. Historical metrics are stored locally for trend analysis, enabling the agent to identify recurring bottlenecks in specific queues or time windows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buildkite-agent-monitor/"
framework:
  - "Gemini"
---

# Buildkite Agent Monitor

The Buildkite Agent Monitor skill provides real-time visibility into your Buildkite CI infrastructure by querying the Buildkite REST API v3 and GraphQL API endpoints. It tracks agent pool health including connectivity status, queue depth trends, and job wait time percentiles.
The skill polls the /v2/organizations/{org}/agents endpoint to detect agents that have gone offline or become unresponsive, comparing last-seen timestamps against configurable thresholds. Queue depth monitoring queries the GraphQL pipeline.jobs connection to compute real-time backlog sizes per queue name, triggering alerts when depth exceeds configured limits.
Job wait time analysis uses the Buildkite Builds API to compute p50, p95, and p99 wait times over sliding windows. When any metric crosses threshold, the skill formats detailed alert messages and dispatches them via the Slack Web API chat.postMessage method, including direct links to the Buildkite dashboard. Historical metrics are stored locally for trend analysis, enabling the agent to identify recurring bottlenecks in specific queues or time windows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/buildkite-agent-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/buildkite-agent-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-agent-monitor/)
