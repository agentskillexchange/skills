---
title: "Cypress Network Stub Generator"
description: "The Cypress Network Stub Generator converts HAR (HTTP Archive) files into deterministic cy.intercept() route handlers for Cypress E2E tests. It parses HAR entries to create matching routeHandlers with appropriate status codes, headers, and response bodies for each API endpoint. The skill leverages cy.session() to cache authentication state across test specs, dramatically reducing login overhead in large test suites. For applications spanning multiple domains, it uses cy.origin() to handle cross-origin interactions without disabling web security. Key features include automatic fixture file generation from HAR response bodies, intelligent URL pattern matching using minimatch globs for dynamic API paths, and cy.clock() integration for time-dependent response scenarios. It supports GraphQL request matching by parsing query operation names from request bodies and routing to appropriate stub responses. The generator also creates cy.wait() aliases for intercepted routes to enable reliable assertion timing."
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

# Cypress Network Stub Generator

The Cypress Network Stub Generator converts HAR (HTTP Archive) files into deterministic cy.intercept() route handlers for Cypress E2E tests. It parses HAR entries to create matching routeHandlers with appropriate status codes, headers, and response bodies for each API endpoint. The skill leverages cy.session() to cache authentication state across test specs, dramatically reducing login overhead in large test suites. For applications spanning multiple domains, it uses cy.origin() to handle cross-origin interactions without disabling web security. Key features include automatic fixture file generation from HAR response bodies, intelligent URL pattern matching using minimatch globs for dynamic API paths, and cy.clock() integration for time-dependent response scenarios. It supports GraphQL request matching by parsing query operation names from request bodies and routing to appropriate stub responses. The generator also creates cy.wait() aliases for intercepted routes to enable reliable assertion timing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-network-stub-generator/)
