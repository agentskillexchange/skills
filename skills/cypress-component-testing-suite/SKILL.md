---
title: "Cypress Component Testing Suite"
description: "Implements component and E2E tests using Cypress with cy.mount, cy.intercept, and cy.get selectors. Configures cypress.config.ts with component devServer, custom commands, and Mochawesome reporter integration."
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress Component Testing Suite

This skill sets up comprehensive testing suites using Cypress for both component and end-to-end testing. Component testing uses cy.mount() with framework-specific adapters for React, Vue, and Angular, configured through component.devServer in cypress.config.ts. E2E tests leverage cy.visit() for page navigation, cy.get() with data-cy attribute selectors for reliable element targeting, and cy.contains() for text-based lookups. Network stubbing uses cy.intercept() to mock API responses with fixture files loaded via cy.fixture(). The agent configures custom commands in cypress/support/commands.ts for reusable login flows, API seeding, and assertion helpers. Time travel debugging is enhanced through cy.screenshot() on failure and video recording configuration. The skill sets up Mochawesome reporter via cypress-mochawesome-reporter for HTML report generation with embedded screenshots. Environment-specific configurations use Cypress.env() with cypress.env.json files for different deployment targets. Retry logic uses retries configuration in cypress.config.ts with separate runMode and openMode settings. Includes GitHub Actions integration with cypress-io/github-action for CI pipeline execution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cypress-component-testing-suite
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cypress-component-testing-suite` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-suite/)
