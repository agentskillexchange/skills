---
title: "Cypress Component Test Generator"
description: "Auto-generates Cypress component tests from React and Vue source files using AST parsing. Produces mount, interaction, and accessibility test cases."
verification: security_reviewed
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  ase_npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress Component Test Generator

The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage.

For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection.

Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cypress-component-test-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cypress-component-test-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-test-generator/)
