---
title: "Cypress Component Test Generator"
description: "The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage. For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection. Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management."
source: "https://github.com/cypress-io/cypress"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress Component Test Generator

The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage. For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection. Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-test-generator/)
