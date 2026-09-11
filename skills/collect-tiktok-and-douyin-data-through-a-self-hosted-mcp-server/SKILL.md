---
name: "Collect TikTok and Douyin data through a self-hosted MCP server"
slug: "collect-tiktok-and-douyin-data-through-a-self-hosted-mcp-server"
description: "Run Douyin_TikTok_Download_API as a private MCP-backed service so agents can parse, archive, and retrieve TikTok or Douyin posts, authors, comments, search results, and media."
github_stars: 20068
verification: "security_reviewed"
source: "https://github.com/Evil0ctal/Douyin_TikTok_Download_API"
author: "Evil0ctal"
publisher_type: "independent"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "Evil0ctal/Douyin_TikTok_Download_API"
  github_stars: 20068
---

# Collect TikTok and Douyin data through a self-hosted MCP server

Run Douyin_TikTok_Download_API as a private MCP-backed service so agents can parse, archive, and retrieve TikTok or Douyin posts, authors, comments, search results, and media.

## Prerequisites

Docker, Docker Compose, Douyin_TikTok_Download_API, PostgreSQL and Redis from the compose stack, MCP-compatible client or REST/CLI access

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/Evil0ctal/Douyin_TikTok_Download_API, change into the repo, copy .env.example to .env, set DTK_SECRET_KEY and any required deployment settings, then run COMPOSE_ENV_FILES=.env docker compose -p dtk -f docker/compose.yml up -d. Open http://localhost:8000 to finish setup, create an API key, and follow the MCP documentation at https://douyin.wtf/mcp/ to connect the agent client to the self-hosted instance.

- Source: https://github.com/Evil0ctal/Douyin_TikTok_Download_API

## Documentation

- https://douyin.wtf

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/collect-tiktok-and-douyin-data-through-a-self-hosted-mcp-server/)
