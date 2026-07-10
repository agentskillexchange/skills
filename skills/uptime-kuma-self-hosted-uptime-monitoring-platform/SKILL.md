---
name: "Uptime Kuma Self-Hosted Uptime Monitoring Platform"
slug: "uptime-kuma-self-hosted-uptime-monitoring-platform"
description: "Uptime Kuma is an open source uptime monitor for HTTP, TCP, ping, DNS, Docker, and keyword checks. It gives agents a concrete way to create, update, and review monitors, incidents, notifications, and public status pages from a self-hosted monitoring stack."
github_stars: 85143
verification: "security_reviewed"
source: "https://github.com/louislam/uptime-kuma"
author: "louislam"
publisher_type: "Open Source Project"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "louislam/uptime-kuma"
  github_stars: 85143
  npm_package: "uptime-kuma"
  npm_weekly_downloads: 97
---

# Uptime Kuma Self-Hosted Uptime Monitoring Platform

Uptime Kuma is an open source uptime monitor for HTTP, TCP, ping, DNS, Docker, and keyword checks. It gives agents a concrete way to create, update, and review monitors, incidents, notifications, and public status pages from a self-hosted monitoring stack.

## Prerequisites

node.js, npm, bun, docker, docker compose, go

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

- https://github.com/louislam/uptime-kuma/blob/master/CONTRIBUTING.md#can-i-create-a-pull-request-for-uptime-kuma

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-self-hosted-uptime-monitoring-platform/)
