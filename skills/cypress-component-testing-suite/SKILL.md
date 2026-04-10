---
title: "Cypress Component Testing Suite"
description: "Implements component and E2E tests using Cypress with cy.mount, cy.intercept, and cy.get selectors. Configures cypress.config.ts with component devServer, custom commands, and Mochawesome reporter integration."
slug: "cypress-component-testing-suite"
category:
  - "Browser Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cypress-component-testing-suite/"
---

# Cypress Component Testing Suite

Implements component and E2E tests using Cypress with cy.mount, cy.intercept, and cy.get selectors. Configures cypress.config.ts with component devServer, custom commands, and Mochawesome reporter integration.

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
clawhub install cypress-component-testing-suite
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill sets up comprehensive testing suites using Cypress for both component and end-to-end testing. Component testing uses cy.mount() with framework-specific adapters for React, Vue, and Angular, configured through component.devServer in cypress.config.ts. E2E tests leverage cy.visit() for page navigation, cy.get() with data-cy attribute selectors for reliable element targeting, and cy.contains() for text-based lookups. Network stubbing uses cy.intercept() to mock API responses with fixture files loaded via cy.fixture(). The agent configures custom commands in cypress/support/commands.ts for reusable login flows, API seeding, and assertion helpers. Time travel debugging is enhanced through cy.screenshot() on failure and video recording configuration. The skill sets up Mochawesome reporter via cypress-mochawesome-reporter for HTML report generation with embedded screenshots. Environment-specific configurations use Cypress.env() with cypress.env.json files for different deployment targets. Retry logic uses retries configuration in cypress.config.ts with separate runMode and openMode settings. Includes GitHub Actions integration with cypress-io/github-action for CI pipeline execution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-suite/)
