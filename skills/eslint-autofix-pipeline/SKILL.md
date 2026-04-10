---
title: "ESLint Auto-Fix Pipeline"
description: "Runs ESLint with the –fix flag across JavaScript and TypeScript codebases, applying auto-fixable rules from eslint-config-airbnb and @typescript-eslint/recommended. Generates diff reports for manual review of remaining issues."
slug: "eslint-autofix-pipeline"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-autofix-pipeline/"
---

# ESLint Auto-Fix Pipeline

Runs ESLint with the –fix flag across JavaScript and TypeScript codebases, applying auto-fixable rules from eslint-config-airbnb and @typescript-eslint/recommended. Generates diff reports for manual review of remaining issues.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install eslint-autofix-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ESLint Auto-Fix Pipeline agent automates code linting and correction for JavaScript and TypeScript projects. It executes ESLint programmatically using the ESLint Node.js API (new ESLint({ fix: true })) with configurable rule sets including eslint-config-airbnb, @typescript-eslint/recommended, and eslint-plugin-react.
The agent processes files in batches, applying auto-fixable corrections for spacing, semicolons, import ordering, unused variables, and other style violations. For issues that cannot be auto-fixed, it generates structured diff reports highlighting the exact lines and suggested remediation steps.
Supports integration with Prettier for formatting conflicts resolution via eslint-config-prettier and eslint-plugin-prettier. The pipeline can be configured to run as a pre-commit hook or as part of a CI workflow, with exit codes reflecting the severity of remaining issues. Handles monorepo configurations with cascading eslintrc files and workspace-level overrides.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-pipeline/)
