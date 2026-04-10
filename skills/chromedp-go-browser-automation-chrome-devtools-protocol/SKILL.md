---
title: "chromedp Go Browser Automation with Chrome DevTools Protocol"
description: "This skill turns chromedp into a repeatable browser automation workflow for Go teams. It covers navigation, DOM queries, screenshots, PDF capture, network-aware waits, and structured extraction through the Chrome DevTools Protocol."
slug: "chromedp-go-browser-automation-chrome-devtools-protocol"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/chromedp/chromedp"
tool_ecosystem:
  github_repo: "chromedp/chromedp"
  github_stars: 12900
---

# chromedp Go Browser Automation with Chrome DevTools Protocol

This skill turns chromedp into a repeatable browser automation workflow for Go teams. It covers navigation, DOM queries, screenshots, PDF capture, network-aware waits, and structured extraction through the Chrome DevTools Protocol.

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
clawhub install chromedp-go-browser-automation-chrome-devtools-protocol
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

chromedp is a high-level Go library for driving Chromium-based browsers through the Chrome DevTools Protocol (CDP). This skill packages chromedp into a practical workflow for teams that need browser automation inside Go services, test suites, data collection jobs, or internal tools. Instead of treating browser control as an isolated script, the skill frames chromedp as an application integration point: define a browser allocator, build a context tree with cancellation, compose chromedp.Tasks, and collect artifacts such as screenshots, PDFs, DOM snapshots, cookies, and extracted text or JSON.
The skill is useful for acceptance testing, authenticated page checks, scraping structured content, rendering pages to PDF, and automating browser-only admin flows. It explains how to use actions such as Navigate, WaitVisible, Click, SendKeys, Text, OuterHTML, Screenshot, and FullScreenshot, while also accounting for runtime concerns like timeouts, headless versus headed mode, network idleness, and cleanup of browser processes. For more advanced jobs, it can listen to CDP network and page events, evaluate JavaScript in-page, and coordinate extraction into typed Go structs.
Outputs typically include rendered files, JSON payloads, assertion results, or captured page state that can flow into CI pipelines, cron jobs, message queues, or observability systems. Integration points include Go HTTP services, background workers, GitHub Actions, Docker containers, and internal automation APIs. If the job depends on Chromium rendering, browser events, or authenticated session state, chromedp gives a Go-native way to do it without leaving the Go runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chromedp-go-browser-automation-chrome-devtools-protocol/)
