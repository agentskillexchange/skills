---
title: "Cypress E2E Test Generator"
description: "Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation."
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress E2E Test Generator

Automated end-to-end test generation agent for Cypress testing framework. Records user interaction flows and converts them into maintainable Cypress test specifications. Uses the Cypress Real Events plugin for accurate mouse and keyboard event simulation. Generates network request fixtures automatically using cy.intercept() to capture and replay API responses. Implements the Page Object Model pattern for generated tests with automatic selector optimization favoring data-testid attributes over fragile CSS selectors. Supports custom command generation for repeated interaction patterns. Integrates with Cypress Dashboard for test analytics, parallelization, and flaky test management. Includes visual testing via the cypress-image-snapshot plugin. Generates TypeScript test files with full type definitions for custom commands and fixtures.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/)
