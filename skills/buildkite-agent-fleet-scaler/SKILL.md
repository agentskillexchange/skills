---
title: "Buildkite Agent Fleet Scaler"
description: "The Buildkite Agent Fleet Scaler skill provides intelligent auto-scaling for Buildkite CI agent infrastructure. It polls the Buildkite GraphQL API to monitor queue depths, job wait times, and agent utilization across multiple queues. Based on configurable thresholds and predictive models trained on historical queue data, it triggers scaling actions through AWS EC2 Auto Scaling Groups or Kubernetes Horizontal Pod Autoscalers. The skill handles spot instance interruption gracefully by draining agents before termination using the Buildkite Agent API. Supports mixed instance strategies combining on-demand baseline capacity with spot burst capacity. Implements queue-aware routing to direct jobs to appropriately sized agents based on resource requirements. Generates cost reports comparing actual spend against on-demand pricing. Integrates with Datadog for metric export and alerting on scaling events."
source: "https://buildkite.com/docs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
---

# Buildkite Agent Fleet Scaler

The Buildkite Agent Fleet Scaler skill provides intelligent auto-scaling for Buildkite CI agent infrastructure. It polls the Buildkite GraphQL API to monitor queue depths, job wait times, and agent utilization across multiple queues. Based on configurable thresholds and predictive models trained on historical queue data, it triggers scaling actions through AWS EC2 Auto Scaling Groups or Kubernetes Horizontal Pod Autoscalers. The skill handles spot instance interruption gracefully by draining agents before termination using the Buildkite Agent API. Supports mixed instance strategies combining on-demand baseline capacity with spot burst capacity. Implements queue-aware routing to direct jobs to appropriately sized agents based on resource requirements. Generates cost reports comparing actual spend against on-demand pricing. Integrates with Datadog for metric export and alerting on scaling events.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/)
