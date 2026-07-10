---
name: "changedetection.io Self-Hosted Website Change Monitoring Platform"
slug: "changedetection-io-website-change-monitor"
description: "changedetection.io is an open-source, self-hosted tool for monitoring websites for content changes, price drops, restock alerts, and defacement detection. It supports visual selectors, browser automation via Playwright, and delivers notifications through Discord, Slack, Telegram, email, webhooks, and dozens more channels."
github_stars: 30867
verification: "security_reviewed"
source: "https://github.com/dgtlmoon/changedetection.io"
category: "Research & Scraping"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dgtlmoon/changedetection.io"
  github_stars: 30867
---

# changedetection.io Self-Hosted Website Change Monitoring Platform

changedetection.io is an open-source, self-hosted tool for monitoring websites for content changes, price drops, restock alerts, and defacement detection. It supports visual selectors, browser automation via Playwright, and delivers notifications through Discord, Slack, Telegram, email, webhooks, and dozens more channels.

## Installation

Use the upstream install or setup path that matches your environment:
- $ docker compose up -d
- Docker standalone
- $ docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io dgtlmoon/changedetection.io
- docker pull dgtlmoon/changedetection.io

Requirements and caveats from upstream:
- [![Release Version][release-shield]][release-link] [![Docker Pulls][docker-pulls]][docker-link] [![License][license-shield]](LICENSE.md)
- Requires Playwright to be enabled.
- ### Docker

Basic usage or getting-started notes:
- Works with any model you already pay for — GPT-4o-mini and Gemini Flash handle this well at fractions of a cent per check. Or run it entirely locally with **Ollama**, **vLLM**, **LM Studio**, or any **OpenAI-compatibl...
- After **Browser Steps** have been run, then visit the **Visual Selector** tab to refine the content you're interested in.
- ### Example use cases

- Source: https://github.com/dgtlmoon/changedetection.io
- Extracted from upstream docs: https://raw.githubusercontent.com/dgtlmoon/changedetection.io/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/changedetection-io-website-change-monitor/)
