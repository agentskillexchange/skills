---
title: "Buildkite Dynamic Pipeline Agent"
description: "The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests."
source: "https://buildkite.com/docs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Buildkite Dynamic Pipeline Agent

The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/)
