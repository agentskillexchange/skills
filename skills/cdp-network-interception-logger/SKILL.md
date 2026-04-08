---
title: CDP Network Interception Logger
description: Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived
  events to intercept, log, and modify HTTP traffic during browser automation. Exports
  HAR files compatible with Charles Proxy and supports request/response body modification.
  This skill integrates with production-grade tooling to streamline automation workflows.
  It handles edge cases such as timeout management, retry logic with exponential backoff,
  and detailed error reporting. Configuration is managed through environment variables
  and YAML config files, supporting both local development and CI/CD pipeline environments.
  The skill outputs structured JSON logs compatible with ELK stack and Datadog for
  observability. It includes built-in rate limiting to respect API quotas and implements
  proper credential rotation using vault-based secret management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cdp-network-interception-logger/
category:
- Browser Automation
framework:
- Codex
---

# CDP Network Interception Logger

Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived events to intercept, log, and modify HTTP traffic during browser automation. Exports HAR files compatible with Charles Proxy and supports request/response body modification. This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cdp-network-interception-logger/)
