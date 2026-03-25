---
name: "CircleCI Orb Composer"
description: "Composes and validates CircleCI Orbs using the circleci/circleci-cli and circleci/orb-tools-orb SDK. Automates orb packaging, semantic versioning with conventional-changelog, and publishing to the CircleCI Orb Registry."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-composer-7/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Composer

Composes and validates CircleCI Orbs using the circleci/circleci-cli and circleci/orb-tools-orb SDK. Automates orb packaging, semantic versioning with conventional-changelog, and publishing to the CircleCI Orb Registry.

## Overview

The CircleCI Orb Composer skill streamlines the creation, validation, and publishing of CircleCI Orbs — reusable configuration packages for CircleCI pipelines. It uses the circleci/circleci-cli to validate orb source YAML and the circleci/orb-tools-orb to automate the full orb development lifecycle.

The skill handles orb structure scaffolding with proper src/ directory layouts for commands, jobs, executors, and examples. It integrates conventional-changelog for automatic semantic versioning based on commit messages, ensuring orb versions follow semver conventions.

Capabilities include generating parameterized commands with proper type validation, creating executor definitions for Docker/machine/macOS environments, building job templates with configurable steps, and producing comprehensive usage examples. The skill validates orbs against the CircleCI schema, runs integration tests using circleci local execute, and publishes to the CircleCI Orb Registry with proper namespace management. It also supports generating orb documentation using orb-tools/pack and orb-tools/review commands.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composer-7
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composer-7 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composer-7 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composer-7 -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-composer-7
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-composer-7/
