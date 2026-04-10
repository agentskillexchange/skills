---
name: Puppeteer Screenshot Diff Engine
description: Visual regression testing using Puppeteer page.screenshot() with pixelmatch
  comparison. Leverages CDP sessions via page.createCDPSession() for precise viewport
  emulation and network throttling.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-screenshot-diff-engine/
category:
- Browser Automation
framework:
- Claude Code
---
# Puppeteer Screenshot Diff Engine

The Puppeteer Screenshot Diff Engine automates visual regression testing by capturing page screenshots through Puppeteer's page.screenshot({ fullPage: true }) API and comparing them pixel-by-pixel using the pixelmatch library with configurable threshold values.
It establishes Chrome DevTools Protocol sessions via page.createCDPSession() to precisely control device emulation through Emulation.setDeviceMetricsOverride and simulate network conditions with Network.emulateNetworkConditions. This ensures screenshots are captured under reproducible conditions across CI runs.
The engine supports baseline management with automatic golden image updates, generates HTML diff reports highlighting changed regions with bounding boxes, and integrates with page.waitForSelector() and page.waitForNetworkIdle() to ensure pages are fully rendered before capture. It handles dynamic content by masking regions through CSS injection via page.addStyleTag().

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-screenshot-diff-engine/)
