---
name: Playwright Visual Regression Suite
description: Automated visual regression testing using Playwright&#8217;s screenshot
  comparison API (page.screenshot with maxDiffPixelRatio) and toMatchSnapshot assertions.
  Supports cross-browser testing on Chromium, Firefox, and WebKit.
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-visual-regression-suite/
category:
- Browser Automation
framework:
- Codex
---
# Playwright Visual Regression Suite

The Playwright Visual Regression Suite automates UI consistency checks using Playwright's built-in screenshot comparison capabilities. It leverages page.screenshot() with configurable options including fullPage captures, element-level screenshots via locator.screenshot(), and clip regions for specific viewport areas.
The skill uses expect(screenshot).toMatchSnapshot() with tunable thresholds: maxDiffPixels for absolute pixel differences and maxDiffPixelRatio for percentage-based tolerance. It supports cross-browser baselines across Chromium, Firefox, and WebKit, maintaining separate golden files per browser and viewport size.
Advanced features include animation disabling via page.evaluate to freeze CSS transitions, font anti-aliasing normalization for CI environments, and dark/light theme variant testing. The suite integrates with Playwright's test runner for parallel execution, generates HTML diff reports showing before/after/difference overlays, and supports baseline update workflows via -update-snapshots flag. CI integration includes GitHub Actions artifacts for failed screenshot storage.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-visual-regression-suite/)
