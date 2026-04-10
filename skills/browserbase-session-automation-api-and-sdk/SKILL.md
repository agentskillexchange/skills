---
title: "Browserbase Session Automation API and SDK"
description: "Use Browserbase when an agent needs hosted browser sessions, remote automation, session recording, and scalable browser infrastructure without managing Chromium fleets directly. This skill packages the Browserbase API and SDK into a concrete workflow for running, monitoring, and extracting results from cloud browser sessions."
slug: "browserbase-session-automation-api-and-sdk"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/browserbase/sdk-node"
tool_ecosystem:
  github_repo: "browserbase/sdk-node"
  github_stars: 61
  npm_package: "@browserbasehq/sdk"
  npm_weekly_downloads: 778552
listed: true
---

# Browserbase Session Automation API and SDK

Use Browserbase when an agent needs hosted browser sessions, remote automation, session recording, and scalable browser infrastructure without managing Chromium fleets directly. This skill packages the Browserbase API and SDK into a concrete workflow for running, monitoring, and extracting results from cloud browser sessions.

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
clawhub install browserbase-session-automation-api-and-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Browserbase provides a hosted browser automation platform for teams that want real browser control without maintaining their own Playwright or Chromium infrastructure. A skill built around the Browserbase Session Automation API and SDK is well suited to tasks such as remote web testing, browser-backed data extraction, authenticated workflow execution, and queued automation jobs that need session IDs, logs, or recordings.
The skill would typically create and manage Browserbase sessions through the official SDK, launch a browser context, run automation steps, and return artifacts such as HTML, screenshots, PDFs, traces, console logs, or extracted structured data. It can also coordinate retries, session cleanup, concurrency limits, and post-run summaries. When paired with an agent, Browserbase becomes a reliable execution layer for jobs like purchase-flow validation, compliance checks, back-office portal automation, or recurring website monitoring.
Important integration points include the Browserbase API, SDK authentication, Playwright-compatible browser control, remote session metadata, recording and replay, and webhook or queue-based orchestration. Relevant technical terms include session lifecycle, browser context, remote debugging, API tokens, trace capture, automation pipeline, and artifact storage. This makes the skill specific and practical: it does not merely say “automate a website,” it teaches an agent how to use Browserbase as the underlying hosted browser runtime and what outputs to capture for downstream systems.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-session-automation-api-and-sdk/)
