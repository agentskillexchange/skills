---
title: "Puppeteer Cookie Consent Handler"
description: "Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns."
verification: "security_reviewed"
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Cookie Consent Handler

Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/puppeteer-cookie-consent-handler-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/puppeteer-cookie-consent-handler-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/)
