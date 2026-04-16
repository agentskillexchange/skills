---
title: "chromedp Go Browser Automation with Chrome DevTools Protocol"
description: "This skill turns chromedp into a repeatable browser automation workflow for Go teams. It covers navigation, DOM queries, screenshots, PDF capture, network-aware waits, and structured extraction through the Chrome DevTools Protocol."
verification: "security_reviewed"
source: "https://github.com/chromedp/chromedp"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "chromedp/chromedp"
  github_stars: 12900
  license: "MIT"
---

# chromedp Go Browser Automation with Chrome DevTools Protocol

chromedp is a high-level Go library for driving Chromium-based browsers through the Chrome DevTools Protocol (CDP). This skill packages chromedp into a practical workflow for teams that need browser automation inside Go services, test suites, data collection jobs, or internal tools. Instead of treating browser control as an isolated script, the skill frames chromedp as an application integration point: define a browser allocator, build a context tree with cancellation, compose chromedp.Tasks, and collect artifacts such as screenshots, PDFs, DOM snapshots, cookies, and extracted text or JSON.

The skill is useful for acceptance testing, authenticated page checks, scraping structured content, rendering pages to PDF, and automating browser-only admin flows. It explains how to use actions such as Navigate, WaitVisible, Click, SendKeys, Text, OuterHTML, Screenshot, and FullScreenshot, while also accounting for runtime concerns like timeouts, headless versus headed mode, network idleness, and cleanup of browser processes. For more advanced jobs, it can listen to CDP network and page events, evaluate JavaScript in-page, and coordinate extraction into typed Go structs.

Outputs typically include rendered files, JSON payloads, assertion results, or captured page state that can flow into CI pipelines, cron jobs, message queues, or observability systems. Integration points include Go HTTP services, background workers, GitHub Actions, Docker containers, and internal automation APIs. If the job depends on Chromium rendering, browser events, or authenticated session state, chromedp gives a Go-native way to do it without leaving the Go runtime.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chromedp-go-browser-automation-chrome-devtools-protocol/)
