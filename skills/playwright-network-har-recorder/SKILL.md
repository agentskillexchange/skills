---
name: Playwright Network HAR Recorder
description: Records and replays HTTP Archive (HAR) files using Playwright routeFromHAR
  API for deterministic test environments. Supports selective recording, response
  modification, and API mock generation.
category: Browser Automation
framework: Codex
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-network-har-recorder/"
---
# Playwright Network HAR Recorder

Records and replays HTTP Archive (HAR) files using Playwright routeFromHAR API for deterministic test environments. Supports selective recording, response modification, and API mock generation.

The Playwright Network HAR Recorder captures and replays network traffic as HTTP Archive (HAR) files using Playwright’s built-in routeFromHAR and recordHar APIs. This enables deterministic test environments by replacing live API calls with recorded responses.

Recording mode captures all network traffic with configurable filters by URL pattern, content type, or request method. The HAR file includes request/response headers, bodies, timing data, and TLS certificate information. Sensitive data can be automatically redacted using configurable patterns for auth tokens, API keys, and PII fields.

Replay mode uses routeFromHAR to intercept matching requests and serve recorded responses, with fallback strategies for unmatched requests (pass-through, abort, or custom response). Response modification enables dynamic updates to recorded data — injecting test-specific values, simulating error responses, or adjusting timestamps to prevent stale data issues.

API mock generation converts HAR recordings into standalone mock server configurations compatible with MSW (Mock Service Worker), WireMock, and Playwright’s native route handlers. The skill includes HAR file comparison tools for detecting API contract changes between recordings, useful for consumer-driven contract testing workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-network-har-recorder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-network-har-recorder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-network-har-recorder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-network-har-recorder -a codex
```

### OpenClaw

```bash
clawhub install playwright-network-har-recorder
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-har-recorder/)
