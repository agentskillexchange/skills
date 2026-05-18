---
name: "Twitter/X Trend Monitor & Thread Publisher"
slug: "twitter-x-trend-monitor-thread-publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
github_stars: 74154
verification: "listed"
source: "https://github.com/redis/redis"
category: "Templates & Workflows"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "redis/redis"
  github_stars: 74154
---

# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -d -p 6379:6379 redis:latest
- cmake --version
- make -j "$(nproc)" all
- brew update

Requirements and caveats from upstream:
- [**Official Redis Docker images (Alpine/Debian)**](https://hub.docker.com/_/redis)
- [**Python (redis-py)**](https://github.com/redis-developer/redis-starter-python)
- [**JavaScript (node-redis)**](https://github.com/redis-developer/redis-starter-js)

Basic usage or getting-started notes:
- This document serves as both a quick start guide to Redis and a detailed resource for building it from source.
- New to Redis? Start with [What is Redis](#what-is-redis) and [Getting Started](#getting-started)
- [Getting started](#getting-started)

- Source: https://github.com/redis/redis
- Extracted from upstream docs: https://raw.githubusercontent.com/redis/redis/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
