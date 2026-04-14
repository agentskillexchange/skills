---
title: "Cypress E2E API Intercept Skill"
description: "Creates end-to-end tests with Cypress cy.intercept() for API mocking and cy.wait() for request assertion. Uses Cypress Testing Library queries with findByRole() and findByText() for accessible element selection."
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
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

This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept(“GET”, “/api/users”, { fixture: “users.json” }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait(“@alias”) to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole(“button”, { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/)
