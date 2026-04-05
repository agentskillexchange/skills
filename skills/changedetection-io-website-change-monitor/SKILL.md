---
name: "changedetection.io Self-Hosted Website Change Monitoring Platform"
description: "changedetection.io is an open-source, self-hosted tool for monitoring websites for content changes, price drops, restock alerts, and defacement detection. It supports visual selectors, browser automation via Playwright, and delivers notifications through Discord, Slack, Telegram, email, webhooks, and dozens more channels."
category: "Research & Scraping"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/dgtlmoon/changedetection.io"
tool_ecosystem:
  tool: changedetection.io
  github_repo: dgtlmoon/changedetection.io
  github_stars: 30867
---
# changedetection.io Self-Hosted Website Change Monitoring Platform

changedetection.io is an open-source, self-hosted tool for monitoring websites for content changes, price drops, restock alerts, and defacement detection. It supports visual selectors, browser automation via Playwright, and delivers notifications through Discord, Slack, Telegram, email, webhooks, and dozens more channels.

## Overview

changedetection.io is a powerful open-source website change detection and monitoring platform written in Python. With over 30,000 GitHub stars and active development, it has become the leading self-hosted solution for tracking changes across web pages.

Core Capabilities

The tool crawls specified URLs on a configurable schedule and compares page content against previous snapshots to detect changes. It supports both simple text-based diffing and advanced visual comparison through its Playwright-powered browser content fetcher. Users can define CSS selectors, XPath expressions, or JSONPath filters to target specific sections of a page, ensuring precise monitoring without noise from irrelevant layout changes.

Browser Automation and Interaction

changedetection.io includes a Browser Steps feature that allows users to define pre-fetch interactions such as logging into authenticated pages, clicking cookie consent banners, filling form fields, navigating paginated content, and adding items to shopping carts before capturing the monitored content. This makes it suitable for monitoring behind-login dashboards, dynamic single-page applications, and JavaScript-rendered content.

Price and Restock Monitoring

A dedicated price and restock detection mode parses HTML meta-data and structured data from product pages to extract pricing information. Agents can track product price history, set threshold alerts for price drops, and receive restock notifications when out-of-stock items become available again.

Notification Integrations

The platform integrates with over 90 notification channels via the Apprise library, including Discord, Slack, Telegram, Microsoft Teams, Pushover, Ntfy, email (SMTP), generic webhooks, and many more. Notifications include the diff of what changed, making it easy to triage updates without visiting the monitored page.

Agent Integration

For AI agent workflows, changedetection.io exposes a REST API that allows programmatic management of watches, retrieval of change history, and triggering of on-demand checks. Agents can create monitoring jobs, poll for changes, and parse structured diff output to drive downstream automation such as competitive intelligence gathering, content compliance auditing, or dynamic pricing responses.

Deployment

The recommended deployment method is Docker, with a single command to get started. The platform stores data in a local datastore volume and runs a lightweight web UI for configuration and review. It can also be deployed alongside a Playwright fetcher container for full browser rendering support.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill changedetection-io-website-change-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill changedetection-io-website-change-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill changedetection-io-website-change-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill changedetection-io-website-change-monitor -a codex
```

### OpenClaw

```bash
clawhub install changedetection-io-website-change-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/changedetection-io-website-change-monitor/)
