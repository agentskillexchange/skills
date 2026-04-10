---
title: "Selenium Grid Parallel Test Runner"
description: "Orchestrates distributed browser tests across Selenium Grid 4 nodes with dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol and Zalenium-style video recording."
slug: "selenium-grid-parallel-test-runner"
category:
  - "Browser Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/"
---

# Selenium Grid Parallel Test Runner

Orchestrates distributed browser tests across Selenium Grid 4 nodes with dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol and Zalenium-style video recording.

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
clawhub install selenium-grid-parallel-test-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Parallel Test Runner distributes browser automation workloads across a Selenium Grid 4 cluster for maximum throughput. It uses the selenium-webdriver RemoteWebDriver interface with W3C WebDriver protocol compliance for cross-browser compatibility. The skill dynamically provisions grid nodes based on test queue depth using the Grid 4 GraphQL API for real-time capacity monitoring. Each test session gets an isolated node with configurable browser capabilities including screen resolution, timezone, and locale. Video recording captures every session using the FFMPEG-based recorder built into Selenium Grid 4 Docker images. Test artifacts including screenshots, page sources, and console logs are automatically collected and organized by test run ID. The skill supports retry logic with configurable max attempts and failure categorization for flaky test identification. Integration with TestNG and JUnit reporters generates detailed HTML dashboards.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/)
