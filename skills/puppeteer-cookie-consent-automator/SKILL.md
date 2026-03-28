---
name: "Puppeteer Cookie Consent Automator"
description: "Automatically detects and handles cookie consent banners across websites using Puppeteer CDP protocol and a trained classifier. Supports OneTrust, Cookiebot, and TrustArc consent management platforms."
category: "Browser Automation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
tool_ecosystem:
  tool: puppeteer
  github_stars: 93932
  npm_weekly_downloads: 8696130
  github_repo: puppeteer/puppeteer
  license: Apache-2.0
  maintained: true
---

# Puppeteer Cookie Consent Automator

Automatically detects and handles cookie consent banners across websites using Puppeteer CDP protocol and a trained classifier. Supports OneTrust, Cookiebot, and TrustArc consent management platforms.

## Overview

The Puppeteer Cookie Consent Automator navigates websites via Puppeteer using the Chrome DevTools Protocol and automatically identifies and interacts with cookie consent banners. It maintains a detection library covering major consent management platforms including OneTrust, Cookiebot, TrustArc, and Quantcast Choice. Detection uses a combination of DOM selector matching, iframe content analysis, and text classification to identify consent dialogs regardless of implementation approach. The agent supports configurable consent strategies: accept all, reject all, accept necessary only, or custom category selection. For each consent interaction, it logs the consent state, categories accepted, and cookie changes before and after consent using the CDP Network.getCookies endpoint. Shadow DOM traversal handles consent banners embedded in web component shadow roots. The tool integrates with compliance auditing workflows by verifying that cookie behavior matches declared cookie policies. Batch mode processes URL lists for large-scale consent compliance scanning.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-automator -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-cookie-consent-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-cookie-consent-automator/
