---
name: "Use Dify for production agentic workflow apps"
slug: "use-dify-for-production-agentic-workflow-apps"
description: "Build, test, and operate agentic workflow apps in Dify when an operator needs a governed path from prototype to production."
github_stars: 143727
verification: "security_reviewed"
source: "https://github.com/langgenius/dify"
author: "langgenius"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "langgenius/dify"
  github_stars: 143727
---

# Use Dify for production agentic workflow apps

Build, test, and operate agentic workflow apps in Dify when an operator needs a governed path from prototype to production.

## Prerequisites

Docker, Docker Compose, Dify workspace, model provider credentials, optional observability integrations

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose up -d
- If you need to customize the configuration, edit docker/.env. The essential startup defaults live in [docker/.env.example](docker/.env.example), and optional advanced variables are split under docker/envs/ by theme. A...

Requirements and caveats from upstream:
- <a href="https://hub.docker.com/u/langgenius" target="_blank">
- <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/langgenius/dify-web?labelColor=%20%23FDB062&color=%20%23f79009"></a>
- The easiest way to start the Dify server is through [Docker Compose](docker/docker-compose.yaml). Before running Dify with the following commands, make sure that [Docker](https://docs.docker.com/get-docker/) and [Dock...

Basic usage or getting-started notes:
- Before installing Dify, make sure your machine meets the following minimum system requirements:
- CPU >= 2 Core
- RAM >= 4 GiB

- Source: https://github.com/langgenius/dify
- Extracted from upstream docs: https://raw.githubusercontent.com/langgenius/dify/HEAD/README.md

## Documentation

- https://docs.dify.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-dify-for-production-agentic-workflow-apps/)
