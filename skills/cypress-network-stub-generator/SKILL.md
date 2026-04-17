---
title: "Cypress Network Stub Generator"
description: "Generates cy.intercept() stubs from recorded HAR files for deterministic E2E tests. Uses cy.session() for authentication caching and cy.origin() for cross-origin testing workflows."
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
  license: "MIT"
---

# Cypress Network Stub Generator

The Cypress Network Stub Generator converts HAR (HTTP Archive) files into deterministic cy.intercept() route handlers for Cypress E2E tests. It parses HAR entries to create matching routeHandlers with appropriate status codes, headers, and response bodies for each API endpoint.

The skill leverages cy.session() to cache authentication state across test specs, dramatically reducing login overhead in large test suites. For applications spanning multiple domains, it uses cy.origin() to handle cross-origin interactions without disabling web security.

Key features include automatic fixture file generation from HAR response bodies, intelligent URL pattern matching using minimatch globs for dynamic API paths, and cy.clock() integration for time-dependent response scenarios. It supports GraphQL request matching by parsing query operation names from request bodies and routing to appropriate stub responses. The generator also creates cy.wait() aliases for intercepted routes to enable reliable assertion timing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cypress-network-stub-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cypress-network-stub-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-network-stub-generator/)
