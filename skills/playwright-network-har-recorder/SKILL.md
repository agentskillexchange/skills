---
title: Playwright Network HAR Recorder
description: The Playwright Network HAR Recorder captures and replays network traffic
  as HTTP Archive (HAR) files using Playwright’s built-in routeFromHAR and recordHar
  APIs. This enables deterministic test environments by replacing live API calls with
  recorded responses. Recording mode captures all network traffic with configurable
  filters by URL pattern, content type, or request method. The HAR file includes request/response
  headers, bodies, timing data, and TLS certificate information. Sensitive data can
  be automatically redacted using configurable patterns for auth tokens, API keys,
  and PII fields. Replay mode uses routeFromHAR to intercept matching requests and
  serve recorded responses, with fallback strategies for unmatched requests (pass-through,
  abort, or custom response). Response modification enables dynamic updates to recorded
  data — injecting test-specific values, simulating error responses, or adjusting
  timestamps to prevent stale data issues. API mock generation converts HAR recordings
  into standalone mock server configurations compatible with MSW (Mock Service Worker),
  WireMock, and Playwright’s native route handlers. The skill includes HAR file comparison
  tools for detecting API contract changes between recordings, useful for consumer-driven
  contract testing workflows.
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-network-har-recorder/
category:
- Browser Automation
framework:
- Codex
---

# Playwright Network HAR Recorder

The Playwright Network HAR Recorder captures and replays network traffic as HTTP Archive (HAR) files using Playwright’s built-in routeFromHAR and recordHar APIs. This enables deterministic test environments by replacing live API calls with recorded responses. Recording mode captures all network traffic with configurable filters by URL pattern, content type, or request method. The HAR file includes request/response headers, bodies, timing data, and TLS certificate information. Sensitive data can be automatically redacted using configurable patterns for auth tokens, API keys, and PII fields. Replay mode uses routeFromHAR to intercept matching requests and serve recorded responses, with fallback strategies for unmatched requests (pass-through, abort, or custom response). Response modification enables dynamic updates to recorded data — injecting test-specific values, simulating error responses, or adjusting timestamps to prevent stale data issues. API mock generation converts HAR recordings into standalone mock server configurations compatible with MSW (Mock Service Worker), WireMock, and Playwright’s native route handlers. The skill includes HAR file comparison tools for detecting API contract changes between recordings, useful for consumer-driven contract testing workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-har-recorder/)
