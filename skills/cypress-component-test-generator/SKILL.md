---
name: "Cypress Component Test Generator"
description: "Auto-generates Cypress component tests from React and Vue source files using AST parsing. Produces mount, interaction, and accessibility test cases."
category: "Browser Automation"
framework: "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cypress-component-test-generator/"
tool_ecosystem:
  tool: cypress
  github_stars: 49611
  npm_weekly_downloads: 7404178
  github_repo: cypress-io/cypress
  license: MIT
  maintained: true
---

# Cypress Component Test Generator

Auto-generates Cypress component tests from React and Vue source files using AST parsing. Produces mount, interaction, and accessibility test cases.

## Overview

The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage.

For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection.

Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-component-test-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-component-test-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-component-test-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-component-test-generator -a codex
```

### OpenClaw

```bash
clawhub install cypress-component-test-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cypress-component-test-generator/
