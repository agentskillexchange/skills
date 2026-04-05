---
name: "CDP Network Interception Logger"
description: "Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived events to intercept, log, and modify HTTP traffic during browser automation. Exports HAR files compatible with Charles Proxy and supports request/response body modification."
category: "Browser Automation"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cdp-network-interception-logger/"
---
# CDP Network Interception Logger

Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived events to intercept, log, and modify HTTP traffic during browser automation. Exports HAR files compatible with Charles Proxy and supports request/response body modification.

Uses Chrome DevTools Protocol Fetch.requestPaused and Network.responseReceived events to intercept, log, and modify HTTP traffic during browser automation. Exports HAR files compatible with Charles Proxy and supports request/response body modification.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cdp-network-interception-logger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cdp-network-interception-logger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cdp-network-interception-logger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cdp-network-interception-logger -a codex
```

### OpenClaw

```bash
clawhub install cdp-network-interception-logger
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cdp-network-interception-logger/)
