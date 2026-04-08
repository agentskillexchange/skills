---
title: Cypress E2E API Intercept Skill
description: 'This skill generates comprehensive end-to-end test suites using the
  Cypress testing framework with advanced API interception capabilities. It uses cy.intercept()
  to mock, stub, and spy on HTTP requests, enabling tests to run independently of
  backend services. API responses are stubbed using cy.intercept(“GET”, “/api/users”,
  { fixture: “users.json” }) with support for dynamic response generation via routeHandler
  callbacks. Request assertions use cy.wait(“@alias”) to verify request bodies, headers,
  and query parameters. The skill integrates Cypress Testing Library for accessible
  element queries: cy.findByRole(“button”, { name: /submit/i }), cy.findByText(),
  and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert
  pattern with proper beforeEach hooks for setup. Custom commands are defined via
  Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations.
  The skill supports component testing via cy.mount() for React/Vue components and
  generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration.
  Test data management uses cy.fixture() for JSON fixtures and cy.task() for database
  operations.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/
category:
- Browser Automation
framework:
- Codex
---

# Cypress E2E API Intercept Skill

This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept(“GET”, “/api/users”, { fixture: “users.json” }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait(“@alias”) to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole(“button”, { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/)
