---
title: "Selenium Grid Parallel Test Runner"
description: "Orchestrates distributed browser tests across Selenium Grid 4 nodes with dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol and Zalenium-style video recording."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Parallel Test Runner

The Selenium Grid Parallel Test Runner distributes browser automation workloads across a Selenium Grid 4 cluster for maximum throughput. It uses the selenium-webdriver RemoteWebDriver interface with W3C WebDriver protocol compliance for cross-browser compatibility. The skill dynamically provisions grid nodes based on test queue depth using the Grid 4 GraphQL API for real-time capacity monitoring. Each test session gets an isolated node with configurable browser capabilities including screen resolution, timezone, and locale. Video recording captures every session using the FFMPEG-based recorder built into Selenium Grid 4 Docker images. Test artifacts including screenshots, page sources, and console logs are automatically collected and organized by test run ID. The skill supports retry logic with configurable max attempts and failure categorization for flaky test identification. Integration with TestNG and JUnit reporters generates detailed HTML dashboards.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-parallel-test-runner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/selenium-grid-parallel-test-runner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/)
