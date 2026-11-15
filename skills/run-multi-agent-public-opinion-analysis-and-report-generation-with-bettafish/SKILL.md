---
name: "Run multi-agent public opinion analysis and report generation with BettaFish"
slug: "run-multi-agent-public-opinion-analysis-and-report-generation-with-bettafish"
description: "Collect public discussion, coordinate specialist agents, and generate an evidence-backed public opinion report from one conversational analysis request."
github_stars: 41383
verification: "security_reviewed"
source: "https://github.com/666ghj/BettaFish"
author: "666ghj"
publisher_type: "individual"
category: "Research & Scraping"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "666ghj/BettaFish"
  github_stars: 41383
---

# Run multi-agent public opinion analysis and report generation with BettaFish

Collect public discussion, coordinate specialist agents, and generate an evidence-backed public opinion report from one conversational analysis request.

## Prerequisites

Python 3.9+, Docker Compose or Python environment, PostgreSQL or MySQL, Playwright Chromium, OpenAI-compatible LLM credentials, public/private data sources configured in .env

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose up -d
- conda create -n your_conda_name python=3.11
- conda activate your_conda_name
- uv venv --python 3.11 # 创建3.11环境

Requirements and caveats from upstream:
- [![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)
- ├── docker-compose.yml # Docker多服务编排配置
- **注：镜像拉取速度慢**，在原 docker-compose.yml 文件中，我们已经通过**注释**的方式提供了备用镜像地址供您替换

Basic usage or getting-started notes:
- ├── .env.example # 环境变量示例文件
- 复制一份 .env.example 文件，命名为 .env ，并按需配置 .env 文件中的环境变量

- Source: https://github.com/666ghj/BettaFish
- Extracted from upstream docs: https://raw.githubusercontent.com/666ghj/BettaFish/HEAD/README.md

## Documentation

- https://github.com/666ghj/BettaFish/blob/main/README-EN.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-agent-public-opinion-analysis-and-report-generation-with-bettafish/)
