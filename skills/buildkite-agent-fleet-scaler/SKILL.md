---
name: "Buildkite Agent Fleet Scaler"
description: "Auto-scales Buildkite agent fleets based on queue depth and job wait times using the Buildkite GraphQL API. Manages AWS EC2 spot instances and Kubernetes HPA configurations for elastic CI capacity."
category: "CI/CD Integrations"
framework: "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# Buildkite Agent Fleet Scaler

Auto-scales Buildkite agent fleets based on queue depth and job wait times using the Buildkite GraphQL API. Manages AWS EC2 spot instances and Kubernetes HPA configurations for elastic CI capacity.

## Overview

The Buildkite Agent Fleet Scaler skill provides intelligent auto-scaling for Buildkite CI agent infrastructure. It polls the Buildkite GraphQL API to monitor queue depths, job wait times, and agent utilization across multiple queues. Based on configurable thresholds and predictive models trained on historical queue data, it triggers scaling actions through AWS EC2 Auto Scaling Groups or Kubernetes Horizontal Pod Autoscalers. The skill handles spot instance interruption gracefully by draining agents before termination using the Buildkite Agent API. Supports mixed instance strategies combining on-demand baseline capacity with spot burst capacity. Implements queue-aware routing to direct jobs to appropriately sized agents based on resource requirements. Generates cost reports comparing actual spend against on-demand pricing. Integrates with Datadog for metric export and alerting on scaling events.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-fleet-scaler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-fleet-scaler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-fleet-scaler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buildkite-agent-fleet-scaler -a codex
```

### OpenClaw

```bash
clawhub install buildkite-agent-fleet-scaler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/
