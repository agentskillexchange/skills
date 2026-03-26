---
name: "Cypress Component Testing Framework"
description: "Scaffolds Cypress component tests for React, Vue, and Angular apps using the Cypress CT mount API. Configures webpack/vite dev servers and generates snapshot-based visual assertions."
category: "Browser Automation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cypress-component-testing-framework-2/"
tool_ecosystem:
  tool: "cypress"
  github_stars: 49611
  npm_weekly_downloads: 7404178
  github_repo: "cypress-io/cypress"
  license: "MIT"
  maintained: true
---

# Cypress Component Testing Framework

Scaffolds Cypress component tests for React, Vue, and Angular apps using the Cypress CT mount API. Configures webpack/vite dev servers and generates snapshot-based visual assertions.

## Overview

The Cypress Component Testing Framework generates isolated component test suites using the Cypress Component Testing runner with framework-specific mount commands for React (cy.mount via @cypress/react), Vue (@cypress/vue), and Angular (@cypress/angular). It configures the component dev server using either webpack via @cypress/webpack-dev-server or Vite via @cypress/vite-dev-server, automatically detecting the project bundler from package.json. Test generation creates mount calls with proper prop injection, slot content for Vue components, and Angular module imports with dependency injection mocking. The skill sets up intercept patterns using cy.intercept() for API mocking, custom cy.commands for shared authentication flows, and fixture data management. Visual regression is handled through cypress-image-snapshot plugin with configurable diff thresholds and baseline management. Each test includes proper cleanup, state isolation via beforeEach hooks, and accessibility assertions using cypress-axe for WCAG 2.1 AA compliance checking. The generated cypress.config.ts includes optimal viewport settings, retry configuration, and parallel recording setup for Cypress Cloud dashboard integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-framework-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-framework-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-framework-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-component-testing-framework-2 -a codex
```

### OpenClaw

```bash
clawhub install cypress-component-testing-framework-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cypress-component-testing-framework-2/
