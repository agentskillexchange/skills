---
title: Cypress Visual Regression Runner
description: 'The Cypress Visual Regression Runner automates visual comparison testing
  by capturing page screenshots during Cypress test runs and comparing them against
  approved baselines. The skill wraps Cypress cy.screenshot() with configurable viewport
  sizes, element targeting via cy.get() selectors, and scroll position management.
  Screenshot comparison uses the pixelmatch library with configurable thresholds for
  color difference tolerance (default: 0.1) and minimum pixel count for failure (default:
  100 pixels). Failed comparisons generate diff images highlighting changed regions
  with configurable overlay colors. The skill supports full-page screenshots via scrolling
  capture, element-level screenshots with padding options, and multi-viewport testing
  across mobile, tablet, and desktop breakpoints defined in cypress.config.js. Baseline
  management includes automatic approval workflows where new screenshots are flagged
  for review and approved baselines are committed to the repository. For cross-browser
  testing, the skill integrates with Percy SDK via @percy/cypress, uploading snapshots
  to Percy’s cloud rendering service for comparison across Chrome, Firefox, Safari,
  and Edge. CI integration supports parallel test execution with Cypress Dashboard
  for distributed screenshot capture across multiple test runners.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/cypress-visual-regression-runner/
category:
- Browser Automation
framework:
- Cursor
---

# Cypress Visual Regression Runner

The Cypress Visual Regression Runner automates visual comparison testing by capturing page screenshots during Cypress test runs and comparing them against approved baselines. The skill wraps Cypress cy.screenshot() with configurable viewport sizes, element targeting via cy.get() selectors, and scroll position management. Screenshot comparison uses the pixelmatch library with configurable thresholds for color difference tolerance (default: 0.1) and minimum pixel count for failure (default: 100 pixels). Failed comparisons generate diff images highlighting changed regions with configurable overlay colors. The skill supports full-page screenshots via scrolling capture, element-level screenshots with padding options, and multi-viewport testing across mobile, tablet, and desktop breakpoints defined in cypress.config.js. Baseline management includes automatic approval workflows where new screenshots are flagged for review and approved baselines are committed to the repository. For cross-browser testing, the skill integrates with Percy SDK via @percy/cypress, uploading snapshots to Percy’s cloud rendering service for comparison across Chrome, Firefox, Safari, and Edge. CI integration supports parallel test execution with Cypress Dashboard for distributed screenshot capture across multiple test runners.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-visual-regression-runner/)
