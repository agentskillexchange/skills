---
title: "Selenium Grid Parallel Test Runner"
description: "Orchestrates distributed browser tests across Selenium Grid 4 nodes with dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol and Zalenium-style video recording."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/)
