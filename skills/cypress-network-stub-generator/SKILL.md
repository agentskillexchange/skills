---
title: "Cypress Network Stub Generator"
description: "Generates cy.intercept() stubs from recorded HAR files for deterministic E2E tests. Uses cy.session() for authentication caching and cy.origin() for cross-origin testing workflows."
slug: "cypress-network-stub-generator"
category:
  - "Browser Automation"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cypress-network-stub-generator/"
---

# Cypress Network Stub Generator

Generates cy.intercept() stubs from recorded HAR files for deterministic E2E tests. Uses cy.session() for authentication caching and cy.origin() for cross-origin testing workflows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install cypress-network-stub-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cypress Network Stub Generator converts HAR (HTTP Archive) files into deterministic cy.intercept() route handlers for Cypress E2E tests. It parses HAR entries to create matching routeHandlers with appropriate status codes, headers, and response bodies for each API endpoint.
The skill leverages cy.session() to cache authentication state across test specs, dramatically reducing login overhead in large test suites. For applications spanning multiple domains, it uses cy.origin() to handle cross-origin interactions without disabling web security.
Key features include automatic fixture file generation from HAR response bodies, intelligent URL pattern matching using minimatch globs for dynamic API paths, and cy.clock() integration for time-dependent response scenarios. It supports GraphQL request matching by parsing query operation names from request bodies and routing to appropriate stub responses. The generator also creates cy.wait() aliases for intercepted routes to enable reliable assertion timing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-network-stub-generator/)
