---
name: "Buildkite Dynamic Pipeline Agent"
description: "Creates Buildkite pipelines dynamically using the Buildkite REST API and pipeline upload commands. Manages agent targeting with queue tags and implements automatic retry strategies for flaky tests."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20332  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Buildkite Dynamic Pipeline Agent

Creates Buildkite pipelines dynamically using the Buildkite REST API and pipeline upload commands. Manages agent targeting with queue tags and implements automatic retry strategies for flaky tests.

## Overview

The Buildkite Dynamic Pipeline Agent skill programmatically generates and uploads Buildkite pipeline definitions using the Buildkite REST and GraphQL APIs. It creates dynamic pipeline steps based on repository analysis, targeting specific agent queues with tag-based routing for specialized workloads like GPU testing or ARM builds. The skill implements intelligent retry strategies using automatic_retry_on configurations with exit status mapping for known flaky test patterns. It configures build artifact uploading and downloading between steps, sets up block steps with select fields for manual deployment approvals, and manages pipeline-level environment variables through the Buildkite Pipelines API. The agent supports group steps for visual organization, parallel step execution with concurrency gates, and matrix builds using the Buildkite matrix configuration syntax. It also integrates with Buildkite Test Analytics API to identify and quarantine consistently failing tests.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-agent -a codex
```

### OpenClaw

```bash
clawhub install buildkite-dynamic-pipeline-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-agent/
