---
name: "CircleCI Workflow Builder"
description: "Generates CircleCI config.yml workflows using the CircleCI Orbs SDK and Workflows API. Supports parallelism tuning with the CircleCI Test Splitting API and resource class optimization for Docker and machine executors."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-workflow-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Workflow Builder

Generates CircleCI config.yml workflows using the CircleCI Orbs SDK and Workflows API. Supports parallelism tuning with the CircleCI Test Splitting API and resource class optimization for Docker and machine executors.

## Overview

The CircleCI Workflow Builder skill automates the creation and optimization of CircleCI configuration files. It uses the CircleCI Orbs SDK to compose reusable configuration packages for common build patterns including Node.js, Python, Go, and Rust projects. The skill leverages the CircleCI Workflows API to design complex workflow graphs with fan-out/fan-in patterns, conditional execution using pipeline parameters, and scheduled triggers via cron expressions. Test splitting is optimized through the CircleCI Test Splitting API, distributing test suites across parallel containers based on timing data from previous runs. The skill configures appropriate resource classes for each job, balancing cost against build speed. It supports Docker layer caching, workspace persistence between jobs, and matrix job generation for cross-platform testing. Advanced features include dynamic configuration using setup workflows, custom orb development, and integration with CircleCI Insights API for build performance analytics.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-builder -a codex
```

### OpenClaw

```bash
clawhub install circleci-workflow-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-workflow-builder/
