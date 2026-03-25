---
name: "GitHub Actions Pipeline Validator"
description: "Validates GitHub Actions workflow YAML files against the Actions schema, checks for deprecated action versions, and ensures proper secret handling. Integrates with actions/checkout, actions/setup-node, and dorny/paths-filter APIs."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-actions-pipeline-validator/"
---

# GitHub Actions Pipeline Validator

Validates GitHub Actions workflow YAML files against the Actions schema, checks for deprecated action versions, and ensures proper secret handling. Integrates with actions/checkout, actions/setup-node, and dorny/paths-filter APIs.

## Overview

The GitHub Actions Pipeline Validator skill provides comprehensive CI/CD pipeline validation for GitHub Actions workflows. It parses workflow YAML files against the official GitHub Actions schema specification, identifying syntax errors, deprecated action references, and misconfigured triggers. The validator checks all uses directives against the GitHub Marketplace API to verify action version compatibility and flag deprecated versions. It integrates with the dorny/paths-filter API to validate path-based trigger configurations and uses the actions/checkout and actions/setup-node SDKs to verify proper setup step ordering. Security scanning identifies exposed secrets, missing environment variable declarations, and overly permissive GITHUB_TOKEN permissions. The skill generates detailed reports with suggested fixes, including automatic version pinning recommendations and workflow optimization tips for reducing build times.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-pipeline-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-pipeline-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-pipeline-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-pipeline-validator -a codex
```

### OpenClaw

```bash
clawhub install github-actions-pipeline-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-pipeline-validator/
