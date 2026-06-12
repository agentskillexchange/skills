---
name: "Monitor cross-platform trends and alert agents with TrendRadar"
slug: "monitor-cross-platform-trends-and-alert-agents-with-trendradar"
description: "Use TrendRadar when an operator needs a self-hosted trend monitor that filters multi-platform feeds, summarizes signals with AI, sends alerts, and exposes trend analysis through MCP."
github_stars: 59359
verification: "security_reviewed"
source: "https://github.com/sansan0/TrendRadar"
author: "sansan0"
publisher_type: "open_source"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "sansan0/TrendRadar"
  github_stars: 59359
---

# Monitor cross-platform trends and alert agents with TrendRadar

Use TrendRadar when an operator needs a self-hosted trend monitor that filters multi-platform feeds, summarizes signals with AI, sends alerts, and exposes trend analysis through MCP.

## Prerequisites

Docker or Python runtime, TrendRadar configuration, notification channel credentials, optional model credentials, MCP-capable client

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/sansan0/TrendRadar.git
- docker compose pull
- docker compose up -d
- docker compose pull trendradar

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/wantcat/trendradar?style=flat-square&logo=docker&logoColor=white&label=TrendRadar%20Pulls&color=2496ED)](https://hub.docker.com/r/wantcat/trendradar)
- [![Docker Pulls](https://img.shields.io/docker/pulls/wantcat/trendradar-mcp?style=flat-square&logo=docker&logoColor=white&label=MCP%20Pulls&color=2496ED)](https://hub.docker.com/r/wantcat/trendradar-mcp)
- [![Docker](https://img.shields.io/badge/Docker-部署-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/wantcat/trendradar)

Basic usage or getting-started notes:
- EMAIL_TO="user1@example.com,user2@example.com,user3@example.com"
- 找到 **"Get Hot News"**(必须得是这个字)点进去，点击右侧的 **"Run workflow"** 按钮运行
- 点击 Run workflow 后需要刷新浏览器页面才能看到新的运行记录

- Source: https://github.com/sansan0/TrendRadar
- Extracted from upstream docs: https://raw.githubusercontent.com/sansan0/TrendRadar/HEAD/README.md

## Documentation

- https://sansan0.github.io/TrendRadar/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-cross-platform-trends-and-alert-agents-with-trendradar/)
