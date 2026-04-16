---
title: "Cypress Visual Regression Runner"
description: "Runs visual regression tests comparing screenshots captured via Cypress cy.screenshot() against baseline images using pixelmatch diffing. Integrates with Percy SDK for cross-browser visual snapshots."
verification: "security_reviewed"
source: "https://github.com/cypress-io/cypress"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "cypress-io/cypress"
  github_stars: 49617
  ase_npm_package: "cypress"
  npm_weekly_downloads: 7268478
  license: "MIT"
---

# Cypress Visual Regression Runner

The Cypress Visual Regression Runner automates visual comparison testing by capturing page screenshots during Cypress test runs and comparing them against approved baselines. The skill wraps Cypress cy.screenshot() with configurable viewport sizes, element targeting via cy.get() selectors, and scroll position management. Screenshot comparison uses the pixelmatch library with configurable thresholds for color difference tolerance (default: 0.1) and minimum pixel count for failure (default: 100 pixels). Failed comparisons generate diff images highlighting changed regions with configurable overlay colors. The skill supports full-page screenshots via scrolling capture, element-level screenshots with padding options, and multi-viewport testing across mobile, tablet, and desktop breakpoints defined in cypress.config.js. Baseline management includes automatic approval workflows where new screenshots are flagged for review and approved baselines are committed to the repository. For cross-browser testing, the skill integrates with Percy SDK via @percy/cypress, uploading snapshots to Percy’s cloud rendering service for comparison across Chrome, Firefox, Safari, and Edge. CI integration supports parallel test execution with Cypress Dashboard for distributed screenshot capture across multiple test runners.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-visual-regression-runner/)
