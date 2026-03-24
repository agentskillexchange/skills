---
name: "Playwright Multi-Browser Test Generator"
description: "Generates Playwright test scripts for Chromium, Firefox, and WebKit from natural language descriptions. Uses the Playwright codegen recorder API and assertion library for reliable E2E tests."
category: "Browser Automation"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-multi-browser-test-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Multi-Browser Test Generator

Generates Playwright test scripts for Chromium, Firefox, and WebKit from natural language descriptions. Uses the Playwright codegen recorder API and assertion library for reliable E2E tests.

## Overview

The Playwright Multi-Browser Test Generator creates production-ready end-to-end test scripts targeting all three browser engines supported by Playwright: Chromium, Firefox, and WebKit. Given natural language descriptions of user flows, it generates TypeScript test files using Playwright Test runner with proper fixtures, page object models, and auto-waiting assertions. The skill leverages Playwright locator strategies—role-based selectors, text content matching, and CSS/XPath fallbacks—to create resilient selectors that survive UI changes. It configures browser contexts with viewport settings, geolocation, permissions, and color scheme preferences for comprehensive coverage. Network interception via page.route() is used to mock API responses for deterministic testing. The generated tests include visual regression checks using Playwright screenshot comparison with configurable threshold values. Parallel execution is configured across browser projects with shared authentication state via storageState, and HTML test reports are generated with trace viewer integration for debugging failures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator -a codex
```

### OpenClaw

```bash
clawhub install playwright-multi-browser-test-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-multi-browser-test-generator/
