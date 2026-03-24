---
name: "Puppeteer Visual Regression Tester"
description: "Automates visual regression testing using Puppeteer page.screenshot() with pixelmatch diffing. Captures full-page screenshots at multiple viewport sizes and generates HTML diff reports with highlighted change regions."
category: "Browser Automation"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/puppeteer-visual-regression-tester/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93912  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Puppeteer Visual Regression Tester

Automates visual regression testing using Puppeteer page.screenshot() with pixelmatch diffing. Captures full-page screenshots at multiple viewport sizes and generates HTML diff reports with highlighted change regions.

## Overview

This skill automates visual regression testing for web applications using Puppeteer and the pixelmatch image comparison library. It captures full-page screenshots using page.screenshot({ fullPage: true }) at configurable viewport sizes and compares them against baseline images to detect unintended visual changes.

The skill supports multiple viewport configurations (mobile, tablet, desktop, ultrawide) and handles dynamic content by injecting CSS to hide animations, carousels, and timestamp elements before capture. It uses page.evaluate() to scroll through lazy-loaded content and wait for all network requests to settle via page.waitForNetworkIdle().

Diff reports are generated as interactive HTML files with side-by-side comparisons, overlay mode, and highlighted change regions. Configurable threshold settings allow teams to tune sensitivity for different page sections, ignoring sub-pixel rendering differences while catching layout shifts.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-tester -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-visual-regression-tester
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-visual-regression-tester/
