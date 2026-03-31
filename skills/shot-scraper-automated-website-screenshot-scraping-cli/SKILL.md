---
name: "shot-scraper Automated Website Screenshot and Scraping CLI"
description: "shot-scraper is a Python CLI tool by Simon Willison for taking automated screenshots of websites and executing JavaScript against pages. Built on Playwright, it supports headless browser automation, multi-step screenshot workflows defined in YAML, and HTML-to-image rendering for CI pipelines and monitoring."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/simonw/shot-scraper"
tool_ecosystem:
  tool: shot-scraper
  github_repo: simonw/shot-scraper
  github_stars: 2307
  license: Apache-2.0
  maintained: true
---
# shot-scraper Automated Website Screenshot and Scraping CLI

shot-scraper is a Python CLI tool by Simon Willison for taking automated screenshots of websites and executing JavaScript against pages. Built on Playwright, it supports headless browser automation, multi-step screenshot workflows defined in YAML, and HTML-to-image rendering for CI pipelines and monitoring.

## Overview

shot-scraper is a command-line utility built by Simon Willison that uses Playwright to take automated screenshots of websites and extract data by executing JavaScript against web pages. It is designed for developers, testers, and content creators who need repeatable, scriptable browser automation without writing full test suites.

Core Capabilities

The tool supports single-page screenshots with customizable viewport dimensions, CSS selectors for capturing specific page elements, JavaScript execution to interact with or extract data from pages, and multi-step workflows defined in YAML files. It can authenticate against websites that require login, wait for specific page states, and handle complex single-page applications.

Screenshot Automation

Run `shot-scraper https://example.com` to capture a full-page screenshot. Use `--selector` to target specific DOM elements, `--width` and `--height` to set viewport dimensions, and `--javascript` to execute scripts before capture. The `shot-scraper multi` command reads a YAML file defining multiple screenshots to take in sequence.

Data Extraction

Beyond screenshots, shot-scraper can execute arbitrary JavaScript against pages and return the results. This makes it useful for scraping data from JavaScript-heavy websites, extracting rendered content, testing page behavior, and monitoring visual changes over time.

Installation

Install via pip: `pip install shot-scraper`, then run `shot-scraper install` to download the Playwright browser binaries. The tool runs on Python 3.8+ and works on Linux, macOS, and Windows.

CI/CD Integration

shot-scraper integrates well with GitHub Actions and other CI systems for automated visual regression testing, documentation screenshot generation, and site monitoring. Its YAML-driven multi-shot mode makes it easy to maintain screenshot libraries that update automatically when pages change.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill shot-scraper-automated-website-screenshot-scraping-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill shot-scraper-automated-website-screenshot-scraping-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill shot-scraper-automated-website-screenshot-scraping-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill shot-scraper-automated-website-screenshot-scraping-cli -a codex
```

### OpenClaw

```bash
clawhub install shot-scraper-automated-website-screenshot-scraping-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shot-scraper-automated-website-screenshot-scraping-cli/)
