---
name: "Cypress Network Stub Generator"
description: "Generates cy.intercept() stubs from recorded HAR files for deterministic E2E tests. Uses cy.session() for authentication caching and cy.origin() for cross-origin testing workflows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cypress-network-stub-generator/"
category:
  - "Browser Automation"
framework:
  - "Codex"
---

# Cypress Network Stub Generator

The Cypress Network Stub Generator converts HAR (HTTP Archive) files into deterministic cy.intercept() route handlers for Cypress E2E tests. It parses HAR entries to create matching routeHandlers with appropriate status codes, headers, and response bodies for each API endpoint.
The skill leverages cy.session() to cache authentication state across test specs, dramatically reducing login overhead in large test suites. For applications spanning multiple domains, it uses cy.origin() to handle cross-origin interactions without disabling web security.
Key features include automatic fixture file generation from HAR response bodies, intelligent URL pattern matching using minimatch globs for dynamic API paths, and cy.clock() integration for time-dependent response scenarios. It supports GraphQL request matching by parsing query operation names from request bodies and routing to appropriate stub responses. The generator also creates cy.wait() aliases for intercepted routes to enable reliable assertion timing.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-network-stub-generator/)
