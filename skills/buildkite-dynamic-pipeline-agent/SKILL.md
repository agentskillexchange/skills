---
title: Buildkite Dynamic Pipeline Agent
description: The Buildkite Dynamic Pipeline Agent skill programmatically generates
  and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL
  APIs. It creates dynamic pipeline steps based on repository analysis, targeting
  specific agent queues with tag-based routing for specialized workloads like GPU
  testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on
  configurations with exit status mapping for known flaky test patterns. It configures
  build artifact uploading and downloading between steps, sets up block steps with
  select fields for manual deployment approvals, and manages pipeline-level environment
  variables through the Buildkite Pipelines API. The agent supports group steps for
  visual organization, parallel step execution with concurrency gates, and matrix
  builds using the Buildkite matrix configuration syntax. It also integrates with
  Buildkite Test Analytics API to identify and quarantine consistently failing tests.
verification: security_reviewed
source: https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/
category:
- CI/CD Integrations
framework:
- Cursor
---

# Buildkite Dynamic Pipeline Agent

The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/)
