---
name: "Gatus Endpoint Monitoring and Status Page Platform"
slug: "gatus-endpoint-monitoring-status-page-platform"
description: "Gatus is an open source uptime and endpoint monitoring platform built for developers and ops teams. It checks HTTP, TCP, ICMP, and DNS targets, evaluates conditions like status codes or response times, and can route alerts to systems such as Slack, PagerDuty, Discord, and Twilio."
github_stars: 10652
verification: "listed"
source: "https://github.com/TwiN/gatus"
author: "TwiN"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "twin/gatus"
  github_stars: 10652
---

# Gatus Endpoint Monitoring and Status Page Platform

Gatus is an open source uptime and endpoint monitoring platform built for developers and ops teams. It checks HTTP, TCP, ICMP, and DNS targets, evaluates conditions like status codes or response times, and can route alerts to systems such as Slack, PagerDuty, Discord, and Twilio.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 8080:8080 --name gatus ghcr.io/twin/gatus:stable
- You can also use Docker Hub if you prefer:
- docker run -p 8080:8080 --name gatus twinproduction/gatus:stable
- Make sure you have the ability to use ses:SendEmail.

Requirements and caveats from upstream:
- [![Docker pulls](https://img.shields.io/docker/pulls/twinproduction/gatus.svg)](https://cloud.docker.com/repository/docker/twinproduction/gatus)
- [Docker](#docker)
- **Low resource consumption**: As with most Go applications, the resource footprint that this application requires is negligibly small.

Basic usage or getting-started notes:
- <summary><b>Quick start</b></summary>
- For more details, see [Usage](#usage)
- [Usage](#usage)

- Source: https://github.com/TwiN/gatus
- Extracted from upstream docs: https://raw.githubusercontent.com/TwiN/gatus/HEAD/README.md

## Documentation

- https://gatus.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gatus-endpoint-monitoring-status-page-platform/)
