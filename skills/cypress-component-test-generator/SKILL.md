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
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress Component Test Generator

The Cypress Component Test Generator skill analyzes React and Vue component source files using Babel AST parsing to automatically generate comprehensive Cypress component test suites. It identifies props interfaces, event handlers, conditional renders, and slot content to produce meaningful test coverage.

For React components, the generator creates mount tests with all prop combinations, simulates user interactions via cy.click and cy.type commands, and validates rendered output against expected DOM structures. Vue components receive equivalent treatment with Vuex store mocking and Vue Router stub injection.

Accessibility tests are generated automatically using cypress-axe integration, checking WCAG 2.1 AA compliance for each component state. The generator produces both happy-path and edge-case scenarios including empty states, error boundaries, and loading skeletons. Output follows Cypress best practices with proper beforeEach hooks, custom commands, and fixture data management.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-component-test-generator/)
