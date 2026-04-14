---
title: "Puppeteer Cookie Consent Handler"
description: "Detects and dismisses cookie consent banners across websites using Puppeteer page.evaluate selectors and the CMP (Consent Management Platform) protocol. Supports IAB TCF v2.0 consent strings and GDPR/CCPA banner patterns."
verification: security_reviewed
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-handler-3/)
