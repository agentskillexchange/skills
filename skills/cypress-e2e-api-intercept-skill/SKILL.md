---
name: "Cypress E2E API Intercept Skill"
description: "Creates end-to-end tests with Cypress cy.intercept() for API mocking and cy.wait() for request assertion. Uses Cypress Testing Library queries with findByRole() and findByText() for accessible element selection."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/"
category:
  - "Browser Automation"
framework:
  - "Codex"
---

# Cypress E2E API Intercept Skill

This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept(&#8220;GET&#8221;, &#8220;/api/users&#8221;, { fixture: &#8220;users.json&#8221; }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait(&#8220;@alias&#8221;) to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole(&#8220;button&#8221;, { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/)
