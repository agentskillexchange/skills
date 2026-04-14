---
title: "Playwright Extra Browser Automation Plugins"
description: "Playwright Extra adds a plugin layer on top of Microsoft Playwright so agents can reuse stealth, CAPTCHA handling, and custom browser hooks instead of wiring those capabilities by hand. It is useful when browser automations need anti-bot evasions or shared middleware across Chromium sessions."
verification: security_reviewed
source: "https://github.com/berstend/puppeteer-extra/tree/master/packages/playwright-extra"
category:
  - "Browser Automation"
---

# Playwright Extra Browser Automation Plugins

Playwright Extra adds a plugin layer on top of Microsoft Playwright so agents can reuse stealth, CAPTCHA handling, and custom browser hooks instead of wiring those capabilities by hand. It is useful when browser automations need anti-bot evasions or shared middleware across Chromium sessions.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-extra-browser-automation-plugins/)
