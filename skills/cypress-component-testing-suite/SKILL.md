---
title: Cypress Component Testing Suite
description: This skill sets up comprehensive testing suites using Cypress for both
  component and end-to-end testing. Component testing uses cy.mount() with framework-specific
  adapters for React, Vue, and Angular, configured through component.devServer in
  cypress.config.ts. E2E tests leverage cy.visit() for page navigation, cy.get() with
  data-cy attribute selectors for reliable element targeting, and cy.contains() for
  text-based lookups. Network stubbing uses cy.intercept() to mock API responses with
  fixture files loaded via cy.fixture(). The agent configures custom commands in cypress/support/commands.ts
  for reusable login flows, API seeding, and assertion helpers. Time travel debugging
  is enhanced through cy.screenshot() on failure and video recording configuration.
  The skill sets up Mochawesome reporter via cypress-mochawesome-reporter for HTML
  report generation with embedded screenshots. Environment-specific configurations
  use Cypress.env() with cypress.env.json files for different deployment targets.
  Retry logic uses retries configuration in cypress.config.ts with separate runMode
  and openMode settings. Includes GitHub Actions integration with cypress-io/github-action
  for CI pipeline execution.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-suite/)
