---
title: "Playwright Network HAR Recorder"
description: "The Playwright Network HAR Recorder captures and replays network traffic as HTTP Archive (HAR) files using Playwright&#8217;s built-in routeFromHAR and recordHar APIs. This enables deterministic test environments by replacing live API calls with recorded responses. Recording mode captures all network traffic with configurable filters by URL pattern, content type, or request method. The HAR file includes request/response headers, bodies, timing data, and TLS certificate information. Sensitive data can be automatically redacted using configurable patterns for auth tokens, API keys, and PII fields. Replay mode uses routeFromHAR to intercept matching requests and serve recorded responses, with fallback strategies for unmatched requests (pass-through, abort, or custom response). Response modification enables dynamic updates to recorded data — injecting test-specific values, simulating error responses, or adjusting timestamps to prevent stale data issues. API mock generation converts HAR recordings into standalone mock server configurations compatible with MSW (Mock Service Worker), WireMock, and Playwright&#8217;s native route handlers. The skill includes HAR file comparison tools for detecting API contract changes between recordings, useful for consumer-driven contract testing workflows."
source: "https://github.com/microsoft/playwright"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright Network HAR Recorder

The Playwright Network HAR Recorder captures and replays network traffic as HTTP Archive (HAR) files using Playwright&#8217;s built-in routeFromHAR and recordHar APIs. This enables deterministic test environments by replacing live API calls with recorded responses. Recording mode captures all network traffic with configurable filters by URL pattern, content type, or request method. The HAR file includes request/response headers, bodies, timing data, and TLS certificate information. Sensitive data can be automatically redacted using configurable patterns for auth tokens, API keys, and PII fields. Replay mode uses routeFromHAR to intercept matching requests and serve recorded responses, with fallback strategies for unmatched requests (pass-through, abort, or custom response). Response modification enables dynamic updates to recorded data — injecting test-specific values, simulating error responses, or adjusting timestamps to prevent stale data issues. API mock generation converts HAR recordings into standalone mock server configurations compatible with MSW (Mock Service Worker), WireMock, and Playwright&#8217;s native route handlers. The skill includes HAR file comparison tools for detecting API contract changes between recordings, useful for consumer-driven contract testing workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-har-recorder/)
