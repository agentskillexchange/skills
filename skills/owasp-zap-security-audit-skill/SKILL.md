---
title: OWASP ZAP Security Audit Skill
description: Wraps OWASP ZAP API for automated web application security testing including
  active scan, spider crawl, and ajax spider endpoints. Generates structured findings
  reports with CWE classifications and OWASP Top 10 category mapping. Overview This
  skill provides automated integration capabilities designed for production agent
  workflows. It handles authentication, rate limiting, and error recovery out of the
  box, allowing agents to focus on high-level task orchestration rather than low-level
  API management. Key Features Automatic retry logic with exponential backoff for
  API rate limits Structured output formatting compatible with downstream agent pipelines
  Comprehensive error handling with actionable diagnostic messages Configurable caching
  layer to reduce redundant API calls Usage Install via the Agent Skill Exchange registry
  and configure with your API credentials. The skill exposes a standardized interface
  that works across supported agent frameworks, with framework-specific optimizations
  applied automatically during initialization.
verification: security_reviewed
source: https://agentskillexchange.com/skills/owasp-zap-security-audit-skill/
category:
- Security &amp; Verification
framework:
- Claude Code
---

# OWASP ZAP Security Audit Skill

Wraps OWASP ZAP API for automated web application security testing including active scan, spider crawl, and ajax spider endpoints. Generates structured findings reports with CWE classifications and OWASP Top 10 category mapping. Overview This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management. Key Features Automatic retry logic with exponential backoff for API rate limits Structured output formatting compatible with downstream agent pipelines Comprehensive error handling with actionable diagnostic messages Configurable caching layer to reduce redundant API calls Usage Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-audit-skill/)
