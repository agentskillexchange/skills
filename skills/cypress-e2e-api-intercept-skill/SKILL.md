---
name: "Cypress E2E API Intercept Skill"
description: "Creates end-to-end tests with Cypress cy.intercept() for API mocking and cy.wait() for request assertion. Uses Cypress Testing Library queries with findByRole() and findByText() for accessible element selection."
category: "Browser Automation"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
tool_ecosystem:
  tool: cypress
  github_repo: cypress-io/cypress
  github_stars: 49610
  license: MIT
  maintained: true
---
# Cypress E2E API Intercept Skill

Creates end-to-end tests with Cypress cy.intercept() for API mocking and cy.wait() for request assertion. Uses Cypress Testing Library queries with findByRole() and findByText() for accessible element selection.

## Overview

This skill generates comprehensive end-to-end test suites using the Cypress testing framework with advanced API interception capabilities. It uses cy.intercept() to mock, stub, and spy on HTTP requests, enabling tests to run independently of backend services. API responses are stubbed using cy.intercept("GET", "/api/users", { fixture: "users.json" }) with support for dynamic response generation via routeHandler callbacks. Request assertions use cy.wait("@alias") to verify request bodies, headers, and query parameters. The skill integrates Cypress Testing Library for accessible element queries: cy.findByRole("button", { name: /submit/i }), cy.findByText(), and cy.findByLabelText(). It generates test files following the Arrange-Act-Assert pattern with proper beforeEach hooks for setup. Custom commands are defined via Cypress.Commands.add() for reusable login flows, data seeding, and cleanup operations. The skill supports component testing via cy.mount() for React/Vue components and generates cypress.config.js with proper baseUrl, viewportWidth, and retries configuration. Test data management uses cy.fixture() for JSON fixtures and cy.task() for database operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-api-intercept-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-api-intercept-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-api-intercept-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-e2e-api-intercept-skill -a codex
```

### OpenClaw

```bash
clawhub install cypress-e2e-api-intercept-skill
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-e2e-api-intercept-skill/)
