---
name: "CircleCI Orb Pipeline Agent"
description: "Builds and manages CircleCI pipelines using config.yml v2.1, CircleCI API v2, and reusable Orbs. Supports dynamic config, test splitting, and resource class optimization."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Pipeline Agent

Builds and manages CircleCI pipelines using config.yml v2.1, CircleCI API v2, and reusable Orbs. Supports dynamic config, test splitting, and resource class optimization.

## Overview

The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation.

The agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection.

Test splitting is optimized via circleci tests split –split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API.

Dynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-agent -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-pipeline-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/
