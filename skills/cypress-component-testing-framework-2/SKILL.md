---
title: "Cypress Component Testing Framework"
description: "Scaffolds Cypress component tests for React, Vue, and Angular apps using the Cypress CT mount API. Configures webpack/vite dev servers and generates snapshot-based visual assertions."
slug: "cypress-component-testing-framework-2"
category:
  - "Browser Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/cypress-io/cypress"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49609
  npm_package: "cypress"
  npm_weekly_downloads: 6456036
listed: true
---

# Cypress Component Testing Framework

Scaffolds Cypress component tests for React, Vue, and Angular apps using the Cypress CT mount API. Configures webpack/vite dev servers and generates snapshot-based visual assertions.

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
clawhub install cypress-component-testing-framework-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cypress Component Testing Framework generates isolated component test suites using the Cypress Component Testing runner with framework-specific mount commands for React (cy.mount via @cypress/react), Vue (@cypress/vue), and Angular (@cypress/angular). It configures the component dev server using either webpack via @cypress/webpack-dev-server or Vite via @cypress/vite-dev-server, automatically detecting the project bundler from package.json. Test generation creates mount calls with proper prop injection, slot content for Vue components, and Angular module imports with dependency injection mocking. The skill sets up intercept patterns using cy.intercept() for API mocking, custom cy.commands for shared authentication flows, and fixture data management. Visual regression is handled through cypress-image-snapshot plugin with configurable diff thresholds and baseline management. Each test includes proper cleanup, state isolation via beforeEach hooks, and accessibility assertions using cypress-axe for WCAG 2.1 AA compliance checking. The generated cypress.config.ts includes optimal viewport settings, retry configuration, and parallel recording setup for Cypress Cloud dashboard integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-framework-2/)
