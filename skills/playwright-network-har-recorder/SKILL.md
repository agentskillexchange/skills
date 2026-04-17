---
title: "Playwright Network HAR Recorder"
description: "Records and replays HTTP Archive (HAR) files using Playwright routeFromHAR API for deterministic test environments. Supports selective recording, response modification, and API mock generation."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
category:
  - "Browser Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
  license: "Apache-2.0"
---

# Playwright Network HAR Recorder

The Playwright Network HAR Recorder captures and replays network traffic as HTTP Archive (HAR) files using Playwright’s built-in routeFromHAR and recordHar APIs. This enables deterministic test environments by replacing live API calls with recorded responses.

Recording mode captures all network traffic with configurable filters by URL pattern, content type, or request method. The HAR file includes request/response headers, bodies, timing data, and TLS certificate information. Sensitive data can be automatically redacted using configurable patterns for auth tokens, API keys, and PII fields.

Replay mode uses routeFromHAR to intercept matching requests and serve recorded responses, with fallback strategies for unmatched requests (pass-through, abort, or custom response). Response modification enables dynamic updates to recorded data — injecting test-specific values, simulating error responses, or adjusting timestamps to prevent stale data issues.

API mock generation converts HAR recordings into standalone mock server configurations compatible with MSW (Mock Service Worker), WireMock, and Playwright’s native route handlers. The skill includes HAR file comparison tools for detecting API contract changes between recordings, useful for consumer-driven contract testing workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-network-har-recorder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-network-har-recorder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-har-recorder/)
