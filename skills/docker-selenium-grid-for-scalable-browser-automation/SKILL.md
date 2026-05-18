---
name: "Docker Selenium Grid for Scalable Browser Automation"
slug: "docker-selenium-grid-for-scalable-browser-automation"
description: "docker-selenium packages Selenium Grid into ready-to-run container images for Chrome, Firefox, Edge, and distributed browser execution. It is useful when an agent needs reproducible browser automation infrastructure for testing, scraping, QA, or parallel session orchestration."
github_stars: 8619
verification: "listed"
source: "https://github.com/SeleniumHQ/docker-selenium"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SeleniumHQ/docker-selenium"
  github_stars: 8619
---

# Docker Selenium Grid for Scalable Browser Automation

docker-selenium packages Selenium Grid into ready-to-run container images for Chrome, Firefox, Edge, and distributed browser execution. It is useful when an agent needs reproducible browser automation infrastructure for testing, scraping, QA, or parallel session orchestration.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.43.0-20260404
- $ docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium/standalone-chromium:latest
- make set_containerd_image_store
- Noted: That command is only compatible with Ubuntu. For users use Docker Desktop on macOS, it can be enabled easily via

Requirements and caveats from upstream:
- [![Build & test](https://github.com/SeleniumHQ/docker-selenium/actions/workflows/build-test.yml/badge.svg)](https://github.com/SeleniumHQ/docker-selenium/actions/workflows/build-test.yml)
- [![Deploys](https://github.com/SeleniumHQ/docker-selenium/actions/workflows/deploy.yml/badge.svg)](https://github.com/SeleniumHQ/docker-selenium/actions/workflows/deploy.yml)
- [![Release Charts](https://github.com/SeleniumHQ/docker-selenium/actions/workflows/helm-chart-release.yml/badge.svg)](https://github.com/SeleniumHQ/docker-selenium/actions/workflows/helm-chart-release.yml)

Basic usage or getting-started notes:
- [Quick start](#quick-start)
- [Configuration example](#configuration-example)
- bash

- Source: https://github.com/SeleniumHQ/docker-selenium
- Extracted from upstream docs: https://raw.githubusercontent.com/SeleniumHQ/docker-selenium/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-selenium-grid-for-scalable-browser-automation/)
