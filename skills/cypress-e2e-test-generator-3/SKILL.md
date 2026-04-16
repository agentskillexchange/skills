---
title: "Cypress E2E Test Generator"
description: "Generates Cypress end-to-end test suites from user flow recordings. Uses the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic fixture generation."
verification: "security_reviewed"
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  ase_npm_package: "cypress"
  npm_weekly_downloads: 7268478
  license: "MIT"
---

# Cypress E2E Test Generator

Automated end-to-end test generation agent for Cypress testing framework. Records user interaction flows and converts them into maintainable Cypress test specifications. Uses the Cypress Real Events plugin for accurate mouse and keyboard event simulation. Generates network request fixtures automatically using cy.intercept() to capture and replay API responses. Implements the Page Object Model pattern for generated tests with automatic selector optimization favoring data-testid attributes over fragile CSS selectors. Supports custom command generation for repeated interaction patterns. Integrates with Cypress Dashboard for test analytics, parallelization, and flaky test management. Includes visual testing via the cypress-image-snapshot plugin. Generates TypeScript test files with full type definitions for custom commands and fixtures.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/)
