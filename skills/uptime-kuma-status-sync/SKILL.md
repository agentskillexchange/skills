---
name: "Uptime Kuma Status Sync"
slug: "uptime-kuma-status-sync"
description: "Interfaces with the Uptime Kuma Socket.IO API to monitor service health checks. Syncs status page data to Statuspage.io via Atlassian REST API and triggers incident workflows in Rootly."
github_stars: 85583
verification: "security_reviewed"
source: "https://github.com/louislam/uptime-kuma"
author: "Louis Lam"
category: "Monitoring & Alerts"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "louislam/uptime-kuma"
  github_stars: 85583
---

# Uptime Kuma Status Sync

Interfaces with the Uptime Kuma Socket.IO API to monitor service health checks. Syncs status page data to Statuspage.io via Atlassian REST API and triggers incident workflows in Rootly.

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose up -d
- docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
- docker run ... -p 127.0.0.1:3001:3001 ...
- git clone https://github.com/louislam/uptime-kuma.git

Requirements and caveats from upstream:
- <a target="_blank" href="https://github.com/louislam/uptime-kuma"><img src="https://img.shields.io/github/stars/louislam/uptime-kuma?style=flat" /></a> <a target="_blank" href="https://hub.docker.com/r/louislam/uptime...
- Monitoring uptime for HTTP(s) / TCP / HTTP(s) Keyword / HTTP(s) Json Query / Websocket / Ping / DNS Record / Push / Steam Game Server / Docker Containers
- ### 🐳 Docker Compose

Basic usage or getting-started notes:
- Platform
- ✅ Major Linux distros such as Debian, Ubuntu, Fedora and ArchLinux etc.
- ✅ Windows 10 (x64), Windows Server 2012 R2 (x64) or higher

- Source: https://github.com/louislam/uptime-kuma
- Extracted from upstream docs: https://raw.githubusercontent.com/louislam/uptime-kuma/HEAD/README.md

## Documentation

- https://uptimekuma.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-status-sync/)
