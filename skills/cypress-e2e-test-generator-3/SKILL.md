---
name: "Cypress E2E Test Generator"
description: "Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation."
category: "Browser Automation"
framework: "Claude Agents"
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
tool_ecosystem:
  tool: cypress
  github_repo: cypress-io/cypress
  github_stars: 49610
  license: MIT
  maintained: true
---
# Cypress E2E Test Generator

Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation.

## Overview

Automated end-to-end test generation agent for Cypress testing framework. Records user interaction flows and converts them into maintainable Cypress test specifications. Uses the Cypress Real Events plugin for accurate mouse and keyboard event simulation. Generates network request fixtures automatically using cy.intercept() to capture and replay API responses. Implements the Page Object Model pattern for generated tests with automatic selector optimization favoring data-testid attributes over fragile CSS selectors. Supports custom command generation for repeated interaction patterns. Integrates with Cypress Dashboard for test analytics, parallelization, and flaky test management. Includes visual testing via the cypress-image-snapshot plugin. Generates TypeScript test files with full type definitions for custom commands and fixtures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-test-generator-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-test-generator-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-test-generator-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-test-generator-3 -a codex
```

### OpenClaw

```bash
clawhub install cypress-e2e-test-generator-3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/)
