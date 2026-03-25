---
name: "Cypress Visual Regression Runner"
description: "Runs visual regression tests comparing screenshots captured via Cypress cy.screenshot() against baseline images using pixelmatch diffing. Integrates with Percy SDK for cross-browser visual snapshots."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cypress-visual-regression-runner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cypress"  # from ase_tool_match
  github_stars: 49612  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 7404178  # from ase_npm_downloads
  github_repo: "cypress-io/cypress"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cypress Visual Regression Runner

Runs visual regression tests comparing screenshots captured via Cypress cy.screenshot() against baseline images using pixelmatch diffing. Integrates with Percy SDK for cross-browser visual snapshots.

## Overview

The Cypress Visual Regression Runner automates visual comparison testing by capturing page screenshots during Cypress test runs and comparing them against approved baselines. The skill wraps Cypress cy.screenshot() with configurable viewport sizes, element targeting via cy.get() selectors, and scroll position management. Screenshot comparison uses the pixelmatch library with configurable thresholds for color difference tolerance (default: 0.1) and minimum pixel count for failure (default: 100 pixels). Failed comparisons generate diff images highlighting changed regions with configurable overlay colors. The skill supports full-page screenshots via scrolling capture, element-level screenshots with padding options, and multi-viewport testing across mobile, tablet, and desktop breakpoints defined in cypress.config.js. Baseline management includes automatic approval workflows where new screenshots are flagged for review and approved baselines are committed to the repository. For cross-browser testing, the skill integrates with Percy SDK via @percy/cypress, uploading snapshots to Percy’s cloud rendering service for comparison across Chrome, Firefox, Safari, and Edge. CI integration supports parallel test execution with Cypress Dashboard for distributed screenshot capture across multiple test runners.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-runner -a codex
```

### OpenClaw

```bash
clawhub install cypress-visual-regression-runner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cypress-visual-regression-runner/
