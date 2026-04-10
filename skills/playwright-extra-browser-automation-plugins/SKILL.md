---
name: "Playwright Extra Browser Automation Plugins"
description: "Playwright Extra adds a plugin layer on top of Microsoft Playwright so agents can reuse stealth, CAPTCHA handling, and custom browser hooks instead of wiring those capabilities by hand. It is useful when browser automations need anti-bot evasions or shared middleware across Chromium sessions."
verification: security_reviewed
source: "https://github.com/berstend/puppeteer-extra/tree/master/packages/playwright-extra"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
---

# Playwright Extra Browser Automation Plugins

Playwright Extra is a community-maintained extension package for Playwright that brings the plugin model from the puppeteer-extra ecosystem to modern browser automation. The core package, playwright-extra, wraps the standard Playwright browser launch flow and lets you register plugins before creating browser instances. In practice that means an agent can keep using familiar Playwright APIs while adding cross-cutting behavior such as stealth evasions, custom request instrumentation, or CAPTCHA solving integrations.
The package is especially useful for web research and browser workflow automation where plain Playwright gets blocked or needs repetitive setup code. A common integration pattern is to import chromium from playwright-extra, register puppeteer-extra-plugin-stealth or other compatible plugins, and then launch as usual. Because it sits close to the browser lifecycle, the tool can affect page creation, headers, fingerprinting surfaces, and network behavior without forcing an agent to rewrite each automation script.
Upstream evidence is strong: the package is published on npm, the source lives in the berstend/puppeteer-extra GitHub repository, and the repo includes an MIT license and tagged releases. For agent builders, this makes Playwright Extra a practical way to standardize browser automation middleware across scraping, login automation, QA flows, and repeated web tasks that need more resilience than stock Playwright provides.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-extra-browser-automation-plugins/)
