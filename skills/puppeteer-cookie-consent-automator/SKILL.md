---
title: Puppeteer Cookie Consent Automator
description: 'The Puppeteer Cookie Consent Automator navigates websites via Puppeteer
  using the Chrome DevTools Protocol and automatically identifies and interacts with
  cookie consent banners. It maintains a detection library covering major consent
  management platforms including OneTrust, Cookiebot, TrustArc, and Quantcast Choice.
  Detection uses a combination of DOM selector matching, iframe content analysis,
  and text classification to identify consent dialogs regardless of implementation
  approach. The agent supports configurable consent strategies: accept all, reject
  all, accept necessary only, or custom category selection. For each consent interaction,
  it logs the consent state, categories accepted, and cookie changes before and after
  consent using the CDP Network.getCookies endpoint. Shadow DOM traversal handles
  consent banners embedded in web component shadow roots. The tool integrates with
  compliance auditing workflows by verifying that cookie behavior matches declared
  cookie policies. Batch mode processes URL lists for large-scale consent compliance
  scanning.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-cookie-consent-automator/
category:
- Browser Automation
framework:
- Custom Agents
---

# Puppeteer Cookie Consent Automator

The Puppeteer Cookie Consent Automator navigates websites via Puppeteer using the Chrome DevTools Protocol and automatically identifies and interacts with cookie consent banners. It maintains a detection library covering major consent management platforms including OneTrust, Cookiebot, TrustArc, and Quantcast Choice. Detection uses a combination of DOM selector matching, iframe content analysis, and text classification to identify consent dialogs regardless of implementation approach. The agent supports configurable consent strategies: accept all, reject all, accept necessary only, or custom category selection. For each consent interaction, it logs the consent state, categories accepted, and cookie changes before and after consent using the CDP Network.getCookies endpoint. Shadow DOM traversal handles consent banners embedded in web component shadow roots. The tool integrates with compliance auditing workflows by verifying that cookie behavior matches declared cookie policies. Batch mode processes URL lists for large-scale consent compliance scanning.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-automator/)
