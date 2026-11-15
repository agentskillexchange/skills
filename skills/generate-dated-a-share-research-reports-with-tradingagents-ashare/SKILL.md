---
name: "Generate dated A-share research reports with TradingAgents-AShare"
slug: "generate-dated-a-share-research-reports-with-tradingagents-ashare"
description: "Submit a bounded A-share research job from OpenClaw, follow its status, and summarize the resulting analyst debate and risk report for human review."
verification: "security_reviewed"
source: "https://github.com/KylinMountain/TradingAgents-AShare/tree/main/skills/tradingagents-analysis"
author: "KylinMountain"
publisher_type: "Open Source"
category: "Research & Scraping"
framework: "OpenClaw"
---

# Generate dated A-share research reports with TradingAgents-AShare

Submit a bounded A-share research job from OpenClaw, follow its status, and summarize the resulting analyst debate and risk report for human review.

## Prerequisites

OpenClaw, Bash, curl, Python 3; Git for source installation; TradingAgents API token and configured backend/model access

## Installation

Install or set up from the source-backed instructions:

Install Bash, curl, Python 3 and Git. Obtain an API token from the official app Settings / API Tokens page, and configure the service and its model access as documented upstream. Install the upstream skill into the OpenClaw workspace: git clone --depth 1 https://github.com/KylinMountain/TradingAgents-AShare.git mkdir -p ~/.openclaw/workspace/skills/tradingagents-analysis cp -R TradingAgents-AShare/skills/tradingagents-analysis/. ~/.openclaw/workspace/skills/tradingagents-analysis/ Set TRADINGAGENTS_TOKEN through the runtime secret/environment configuration. Explicitly set TRADINGAGENTS_API_URL=https://api.510168.xyz for the official hosted API, or to a trusted self-hosted backend. The app.510168.xyz URL is the web UI. Do not put tokens in prompts or committed files. For self-hosting, follow the repository Docker deployment guide, set a private TA_APP_SECRET_KEY, persist backend data, and configure model access. New/modified upstream components use PolyForm Noncommercial 1.0.0; check LICENSE before commercial deployment.

- Source: https://github.com/KylinMountain/TradingAgents-AShare/tree/main/skills/tradingagents-analysis

## Documentation

- https://github.com/KylinMountain/TradingAgents-AShare/blob/main/skills/tradingagents-analysis/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-dated-a-share-research-reports-with-tradingagents-ashare/)
