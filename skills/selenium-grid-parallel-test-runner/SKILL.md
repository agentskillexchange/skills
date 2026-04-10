---
name: Selenium Grid Parallel Test Runner
description: Orchestrates distributed browser tests across Selenium Grid 4 nodes with
  dynamic scaling. Uses selenium-webdriver RemoteWebDriver with W3C WebDriver protocol
  and Zalenium-style video recording.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/
category:
- Browser Automation
framework:
- Cursor
---
# Selenium Grid Parallel Test Runner

The Selenium Grid Parallel Test Runner distributes browser automation workloads across a Selenium Grid 4 cluster for maximum throughput. It uses the selenium-webdriver RemoteWebDriver interface with W3C WebDriver protocol compliance for cross-browser compatibility. The skill dynamically provisions grid nodes based on test queue depth using the Grid 4 GraphQL API for real-time capacity monitoring. Each test session gets an isolated node with configurable browser capabilities including screen resolution, timezone, and locale. Video recording captures every session using the FFMPEG-based recorder built into Selenium Grid 4 Docker images. Test artifacts including screenshots, page sources, and console logs are automatically collected and organized by test run ID. The skill supports retry logic with configurable max attempts and failure categorization for flaky test identification. Integration with TestNG and JUnit reporters generates detailed HTML dashboards.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/)
