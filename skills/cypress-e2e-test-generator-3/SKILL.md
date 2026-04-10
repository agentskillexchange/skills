---
name: Cypress E2E Test Generator
description: Generates Cypress end-to-end test suites from user flow recordings. Uses
  the Cypress Real Events plugin and cy.intercept() for network stubbing with automatic
  fixture generation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/
category:
- Browser Automation
framework:
- Claude Agents
---
# Cypress E2E Test Generator

Automated end-to-end test generation agent for Cypress testing framework. Records user interaction flows and converts them into maintainable Cypress test specifications. Uses the Cypress Real Events plugin for accurate mouse and keyboard event simulation. Generates network request fixtures automatically using cy.intercept() to capture and replay API responses. Implements the Page Object Model pattern for generated tests with automatic selector optimization favoring data-testid attributes over fragile CSS selectors. Supports custom command generation for repeated interaction patterns. Integrates with Cypress Dashboard for test analytics, parallelization, and flaky test management. Includes visual testing via the cypress-image-snapshot plugin. Generates TypeScript test files with full type definitions for custom commands and fixtures.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-test-generator-3/)
