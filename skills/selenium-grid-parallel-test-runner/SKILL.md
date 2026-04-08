---
title: Selenium Grid Parallel Test Runner
description: The Selenium Grid Parallel Test Runner distributes browser automation
  workloads across a Selenium Grid 4 cluster for maximum throughput. It uses the selenium-webdriver
  RemoteWebDriver interface with W3C WebDriver protocol compliance for cross-browser
  compatibility. The skill dynamically provisions grid nodes based on test queue depth
  using the Grid 4 GraphQL API for real-time capacity monitoring. Each test session
  gets an isolated node with configurable browser capabilities including screen resolution,
  timezone, and locale. Video recording captures every session using the FFMPEG-based
  recorder built into Selenium Grid 4 Docker images. Test artifacts including screenshots,
  page sources, and console logs are automatically collected and organized by test
  run ID. The skill supports retry logic with configurable max attempts and failure
  categorization for flaky test identification. Integration with TestNG and JUnit
  reporters generates detailed HTML dashboards.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-test-runner/)
