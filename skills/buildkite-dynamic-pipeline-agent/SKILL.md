---
title: "Buildkite Dynamic Pipeline Agent"
description: "Creates Buildkite pipelines dynamically using the Buildkite REST API and pipeline upload commands. Manages agent targeting with queue tags and implements automatic retry strategies for flaky tests."
verification: security_reviewed
source: "https://buildkite.com/docs"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Buildkite Dynamic Pipeline Agent

The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/buildkite-dynamic-pipeline-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/buildkite-dynamic-pipeline-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/)
