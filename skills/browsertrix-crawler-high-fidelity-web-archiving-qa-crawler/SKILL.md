---
title: "Browsertrix Crawler High-Fidelity Web Archiving and QA Crawler"
description: "Browsertrix Crawler is a browser-based crawling system from Webrecorder for high-fidelity site capture, QA replay analysis, and configurable crawl behavior. It runs complex crawls in a single Docker container and uses Puppeteer plus Chrome DevTools Protocol under the hood."
slug: "browsertrix-crawler-high-fidelity-web-archiving-qa-crawler"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/webrecorder/browsertrix-crawler"
tool_ecosystem:
  github_repo: "webrecorder/browsertrix-crawler"
  github_stars: 1013
listed: true
---

# Browsertrix Crawler High-Fidelity Web Archiving and QA Crawler

Browsertrix Crawler is a browser-based crawling system from Webrecorder for high-fidelity site capture, QA replay analysis, and configurable crawl behavior. It runs complex crawls in a single Docker container and uses Puppeteer plus Chrome DevTools Protocol under the hood.

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
clawhub install browsertrix-crawler-high-fidelity-web-archiving-qa-crawler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Browsertrix Crawler is the open-source crawling engine behind Webrecorder’s Browsertrix platform. The upstream webrecorder/browsertrix-crawler repository describes it as a high-fidelity browser-based crawling system designed to run complex, customizable crawls in a single Docker container. Instead of only fetching raw HTML, Browsertrix Crawler uses Puppeteer to drive Brave Browser windows and captures site behavior through the Chrome DevTools Protocol, which makes it useful for modern JavaScript-heavy sites and archival-quality capture.
The official documentation highlights features that matter for agent workflows: YAML-based crawl configuration, seed lists and scope rules, blocking rules, screenshots and thumbnails, browser profile reuse, custom Puppeteer driver scripts, real-time screencasting, and quality-assurance crawling that compares replay results against captured content. This makes the tool useful not only for scraping, but also for preservation, auditing, and repeatable site QA tasks where a lightweight HTTP crawler would miss rendered behavior.
As an ASE skill, Browsertrix Crawler fits jobs such as capturing a public site into archival artifacts, validating replay completeness, running scoped multi-page crawls with browser behavior enabled, or producing screenshots and crawl reports from reproducible YAML configurations. Its outputs can include crawl packages, screenshots, QA statistics, and browser-derived capture results. Integration points include Docker-based automation, archiving pipelines, custom Puppeteer behavior scripts, and research or compliance workflows that need browser-accurate capture rather than simple HTML extraction.
The project has an active GitHub repository, official documentation, an open-source license, and recent maintenance activity. For teams that need browser-realistic crawling with reproducible configuration, it fills a distinct role inside the research and scraping category.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browsertrix-crawler-high-fidelity-web-archiving-qa-crawler/)
