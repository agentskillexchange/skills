---
name: "CircleCI Orb Configuration Manager"
description: "Manages CircleCI pipeline configurations using orbs like circleci/node, circleci/docker, and circleci/aws-s3. Handles workflow orchestration, parallelism, and resource class selection via .circleci/config.yml."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-configuration-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Configuration Manager

Manages CircleCI pipeline configurations using orbs like circleci/node, circleci/docker, and circleci/aws-s3. Handles workflow orchestration, parallelism, and resource class selection via .circleci/config.yml.

## Overview

The CircleCI Orb Configuration Manager skill generates and maintains .circleci/config.yml files using the CircleCI 2.1 configuration specification. It integrates certified orbs including circleci/node@5, circleci/docker@2, circleci/aws-s3@4, circleci/slack@4, and circleci/browser-tools@1 to streamline pipeline setup.

The skill configures job executors (Docker, machine, macOS, Windows), sets resource classes (small, medium, large, xlarge, 2xlarge) for cost optimization, and manages workspace persistence using persist_to_workspace and attach_workspace steps. It supports test splitting with circleci tests split –split-by=timings for parallel execution across containers.

Advanced features include pipeline parameter definition using the parameters key, conditional workflow execution with when/unless clauses, scheduled workflow triggers via cron expressions, and dynamic configuration using the continuation orb (circleci/continuation@1). The manager also handles SSH key management for deployment, Docker layer caching (DLC) configuration, and custom orb development using the circleci CLI (circleci orb init, circleci orb publish).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configuration-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configuration-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configuration-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configuration-manager -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-configuration-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-configuration-manager/
