---
name: "Playwright Visual Regression Suite"
description: "Automated visual regression testing using Playwright’s screenshot comparison API (page.screenshot with maxDiffPixelRatio) and toMatchSnapshot assertions. Supports cross-browser testing on Chromium, Firefox, and WebKit."
category: "Browser Automation"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-visual-regression-suite/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Visual Regression Suite

Automated visual regression testing using Playwright’s screenshot comparison API (page.screenshot with maxDiffPixelRatio) and toMatchSnapshot assertions. Supports cross-browser testing on Chromium, Firefox, and WebKit.

## Overview

The Playwright Visual Regression Suite automates UI consistency checks using Playwright’s built-in screenshot comparison capabilities. It leverages page.screenshot() with configurable options including fullPage captures, element-level screenshots via locator.screenshot(), and clip regions for specific viewport areas.

The skill uses expect(screenshot).toMatchSnapshot() with tunable thresholds: maxDiffPixels for absolute pixel differences and maxDiffPixelRatio for percentage-based tolerance. It supports cross-browser baselines across Chromium, Firefox, and WebKit, maintaining separate golden files per browser and viewport size.

Advanced features include animation disabling via page.evaluate to freeze CSS transitions, font anti-aliasing normalization for CI environments, and dark/light theme variant testing. The suite integrates with Playwright’s test runner for parallel execution, generates HTML diff reports showing before/after/difference overlays, and supports baseline update workflows via –update-snapshots flag. CI integration includes GitHub Actions artifacts for failed screenshot storage.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-visual-regression-suite -a codex
```

### OpenClaw

```bash
clawhub install playwright-visual-regression-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-visual-regression-suite/
