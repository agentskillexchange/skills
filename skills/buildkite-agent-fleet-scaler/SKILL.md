---
title: "Buildkite Agent Fleet Scaler"
description: "Auto-scales Buildkite agent fleets based on queue depth and job wait times using the Buildkite GraphQL API. Manages AWS EC2 spot instances and Kubernetes HPA configurations for elastic CI capacity."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
---

# Buildkite Agent Fleet Scaler

The Buildkite Agent Fleet Scaler skill provides intelligent auto-scaling for Buildkite CI agent infrastructure. It polls the Buildkite GraphQL API to monitor queue depths, job wait times, and agent utilization across multiple queues. Based on configurable thresholds and predictive models trained on historical queue data, it triggers scaling actions through AWS EC2 Auto Scaling Groups or Kubernetes Horizontal Pod Autoscalers. The skill handles spot instance interruption gracefully by draining agents before termination using the Buildkite Agent API. Supports mixed instance strategies combining on-demand baseline capacity with spot burst capacity. Implements queue-aware routing to direct jobs to appropriately sized agents based on resource requirements. Generates cost reports comparing actual spend against on-demand pricing. Integrates with Datadog for metric export and alerting on scaling events.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-agent-fleet-scaler/)
