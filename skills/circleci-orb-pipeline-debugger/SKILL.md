---
name: "CircleCI Orb Pipeline Debugger"
description: "Diagnoses CircleCI orb configuration errors and pipeline failures using the CircleCI v2 API. Parses orb YAML schemas, detects version pinning issues, and suggests fixes for executor and job dependency problems."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Pipeline Debugger

Diagnoses CircleCI orb configuration errors and pipeline failures using the CircleCI v2 API. Parses orb YAML schemas, detects version pinning issues, and suggests fixes for executor and job dependency problems.

## Overview

The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-debugger -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-pipeline-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/
