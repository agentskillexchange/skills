---
name: "Selenium Grid Parallel Test Runner"
description: "Orchestrates distributed browser tests across Selenium Grid 4 nodes with dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol and Zalenium-style video recording."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/seleniumhq/selenium"
tool_ecosystem:
  tool: selenium
  github_repo: seleniumhq/selenium
  github_stars: 34196
  license: Apache-2.0
  maintained: true
---
# Selenium Grid Parallel Test Runner

Orchestrates distributed browser tests across Selenium Grid 4 nodes with dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol and Zalenium-style video recording.

## Overview

The Selenium Grid Parallel Test Runner distributes browser automation workloads across a Selenium Grid 4 cluster for maximum throughput. It uses the selenium-webdriver RemoteWebDriver interface with W3C WebDriver protocol compliance for cross-browser compatibility. The skill dynamically provisions grid nodes based on test queue depth using the Grid 4 GraphQL API for real-time capacity monitoring. Each test session gets an isolated node with configurable browser capabilities including screen resolution, timezone, and locale. Video recording captures every session using the FFMPEG-based recorder built into Selenium Grid 4 Docker images. Test artifacts including screenshots, page sources, and console logs are automatically collected and organized by test run ID. The skill supports retry logic with configurable max attempts and failure categorization for flaky test identification. Integration with TestNG and JUnit reporters generates detailed HTML dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-test-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-test-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-test-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-test-runner -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-parallel-test-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/)
