---
title: "Cypress Visual Regression Runner"
description: "Runs visual regression tests comparing screenshots captured via Cypress cy.screenshot() against baseline images using pixelmatch diffing. Integrates with Percy SDK for cross-browser visual snapshots."
slug: "cypress-visual-regression-runner"
category:
  - "Browser Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cypress-visual-regression-runner/"
listed: true
---

# Cypress Visual Regression Runner

Runs visual regression tests comparing screenshots captured via Cypress cy.screenshot() against baseline images using pixelmatch diffing. Integrates with Percy SDK for cross-browser visual snapshots.

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
clawhub install cypress-visual-regression-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cypress Visual Regression Runner automates visual comparison testing by capturing page screenshots during Cypress test runs and comparing them against approved baselines. The skill wraps Cypress cy.screenshot() with configurable viewport sizes, element targeting via cy.get() selectors, and scroll position management. Screenshot comparison uses the pixelmatch library with configurable thresholds for color difference tolerance (default: 0.1) and minimum pixel count for failure (default: 100 pixels). Failed comparisons generate diff images highlighting changed regions with configurable overlay colors. The skill supports full-page screenshots via scrolling capture, element-level screenshots with padding options, and multi-viewport testing across mobile, tablet, and desktop breakpoints defined in cypress.config.js. Baseline management includes automatic approval workflows where new screenshots are flagged for review and approved baselines are committed to the repository. For cross-browser testing, the skill integrates with Percy SDK via @percy/cypress, uploading snapshots to Percy’s cloud rendering service for comparison across Chrome, Firefox, Safari, and Edge. CI integration supports parallel test execution with Cypress Dashboard for distributed screenshot capture across multiple test runners.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cypress-visual-regression-runner/)
