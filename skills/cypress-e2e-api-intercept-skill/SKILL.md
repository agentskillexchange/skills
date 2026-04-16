---
title: "Cypress E2E API Intercept Skill"
description: "Creates end-to-end tests with Cypress cy.intercept() for API mocking and cy.wait() for request assertion. Uses Cypress Testing Library queries with findByRole() and findByText() for accessible element selection."
verification: "security_reviewed"
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  ase_npm_package: "cypress"
  npm_weekly_downloads: 7268478
  license: "MIT"
---

# Cypress E2E API Intercept Skill

This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept(“GET”, “/api/users”, { fixture: “users.json” }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait(“@alias”) to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole(“button”, { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/)
