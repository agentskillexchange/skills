---
name: CircleCI Orb Pipeline Agent
description: Builds and manages CircleCI pipelines using config.yml v2.1, CircleCI
  API v2, and reusable Orbs. Supports dynamic config, test splitting, and resource
  class optimization.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---
# CircleCI Orb Pipeline Agent

The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation.
The agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection.
Test splitting is optimized via circleci tests split -split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API.
Dynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/)
