---
title: "CircleCI Workflow Builder"
description: "Generates CircleCI config.yml workflows using the CircleCI Orbs SDK and Workflows API. Supports parallelism tuning with the CircleCI Test Splitting API and resource class optimization for Docker and machine executors."
slug: "circleci-workflow-builder"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-workflow-builder/"
listed: true
---

# CircleCI Workflow Builder

Generates CircleCI config.yml workflows using the CircleCI Orbs SDK and Workflows API. Supports parallelism tuning with the CircleCI Test Splitting API and resource class optimization for Docker and machine executors.

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
clawhub install circleci-workflow-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Workflow Builder skill automates the creation and optimization of CircleCI configuration files. It uses the CircleCI Orbs SDK to compose reusable configuration packages for common build patterns including Node.js, Python, Go, and Rust projects. The skill leverages the CircleCI Workflows API to design complex workflow graphs with fan-out/fan-in patterns, conditional execution using pipeline parameters, and scheduled triggers via cron expressions. Test splitting is optimized through the CircleCI Test Splitting API, distributing test suites across parallel containers based on timing data from previous runs. The skill configures appropriate resource classes for each job, balancing cost against build speed. It supports Docker layer caching, workspace persistence between jobs, and matrix job generation for cross-platform testing. Advanced features include dynamic configuration using setup workflows, custom orb development, and integration with CircleCI Insights API for build performance analytics.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-builder/)
