---
title: "Cypress E2E API Intercept Skill"
description: "This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept(&#8220;GET&#8221;, &#8220;/api/users&#8221;, { fixture: &#8220;users.json&#8221; }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait(&#8220;@alias&#8221;) to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole(&#8220;button&#8221;, { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations."
source: "https://github.com/cypress-io/cypress"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress E2E API Intercept Skill

This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept(&#8220;GET&#8221;, &#8220;/api/users&#8221;, { fixture: &#8220;users.json&#8221; }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait(&#8220;@alias&#8221;) to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole(&#8220;button&#8221;, { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/)
