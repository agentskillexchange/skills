---
title: "Buildkite Agent Fleet Scaler"
description: "Auto-scales Buildkite agent fleets based on queue depth and job wait times using the Buildkite GraphQL API. Manages AWS EC2 spot instances and Kubernetes HPA configurations for elastic CI capacity."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
---

# Buildkite Agent Fleet Scaler

The Buildkite Agent Fleet Scaler skill provides intelligent auto-scaling for Buildkite CI agent infrastructure. It polls the Buildkite GraphQL API to monitor queue depths, job wait times, and agent utilization across multiple queues. Based on configurable thresholds and predictive models trained on historical queue data, it triggers scaling actions through AWS EC2 Auto Scaling Groups or Kubernetes Horizontal Pod Autoscalers. The skill handles spot instance interruption gracefully by draining agents before termination using the Buildkite Agent API. Supports mixed instance strategies combining on-demand baseline capacity with spot burst capacity. Implements queue-aware routing to direct jobs to appropriately sized agents based on resource requirements. Generates cost reports comparing actual spend against on-demand pricing. Integrates with Datadog for metric export and alerting on scaling events.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/buildkite-agent-fleet-scaler
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/buildkite-agent-fleet-scaler` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/)
