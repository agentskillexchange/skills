---
name: "Puppeteer Cookie Consent Handler"
description: "Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns."
category: "Browser Automation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/"
---
# Puppeteer Cookie Consent Handler

Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-handler-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-handler-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-handler-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-cookie-consent-handler-3 -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-cookie-consent-handler-3
```

## Details

Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/)
