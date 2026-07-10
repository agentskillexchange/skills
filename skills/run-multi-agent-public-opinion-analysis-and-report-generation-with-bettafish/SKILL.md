---
title: "Run multi-agent public opinion analysis and report generation with BettaFish"
description: "Collect public discussion, coordinate specialist agents, and generate an evidence-backed public opinion report from one conversational analysis request."
verification: "security_reviewed"
source: "https://github.com/666ghj/BettaFish"
author: "666ghj"
publisher_type: "individual"
category:
  - "Research & Scraping"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "666ghj/BettaFish"
  github_stars: 41383
---

# Run multi-agent public opinion analysis and report generation with BettaFish

Collect public discussion, coordinate specialist agents, and generate an evidence-backed public opinion report from one conversational analysis request.

## Prerequisites

Python 3.9+, Docker Compose or Python environment, PostgreSQL or MySQL, Playwright Chromium, OpenAI-compatible LLM credentials, public/private data sources configured in .env

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For Docker, clone the repository, configure database and LLM settings, then run `docker compose up -d`. For source startup, create a Python 3.11 environment, install `requirements.txt`, run `playwright install chromium`, copy `.env.example` to `.env`, fill database and OpenAI-compatible LLM settings, then launch the documented Flask application.
```

## Documentation

- https://github.com/666ghj/BettaFish/blob/main/README-EN.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-agent-public-opinion-analysis-and-report-generation-with-bettafish/)
