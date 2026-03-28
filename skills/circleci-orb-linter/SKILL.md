---
name: "CircleCI Orb Linter"
description: "Validates CircleCI configuration files and custom Orbs using the CircleCI CLI (circleci config validate) and Orb Development Kit. Checks for deprecated images, inefficient caching strategies, and security anti-patterns."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
tool_ecosystem:
  tool: circleci
  github_stars: 842
  github_repo: circleci/circleci-docs
  maintained: true
---

# CircleCI Orb Linter

Validates CircleCI configuration files and custom Orbs using the CircleCI CLI (circleci config validate) and Orb Development Kit. Checks for deprecated images, inefficient caching strategies, and security anti-patterns.

## Overview

The CircleCI Orb Linter agent validates CircleCI pipeline configurations and custom Orb definitions using the CircleCI CLI (circleci config validate, circleci orb validate). It performs deep structural analysis of .circleci/config.yml files to identify misconfigurations, deprecated Docker images, and suboptimal workflow definitions.

The agent checks caching strategies by analyzing save_cache and restore_cache key patterns, flagging overly broad or stale cache configurations that waste storage or slow builds. It validates resource class assignments against actual job requirements to optimize compute costs and identifies jobs that could benefit from parallelism or test splitting.

For Orb development, the agent validates Orb source YAML against the CircleCI Orb schema, checks command parameter types, and verifies executor compatibility. It detects security anti-patterns like hardcoded secrets, overly permissive context usage, and missing approval gates for production deployments. Supports config packing for Orb publishing and integration with the CircleCI Insights API for performance-based optimization suggestions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-linter -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-linter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-linter/
