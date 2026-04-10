---
title: "Cypress Component Test Generator"
description: "Auto-generates Cypress component tests from React and Vue source files using AST parsing. Produces mount, interaction, and accessibility test cases."
slug: "cypress-component-test-generator"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cypress-component-test-generator/"
---

# Cypress Component Test Generator

Auto-generates Cypress component tests from React and Vue source files using AST parsing. Produces mount, interaction, and accessibility test cases.

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
clawhub install cypress-component-test-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage.
For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection.
Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-test-generator/)
