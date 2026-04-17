---
title: "Cypress E2E Test Generator"
description: "Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation."
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
  license: "MIT"
---

# Cypress E2E Test Generator

Automated end-to-end test generation agent for Cypress testing framework. Records user interaction flows and converts them into maintainable Cypress test specifications. Uses the Cypress Real Events plugin for accurate mouse and keyboard event simulation. Generates network request fixtures automatically using cy.intercept() to capture and replay API responses. Implements the Page Object Model pattern for generated tests with automatic selector optimization favoring data-testid attributes over fragile CSS selectors. Supports custom command generation for repeated interaction patterns. Integrates with Cypress Dashboard for test analytics, parallelization, and flaky test management. Includes visual testing via the cypress-image-snapshot plugin. Generates TypeScript test files with full type definitions for custom commands and fixtures.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cypress-e2e-test-generator-3
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cypress-e2e-test-generator-3` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/)
