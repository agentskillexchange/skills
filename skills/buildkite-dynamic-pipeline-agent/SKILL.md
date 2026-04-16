---
title: "Buildkite Dynamic Pipeline Agent"
description: "Creates Buildkite pipelines dynamically using the Buildkite REST API and pipeline upload commands. Manages agent targeting with queue tags and implements automatic retry strategies for flaky tests."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Buildkite Dynamic Pipeline Agent

The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/)
