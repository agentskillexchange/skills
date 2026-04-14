---
title: "Selenium Grid Cloud Executor"
description: "Distributes browser test suites across Selenium Grid 4 nodes using RemoteWebDriver and the W3C WebDriver protocol. Supports parallel execution on BrowserStack and Sauce Labs with automatic capability negotiation."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Cloud Executor

This skill enables distributed browser test execution across Selenium Grid 4 infrastructure or cloud providers like BrowserStack and Sauce Labs. It uses the RemoteWebDriver API with the W3C WebDriver protocol for cross-browser compatibility testing at scale.

The skill handles capability negotiation automatically, selecting appropriate browser versions and OS combinations based on test requirements. It supports parallel test execution using TestNG or pytest-xdist, distributing test cases across available Grid nodes for maximum throughput. Session management includes automatic retry on node failures and intelligent load balancing.

Cloud provider integration handles authentication via environment variables, automatic tunnel setup for testing behind firewalls using BrowserStack Local or Sauce Connect, and test artifact collection including video recordings, network logs, and console output. Results are aggregated into unified reports with pass/fail status per browser-OS combination.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-cloud-executor/)
