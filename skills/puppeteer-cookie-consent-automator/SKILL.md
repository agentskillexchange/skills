---
name: Puppeteer Cookie Consent Automator
description: Automatically detects and handles cookie consent banners across websites
  using Puppeteer CDP protocol and a trained classifier. Supports OneTrust, Cookiebot,
  and TrustArc consent management platforms.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-cookie-consent-automator/)
