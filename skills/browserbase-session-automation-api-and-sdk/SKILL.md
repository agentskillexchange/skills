---
name: "Browserbase Session Automation API and SDK"
description: "Use Browserbase when an agent needs hosted browser sessions, remote automation, session recording, and scalable browser infrastructure without managing Chromium fleets directly. This skill packages the Browserbase API and SDK into a concrete workflow for running, monitoring, and extracting results from cloud browser sessions."
verification: security_reviewed
source: "https://github.com/browserbase/sdk-node"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "browserbase/sdk-node"
  github_stars: 61
  ase_npm_package: "@browserbasehq/sdk"
  npm_weekly_downloads: 778552
---

# Browserbase Session Automation API and SDK

Browserbase provides a hosted browser automation platform for teams that want real browser control without maintaining their own Playwright or Chromium infrastructure. A skill built around the Browserbase Session Automation API and SDK is well suited to tasks such as remote web testing, browser-backed data extraction, authenticated workflow execution, and queued automation jobs that need session IDs, logs, or recordings.
The skill would typically create and manage Browserbase sessions through the official SDK, launch a browser context, run automation steps, and return artifacts such as HTML, screenshots, PDFs, traces, console logs, or extracted structured data. It can also coordinate retries, session cleanup, concurrency limits, and post-run summaries. When paired with an agent, Browserbase becomes a reliable execution layer for jobs like purchase-flow validation, compliance checks, back-office portal automation, or recurring website monitoring.
Important integration points include the Browserbase API, SDK authentication, Playwright-compatible browser control, remote session metadata, recording and replay, and webhook or queue-based orchestration. Relevant technical terms include session lifecycle, browser context, remote debugging, API tokens, trace capture, automation pipeline, and artifact storage. This makes the skill specific and practical: it does not merely say “automate a website,” it teaches an agent how to use Browserbase as the underlying hosted browser runtime and what outputs to capture for downstream systems.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserbase-session-automation-api-and-sdk/)
