---
title: "Cypress Component Testing Framework"
description: "Scaffolds Cypress component tests for React, Vue, and Angular apps using the Cypress CT mount API. Configures webpack/vite dev servers and generates snapshot-based visual assertions."
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49609
  npm_package: "cypress"
  npm_weekly_downloads: 6921926
---

# Cypress Component Testing Framework

The Cypress Component Testing Framework generates isolated component test suites using the Cypress Component Testing runner with framework-specific mount commands for React (cy.mount via @cypress/react), Vue (@cypress/vue), and Angular (@cypress/angular). It configures the component dev server using either webpack via @cypress/webpack-dev-server or Vite via @cypress/vite-dev-server, automatically detecting the project bundler from package.json. Test generation creates mount calls with proper prop injection, slot content for Vue components, and Angular module imports with dependency injection mocking. The skill sets up intercept patterns using cy.intercept() for API mocking, custom cy.commands for shared authentication flows, and fixture data management. Visual regression is handled through cypress-image-snapshot plugin with configurable diff thresholds and baseline management. Each test includes proper cleanup, state isolation via beforeEach hooks, and accessibility assertions using cypress-axe for WCAG 2.1 AA compliance checking. The generated cypress.config.ts includes optimal viewport settings, retry configuration, and parallel recording setup for Cypress Cloud dashboard integration.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-testing-framework-2/)
