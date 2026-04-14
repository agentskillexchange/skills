---
title: "Puppeteer Browser Automation Library for Chrome and Firefox"
description: "Uses Puppeteer to control Chrome and Firefox through the DevTools Protocol or WebDriver BiDi for screenshots, PDF generation, scraping, and browser workflow automation. Best when you want a well-known JavaScript automation library with straightforward installation and deep control over browser pages."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94016
---

# Puppeteer Browser Automation Library for Chrome and Firefox

Puppeteer Browser Automation Library for Chrome and Firefox is built around the official Puppeteer project published at puppeteer/puppeteer. Puppeteer provides a high-level JavaScript API for controlling browsers over the DevTools Protocol and, in newer flows, WebDriver BiDi. The upstream install guide shows the primary package command, explains the difference between puppeteer and puppeteer-core, and documents how the standard package downloads a compatible Chrome for Testing binary automatically.

The main job-to-be-done here is dependable scripted browser control in environments where an agent or automation task needs to open pages, wait for application state, capture screenshots, print PDFs, extract rendered content, or perform authenticated UI workflows. This is especially useful for test harnesses, internal scraping tools, QA helpers, regression checks, and content pipelines that need a browser with JavaScript enabled rather than a simple HTTP fetch. Common integration points include Node.js applications, CI jobs, web monitoring scripts, screenshot services, and headless browser workers that connect to remote or managed browser infrastructure.

This skill differs from generic “web scraping” abstractions because Puppeteer exposes page-level automation primitives directly: browser launch and connection, viewport control, DOM interaction, locator-based actions, page events, screenshots, PDF generation, and remote browser connections. It is a real, well-maintained upstream project with a public docs site, Apache-2.0 licensing, active releases, and a large adoption footprint on GitHub. That combination gives it enough evidence and adoption to pass the intake gate and be published as verified metadata rather than a speculative listing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-browser-automation-library-for-chrome-and-firefox/)
