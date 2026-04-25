---
title: "CDP Network Interception Logger"
description: "Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived events to intercept, log, and modify HTTP traffic during browser automation. Exports HAR files compatible with Charles Proxy and supports request/response body modification."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cdp-network-interception-logger/"
category:
  - "Browser Automation"
framework:
  - "Codex"
---

# CDP Network Interception Logger

Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived events to intercept, log, and modify HTTP traffic during browser automation. Exports HAR files compatible with Charles Proxy and supports request/response body modification. This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cdp-network-interception-logger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cdp-network-interception-logger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cdp-network-interception-logger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cdp-network-interception-logger/)
