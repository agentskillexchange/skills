---
title: "Playwright Test Generator with Codegen"
description: "Records and generates end-to-end test scripts using Playwright Codegen with multi-browser targeting. Produces TypeScript test files compatible with Playwright Test runner, handles visual regression via playwright-visual-regression plugin, and integrates with Allure reporting."
slug: "playwright-test-generator-codegen"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-test-generator-codegen/"
---

# Playwright Test Generator with Codegen

Records and generates end-to-end test scripts using Playwright Codegen with multi-browser targeting. Produces TypeScript test files compatible with Playwright Test runner, handles visual regression via playwright-visual-regression plugin, and integrates with Allure reporting.

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
clawhub install playwright-test-generator-codegen
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Playwright Test Generator leverages Playwright Codegen to record user interactions and produce maintainable end-to-end test scripts. Recording sessions capture clicks, form fills, navigation, and assertions across Chromium, Firefox, and WebKit browsers simultaneously through Playwright multi-browser architecture.
Generated tests use the Playwright Test runner with TypeScript for type-safe selectors, built-in auto-waiting, and web-first assertions that eliminate flaky test patterns. The Page Object Model pattern is applied to generated code with automatic selector optimization preferring test-id attributes, ARIA roles, and text content over brittle CSS selectors.
Visual regression testing integrates through the playwright-visual-regression plugin with configurable diff thresholds, platform-specific baselines, and automatic screenshot management. Test results flow to Allure reporting framework producing rich HTML reports with step-by-step traces, screenshots, and video recordings attached to failed tests. The generator supports API mocking via Playwright route interception for isolated frontend testing, and network HAR recording for replay-based test stabilization. Parallel execution leverages Playwright sharding for CI environments with automatic retry configuration for infrastructure-related failures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-generator-codegen/)
