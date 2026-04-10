---
title: "Playwright Network HAR Recorder"
description: "Records and replays HTTP Archive (HAR) files using Playwright routeFromHAR API for deterministic test environments. Supports selective recording, response modification, and API mock generation."
slug: "playwright-network-har-recorder"
category:
  - "Browser Automation"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-network-har-recorder/"
listed: true
---

# Playwright Network HAR Recorder

Records and replays HTTP Archive (HAR) files using Playwright routeFromHAR API for deterministic test environments. Supports selective recording, response modification, and API mock generation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install playwright-network-har-recorder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Playwright Network HAR Recorder captures and replays network traffic as HTTP Archive (HAR) files using Playwright’s built-in routeFromHAR and recordHar APIs. This enables deterministic test environments by replacing live API calls with recorded responses.
Recording mode captures all network traffic with configurable filters by URL pattern, content type, or request method. The HAR file includes request/response headers, bodies, timing data, and TLS certificate information. Sensitive data can be automatically redacted using configurable patterns for auth tokens, API keys, and PII fields.
Replay mode uses routeFromHAR to intercept matching requests and serve recorded responses, with fallback strategies for unmatched requests (pass-through, abort, or custom response). Response modification enables dynamic updates to recorded data — injecting test-specific values, simulating error responses, or adjusting timestamps to prevent stale data issues.
API mock generation converts HAR recordings into standalone mock server configurations compatible with MSW (Mock Service Worker), WireMock, and Playwright’s native route handlers. The skill includes HAR file comparison tools for detecting API contract changes between recordings, useful for consumer-driven contract testing workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-har-recorder/)
