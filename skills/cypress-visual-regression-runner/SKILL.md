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
  npm_package: "cypress"
  npm_weekly_downloads: 7268478
---

# Cypress Visual Regression Runner

The Cypress Visual Regression Runner automates visual comparison testing by capturing page screenshots during Cypress test runs and comparing them against approved baselines. The skill wraps Cypress cy.screenshot() with configurable viewport sizes, element targeting via cy.get() selectors, and scroll position management. Screenshot comparison uses the pixelmatch library with configurable thresholds for color difference tolerance (default: 0.1) and minimum pixel count for failure (default: 100 pixels). Failed comparisons generate diff images highlighting changed regions with configurable overlay colors. The skill supports full-page screenshots via scrolling capture, element-level screenshots with padding options, and multi-viewport testing across mobile, tablet, and desktop breakpoints defined in cypress.config.js. Baseline management includes automatic approval workflows where new screenshots are flagged for review and approved baselines are committed to the repository. For cross-browser testing, the skill integrates with Percy SDK via @percy/cypress, uploading snapshots to Percy’s cloud rendering service for comparison across Chrome, Firefox, Safari, and Edge. CI integration supports parallel test execution with Cypress Dashboard for distributed screenshot capture across multiple test runners.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cypress-visual-regression-runner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cypress-visual-regression-runner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cypress-visual-regression-runner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-visual-regression-runner/)
