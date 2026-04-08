---
title: Cypress Component Test Generator
description: The Cypress Component Test Generator skill analyzes React and Vue component
  source files using Babel AST parsing to automatically generate comprehensive Cypress
  component test suites. It identifies props interfaces, event handlers, conditional
  renders, and slot content to produce meaningful test coverage. For React components,
  the generator creates mount tests with all prop combinations, simulates user interactions
  via cy.click and cy.type commands, and validates rendered output against expected
  DOM structures. Vue components receive equivalent treatment with Vuex store mocking
  and Vue Router stub injection. Accessibility tests are generated automatically using
  cypress-axe integration, checking WCAG 2.1 AA compliance for each component state.
  The generator produces both happy-path and edge-case scenarios including empty states,
  error boundaries, and loading skeletons. Output follows Cypress best practices with
  proper beforeEach hooks, custom commands, and fixture data management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cypress-component-test-generator/
category:
- Browser Automation
framework:
- ChatGPT Agents
---

# Cypress Component Test Generator

The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage. For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection. Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-test-generator/)
