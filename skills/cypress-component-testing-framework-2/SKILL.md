---
title: Cypress Component Testing Framework
description: The Cypress Component Testing Framework generates isolated component
  test suites using the Cypress Component Testing runner with framework-specific mount
  commands for React (cy.mount via @cypress/react), Vue (@cypress/vue), and Angular
  (@cypress/angular). It configures the component dev server using either webpack
  via @cypress/webpack-dev-server or Vite via @cypress/vite-dev-server, automatically
  detecting the project bundler from package.json. Test generation creates mount calls
  with proper prop injection, slot content for Vue components, and Angular module
  imports with dependency injection mocking. The skill sets up intercept patterns
  using cy.intercept() for API mocking, custom cy.commands for shared authentication
  flows, and fixture data management. Visual regression is handled through cypress-image-snapshot
  plugin with configurable diff thresholds and baseline management. Each test includes
  proper cleanup, state isolation via beforeEach hooks, and accessibility assertions
  using cypress-axe for WCAG 2.1 AA compliance checking. The generated cypress.config.ts
  includes optimal viewport settings, retry configuration, and parallel recording
  setup for Cypress Cloud dashboard integration.
verification: security_reviewed
source: https://github.com/cypress-io/cypress
category:
- Browser Automation
framework:
- MCP
tool_ecosystem:
  github_repo: cypress-io/cypress
  github_stars: 49613
  npm_package: cypress
---

# Cypress Component Testing Framework

The Cypress Component Testing Framework generates isolated component test suites using the Cypress Component Testing runner with framework-specific mount commands for React (cy.mount via @cypress/react), Vue (@cypress/vue), and Angular (@cypress/angular). It configures the component dev server using either webpack via @cypress/webpack-dev-server or Vite via @cypress/vite-dev-server, automatically detecting the project bundler from package.json. Test generation creates mount calls with proper prop injection, slot content for Vue components, and Angular module imports with dependency injection mocking. The skill sets up intercept patterns using cy.intercept() for API mocking, custom cy.commands for shared authentication flows, and fixture data management. Visual regression is handled through cypress-image-snapshot plugin with configurable diff thresholds and baseline management. Each test includes proper cleanup, state isolation via beforeEach hooks, and accessibility assertions using cypress-axe for WCAG 2.1 AA compliance checking. The generated cypress.config.ts includes optimal viewport settings, retry configuration, and parallel recording setup for Cypress Cloud dashboard integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-framework-2/)
