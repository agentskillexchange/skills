---
name: "Playwright Multi-Browser Test Suite"
description: "Generates end-to-end test suites using the Playwright Test Runner API with cross-browser coverage on Chromium, Firefox, and WebKit. Implements visual regression testing via the Playwright Screenshots API and network mocking."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-multi-browser-test-suite/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Multi-Browser Test Suite

Generates end-to-end test suites using the Playwright Test Runner API with cross-browser coverage on Chromium, Firefox, and WebKit. Implements visual regression testing via the Playwright Screenshots API and network mocking.

## Overview

The Playwright Multi-Browser Test Suite skill creates comprehensive end-to-end testing workflows using Playwright. It leverages the Playwright Test Runner API to generate test files with proper fixture setup, page object models, and parallel execution configuration across Chromium, Firefox, and WebKit browsers. Visual regression testing is implemented through the Playwright Screenshots API with configurable comparison thresholds, mask regions for dynamic content, and automatic baseline management. The skill configures network request interception for API mocking, enabling isolated frontend testing without backend dependencies. It supports trace recording via Playwright Trace Viewer for debugging failed tests, video capture of test runs for visual review, and HAR file generation for network analysis. Test generation includes accessibility checks using the Playwright accessibility snapshot API, geolocation and locale emulation for internationalization testing, and mobile device emulation with custom viewport configurations. The skill integrates with CI systems through proper reporter configuration including HTML, JSON, and JUnit output formats.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-suite -a codex
```

### OpenClaw

```bash
clawhub install playwright-multi-browser-test-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-multi-browser-test-suite/
