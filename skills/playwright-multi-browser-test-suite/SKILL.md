---
name: Playwright Multi-Browser Test Suite
description: Generates end-to-end test suites using the Playwright Test Runner API
  with cross-browser coverage on Chromium, Firefox, and WebKit. Implements visual
  regression testing via the Playwright Screenshots API and network mocking.
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-multi-browser-test-suite/
category:
- Browser Automation
framework:
- Cursor
---
# Playwright Multi-Browser Test Suite

The Playwright Multi-Browser Test Suite skill creates comprehensive end-to-end testing workflows using Playwright. It leverages the Playwright Test Runner API to generate test files with proper fixture setup, page object models, and parallel execution configuration across Chromium, Firefox, and WebKit browsers. Visual regression testing is implemented through the Playwright Screenshots API with configurable comparison thresholds, mask regions for dynamic content, and automatic baseline management. The skill configures network request interception for API mocking, enabling isolated frontend testing without backend dependencies. It supports trace recording via Playwright Trace Viewer for debugging failed tests, video capture of test runs for visual review, and HAR file generation for network analysis. Test generation includes accessibility checks using the Playwright accessibility snapshot API, geolocation and locale emulation for internationalization testing, and mobile device emulation with custom viewport configurations. The skill integrates with CI systems through proper reporter configuration including HTML, JSON, and JUnit output formats.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-multi-browser-test-suite/)
