---
title: Puppeteer Cookie Consent Handler
description: Detects and dismisses cookie consent banners across websites using Puppeteer
  page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports
  IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns. This skill integrates
  with production-grade tooling to streamline automation workflows. It handles edge
  cases such as timeout management, retry logic with exponential backoff, and detailed
  error reporting. Configuration is managed through environment variables and YAML
  config files, supporting both local development and CI/CD pipeline environments.
  The skill outputs structured JSON logs compatible with ELK stack and Datadog for
  observability. It includes built-in rate limiting to respect API quotas and implements
  proper credential rotation using vault-based secret management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/
category:
- Browser Automation
framework:
- Claude Code
---

# Puppeteer Cookie Consent Handler

Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns. This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/)
