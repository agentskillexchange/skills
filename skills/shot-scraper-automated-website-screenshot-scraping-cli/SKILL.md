---
title: "shot-scraper Automated Website Screenshot and Scraping CLI"
description: "shot-scraper is a Python CLI tool by Simon Willison for taking automated screenshots of websites and executing JavaScript against pages. Built on Playwright, it supports headless browser automation, multi-step screenshot workflows defined in YAML, and HTML-to-image rendering for CI pipelines and monitoring."
slug: "shot-scraper-automated-website-screenshot-scraping-cli"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/simonw/shot-scraper"
tool_ecosystem:
  github_repo: "simonw/shot-scraper"
  github_stars: 2311
---

# shot-scraper Automated Website Screenshot and Scraping CLI

shot-scraper is a Python CLI tool by Simon Willison for taking automated screenshots of websites and executing JavaScript against pages. Built on Playwright, it supports headless browser automation, multi-step screenshot workflows defined in YAML, and HTML-to-image rendering for CI pipelines and monitoring.

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
clawhub install shot-scraper-automated-website-screenshot-scraping-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

shot-scraper is a command-line utility built by Simon Willison that uses Playwright to take automated screenshots of websites and extract data by executing JavaScript against web pages. It is designed for developers, testers, and content creators who need repeatable, scriptable browser automation without writing full test suites.
Core Capabilities
The tool supports single-page screenshots with customizable viewport dimensions, CSS selectors for capturing specific page elements, JavaScript execution to interact with or extract data from pages, and multi-step workflows defined in YAML files. It can authenticate against websites that require login, wait for specific page states, and handle complex single-page applications.
Screenshot Automation
Run shot-scraper https://example.com to capture a full-page screenshot. Use --selector to target specific DOM elements, --width and --height to set viewport dimensions, and --javascript to execute scripts before capture. The shot-scraper multi command reads a YAML file defining multiple screenshots to take in sequence.
Data Extraction
Beyond screenshots, shot-scraper can execute arbitrary JavaScript against pages and return the results. This makes it useful for scraping data from JavaScript-heavy websites, extracting rendered content, testing page behavior, and monitoring visual changes over time.
Installation
Install via pip: pip install shot-scraper, then run shot-scraper install to download the Playwright browser binaries. The tool runs on Python 3.8+ and works on Linux, macOS, and Windows.
CI/CD Integration
shot-scraper integrates well with GitHub Actions and other CI systems for automated visual regression testing, documentation screenshot generation, and site monitoring. Its YAML-driven multi-shot mode makes it easy to maintain screenshot libraries that update automatically when pages change.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shot-scraper-automated-website-screenshot-scraping-cli/)
