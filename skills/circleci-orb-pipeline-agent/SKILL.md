---
title: "CircleCI Orb Pipeline Agent"
description: "Builds and manages CircleCI pipelines using config.yml v2.1, CircleCI API v2, and reusable Orbs. Supports dynamic config, test splitting, and resource class optimization."
slug: "circleci-orb-pipeline-agent"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/"
listed: true
---

# CircleCI Orb Pipeline Agent

Builds and manages CircleCI pipelines using config.yml v2.1, CircleCI API v2, and reusable Orbs. Supports dynamic config, test splitting, and resource class optimization.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install circleci-orb-pipeline-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation.
The agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection.
Test splitting is optimized via circleci tests split –split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API.
Dynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/)
