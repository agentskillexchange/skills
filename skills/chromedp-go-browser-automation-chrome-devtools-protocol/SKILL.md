---
title: "chromedp Go Browser Automation with Chrome DevTools Protocol"
description: "This skill turns chromedp into a repeatable browser automation workflow for Go teams. It covers navigation, DOM queries, screenshots, PDF capture, network-aware waits, and structured extraction through the Chrome DevTools Protocol."
verification: security_reviewed
source: "https://github.com/chromedp/chromedp"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "chromedp/chromedp"
  github_stars: 12900
---

# chromedp Go Browser Automation with Chrome DevTools Protocol

chromedp is a high-level Go library for driving Chromium-based browsers through the Chrome DevTools Protocol (CDP). This skill packages chromedp into a practical workflow for teams that need browser automation inside Go services, test suites, data collection jobs, or internal tools. Instead of treating browser control as an isolated script, the skill frames chromedp as an application integration point: define a browser allocator, build a context tree with cancellation, compose chromedp.Tasks, and collect artifacts such as screenshots, PDFs, DOM snapshots, cookies, and extracted text or JSON.

The skill is useful for acceptance testing, authenticated page checks, scraping structured content, rendering pages to PDF, and automating browser-only admin flows. It explains how to use actions such as Navigate, WaitVisible, Click, SendKeys, Text, OuterHTML, Screenshot, and FullScreenshot, while also accounting for runtime concerns like timeouts, headless versus headed mode, network idleness, and cleanup of browser processes. For more advanced jobs, it can listen to CDP network and page events, evaluate JavaScript in-page, and coordinate extraction into typed Go structs.

Outputs typically include rendered files, JSON payloads, assertion results, or captured page state that can flow into CI pipelines, cron jobs, message queues, or observability systems. Integration points include Go HTTP services, background workers, GitHub Actions, Docker containers, and internal automation APIs. If the job depends on Chromium rendering, browser events, or authenticated session state, chromedp gives a Go-native way to do it without leaving the Go runtime.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chromedp-go-browser-automation-chrome-devtools-protocol/)
