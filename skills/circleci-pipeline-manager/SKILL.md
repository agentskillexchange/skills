---
name: "CircleCI Pipeline Manager"
description: "Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-pipeline-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Pipeline Manager

Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows.

## Overview

The CircleCI Pipeline Manager skill handles end-to-end CI/CD pipeline configuration and management through the CircleCI v2 API and .circleci/config.yml authoring. It creates pipeline configurations using CircleCI concepts including executors (docker, machine, macos), orbs (circleci/node@5, circleci/aws-cli@4, circleci/docker@2), commands, and jobs with proper workflow orchestration using requires and filters. The skill triggers pipelines via POST /api/v2/project/{project-slug}/pipeline with pipeline parameters, monitors workflow status through GET /api/v2/workflow/{id}, and retrieves job artifacts. It supports advanced features including dynamic configuration with setup: true workflows and the continuation orb, workspace and cache management with persist_to_workspace and save_cache/restore_cache steps, and parallelism with circleci tests split. The manager handles context management for shared secrets, scheduled pipeline triggers via the API, and config validation using the circleci config validate command.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-pipeline-manager -a codex
```

### OpenClaw

```bash
clawhub install circleci-pipeline-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-pipeline-manager/
