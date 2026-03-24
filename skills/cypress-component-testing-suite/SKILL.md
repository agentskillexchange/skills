---
name: "Cypress Component Testing Suite"
description: "Implements component and E2E tests using Cypress with cy.mount, cy.intercept, and cy.get selectors. Configures cypress.config.ts with component devServer, custom commands, and Mochawesome reporter integration."
category: "Browser Automation"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cypress-component-testing-suite/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cypress"  # from ase_tool_match
  github_stars: 49612  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 7404178  # from ase_npm_downloads
  github_repo: "cypress-io/cypress"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cypress Component Testing Suite

Implements component and E2E tests using Cypress with cy.mount, cy.intercept, and cy.get selectors. Configures cypress.config.ts with component devServer, custom commands, and Mochawesome reporter integration.

## Overview

This skill sets up comprehensive testing suites using Cypress for both component and end-to-end testing. Component testing uses cy.mount() with framework-specific adapters for React, Vue, and Angular, configured through component.devServer in cypress.config.ts. E2E tests leverage cy.visit() for page navigation, cy.get() with data-cy attribute selectors for reliable element targeting, and cy.contains() for text-based lookups. Network stubbing uses cy.intercept() to mock API responses with fixture files loaded via cy.fixture(). The agent configures custom commands in cypress/support/commands.ts for reusable login flows, API seeding, and assertion helpers. Time travel debugging is enhanced through cy.screenshot() on failure and video recording configuration. The skill sets up Mochawesome reporter via cypress-mochawesome-reporter for HTML report generation with embedded screenshots. Environment-specific configurations use Cypress.env() with cypress.env.json files for different deployment targets. Retry logic uses retries configuration in cypress.config.ts with separate runMode and openMode settings. Includes GitHub Actions integration with cypress-io/github-action for CI pipeline execution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-suite -a codex
```

### OpenClaw

```bash
clawhub install cypress-component-testing-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cypress-component-testing-suite/
