---
name: "Cypress Visual Regression Testing Suite"
description: "Automates pixel-level visual regression testing using Cypress with cypress-image-snapshot plugin. Compares screenshots against baselines using pixelmatch algorithm with configurable diff thresholds."
category: "Browser Automation"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cypress-visual-regression-testing-suite/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cypress"  # from ase_tool_match
  github_stars: 49612  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 7404178  # from ase_npm_downloads
  github_repo: "cypress-io/cypress"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cypress Visual Regression Testing Suite

Automates pixel-level visual regression testing using Cypress with cypress-image-snapshot plugin. Compares screenshots against baselines using pixelmatch algorithm with configurable diff thresholds.

## Overview

The Cypress Visual Regression Testing Suite enables automated visual comparison testing for web applications using the cypress-image-snapshot plugin built on jest-image-snapshot. It captures full-page and element-level screenshots during Cypress test runs and compares them against stored baseline images.

Image comparison uses the pixelmatch algorithm with configurable threshold sensitivity, anti-aliasing detection, and alpha channel handling. Failed comparisons generate three-panel diff images showing the baseline, actual screenshot, and pixel-level difference map with highlighted regions.

The skill supports responsive testing across multiple viewport configurations, dynamic content masking (clipping regions, element hiding via CSS injection), and animation stabilization through Cypress clock control and network idle detection. Baseline management includes automatic update workflows, branch-specific baseline directories, and cleanup of orphaned snapshots.

CI integration provides GitHub Actions and GitLab CI configurations with artifact upload for diff images, Slack notifications for visual regressions via incoming webhooks, and dashboard reporting through cypress-dashboard-api. Parallel execution support uses Cypress sharding with Sorry-cypress for self-hosted orchestration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-testing-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-testing-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-testing-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cypress-visual-regression-testing-suite -a codex
```

### OpenClaw

```bash
clawhub install cypress-visual-regression-testing-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cypress-visual-regression-testing-suite/
