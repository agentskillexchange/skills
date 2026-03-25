---
name: "Playwright Test Generator with Codegen"
description: "Records and generates end-to-end test scripts using Playwright Codegen with multi-browser targeting. Produces TypeScript test files compatible with Playwright Test runner, handles visual regression via playwright-visual-regression plugin, and integrates with Allure reporting."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-test-generator-codegen/"
tool_ecosystem:
  tool: "playwright"
  github_stars: 84938
  npm_weekly_downloads: 39806814
  github_repo: "microsoft/playwright"
  license: "Apache-2.0"
  maintained: true
---

# Playwright Test Generator with Codegen

Records and generates end-to-end test scripts using Playwright Codegen with multi-browser targeting. Produces TypeScript test files compatible with Playwright Test runner, handles visual regression via playwright-visual-regression plugin, and integrates with Allure reporting.

## Overview

The Playwright Test Generator leverages Playwright Codegen to record user interactions and produce maintainable end-to-end test scripts. Recording sessions capture clicks, form fills, navigation, and assertions across Chromium, Firefox, and WebKit browsers simultaneously through Playwright multi-browser architecture.

Generated tests use the Playwright Test runner with TypeScript for type-safe selectors, built-in auto-waiting, and web-first assertions that eliminate flaky test patterns. The Page Object Model pattern is applied to generated code with automatic selector optimization preferring test-id attributes, ARIA roles, and text content over brittle CSS selectors.

Visual regression testing integrates through the playwright-visual-regression plugin with configurable diff thresholds, platform-specific baselines, and automatic screenshot management. Test results flow to Allure reporting framework producing rich HTML reports with step-by-step traces, screenshots, and video recordings attached to failed tests. The generator supports API mocking via Playwright route interception for isolated frontend testing, and network HAR recording for replay-based test stabilization. Parallel execution leverages Playwright sharding for CI environments with automatic retry configuration for infrastructure-related failures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-test-generator-codegen
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-test-generator-codegen -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-test-generator-codegen -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-test-generator-codegen -a codex
```

### OpenClaw

```bash
clawhub install playwright-test-generator-codegen
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-test-generator-codegen/
