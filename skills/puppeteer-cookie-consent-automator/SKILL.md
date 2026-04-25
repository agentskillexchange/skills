---
title: "Puppeteer Cookie Consent Automator"
description: "Automatically detects and handles cookie consent banners across websites using Puppeteer CDP protocol and a trained classifier. Supports OneTrust, Cookiebot, and TrustArc consent management platforms."
verification: "security_reviewed"
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Cookie Consent Automator

The Puppeteer Cookie Consent Automator navigates websites via Puppeteer using the Chrome DevTools Protocol and automatically identifies and interacts with cookie consent banners. It maintains a detection library covering major consent management platforms including OneTrust, Cookiebot, TrustArc, and Quantcast Choice. Detection uses a combination of DOM selector matching, iframe content analysis, and text classification to identify consent dialogs regardless of implementation approach. The agent supports configurable consent strategies: accept all, reject all, accept necessary only, or custom category selection. For each consent interaction, it logs the consent state, categories accepted, and cookie changes before and after consent using the CDP Network.getCookies endpoint. Shadow DOM traversal handles consent banners embedded in web component shadow roots. The tool integrates with compliance auditing workflows by verifying that cookie behavior matches declared cookie policies. Batch mode processes URL lists for large-scale consent compliance scanning.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/puppeteer-cookie-consent-automator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/puppeteer-cookie-consent-automator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/puppeteer-cookie-consent-automator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-automator/)
