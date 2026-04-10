---
title: "Buildkite Dynamic Pipeline Agent"
description: "Creates Buildkite pipelines dynamically using the Buildkite REST API and pipeline upload commands. Manages agent targeting with queue tags and implements automatic retry strategies for flaky tests."
slug: "buildkite-dynamic-pipeline-agent"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/"
---

# Buildkite Dynamic Pipeline Agent

Creates Buildkite pipelines dynamically using the Buildkite REST API and pipeline upload commands. Manages agent targeting with queue tags and implements automatic retry strategies for flaky tests.

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
clawhub install buildkite-dynamic-pipeline-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/)
