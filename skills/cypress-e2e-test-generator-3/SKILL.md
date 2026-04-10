---
title: "Cypress E2E Test Generator"
description: "Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation."
slug: "cypress-e2e-test-generator-3"
category:
  - "Browser Automation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/"
---

# Cypress E2E Test Generator

Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation.

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
clawhub install cypress-e2e-test-generator-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Automated end-to-end test generation agent for Cypress testing framework. Records user interaction flows and converts them into maintainable Cypress test specifications. Uses the Cypress Real Events plugin for accurate mouse and keyboard event simulation. Generates network request fixtures automatically using cy.intercept() to capture and replay API responses. Implements the Page Object Model pattern for generated tests with automatic selector optimization favoring data-testid attributes over fragile CSS selectors. Supports custom command generation for repeated interaction patterns. Integrates with Cypress Dashboard for test analytics, parallelization, and flaky test management. Includes visual testing via the cypress-image-snapshot plugin. Generates TypeScript test files with full type definitions for custom commands and fixtures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/)
