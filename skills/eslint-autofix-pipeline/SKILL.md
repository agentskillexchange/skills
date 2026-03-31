---
name: "ESLint Auto-Fix Pipeline"
description: "Runs ESLint with the –fix flag across JavaScript and TypeScript codebases, applying auto-fixable rules from eslint-config-airbnb and @typescript-eslint/recommended. Generates diff reports for manual review of remaining issues."
category: "Code Quality & Review"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-autofix-pipeline/"
---
# ESLint Auto-Fix Pipeline

Runs ESLint with the –fix flag across JavaScript and TypeScript codebases, applying auto-fixable rules from eslint-config-airbnb and @typescript-eslint/recommended. Generates diff reports for manual review of remaining issues.

## Overview

The ESLint Auto-Fix Pipeline agent automates code linting and correction for JavaScript and TypeScript projects. It executes ESLint programmatically using the ESLint Node.js API (new ESLint({ fix: true })) with configurable rule sets including eslint-config-airbnb, @typescript-eslint/recommended, and eslint-plugin-react.

The agent processes files in batches, applying auto-fixable corrections for spacing, semicolons, import ordering, unused variables, and other style violations. For issues that cannot be auto-fixed, it generates structured diff reports highlighting the exact lines and suggested remediation steps.

Supports integration with Prettier for formatting conflicts resolution via eslint-config-prettier and eslint-plugin-prettier. The pipeline can be configured to run as a pre-commit hook or as part of a CI workflow, with exit codes reflecting the severity of remaining issues. Handles monorepo configurations with cascading eslintrc files and workspace-level overrides.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-autofix-pipeline -a codex
```

### OpenClaw

```bash
clawhub install eslint-autofix-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-autofix-pipeline/)
