---
name: Cypress Component Testing Suite
description: Implements component and E2E tests using Cypress with cy.mount, cy.intercept,
  and cy.get selectors. Configures cypress.config.ts with component devServer, custom
  commands, and Mochawesome reporter integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cypress-component-testing-suite/
category:
- Browser Automation
framework:
- MCP
---
# Cypress Component Testing Suite

This skill sets up comprehensive testing suites using Cypress for both component and end-to-end testing. Component testing uses cy.mount() with framework-specific adapters for React, Vue, and Angular, configured through component.devServer in cypress.config.ts. E2E tests leverage cy.visit() for page navigation, cy.get() with data-cy attribute selectors for reliable element targeting, and cy.contains() for text-based lookups. Network stubbing uses cy.intercept() to mock API responses with fixture files loaded via cy.fixture(). The agent configures custom commands in cypress/support/commands.ts for reusable login flows, API seeding, and assertion helpers. Time travel debugging is enhanced through cy.screenshot() on failure and video recording configuration. The skill sets up Mochawesome reporter via cypress-mochawesome-reporter for HTML report generation with embedded screenshots. Environment-specific configurations use Cypress.env() with cypress.env.json files for different deployment targets. Retry logic uses retries configuration in cypress.config.ts with separate runMode and openMode settings. Includes GitHub Actions integration with cypress-io/github-action for CI pipeline execution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-suite/)
