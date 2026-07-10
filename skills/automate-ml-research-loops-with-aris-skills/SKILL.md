---
name: "Automate ML research loops with ARIS skills"
slug: "automate-ml-research-loops-with-aris-skills"
description: "Use ARIS to run Markdown-based agent skills for literature review, idea discovery, cross-model critique, experiment planning, and paper-writing support."
github_stars: 9609
verification: "security_reviewed"
source: "https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep"
author: "wanshuiyin"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "wanshuiyin/Auto-claude-code-research-in-sleep"
  github_stars: 9609
---

# Automate ML research loops with ARIS skills

Use ARIS to run Markdown-based agent skills for literature review, idea discovery, cross-model critique, experiment planning, and paper-writing support.

## Prerequisites

ARIS skills or ARIS-Code CLI, Claude Code/Codex/OpenClaw-compatible agent, configured model providers

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep.git
- npm install -g @openai/codex
- pip install deepxiv-sdk
- pip install exa-py

Requirements and caveats from upstream:
- 🪶 **Radically lightweight — zero dependencies, zero lock-in.** The entire system is plain Markdown files. No framework to learn, no database to maintain, no Docker to configure, no daemon to babysit. Every skill is a...
- **2026-04-03** — ☁️ **[Modal serverless GPU](skills/serverless-modal/SKILL.md)** — no GPU? gpu: modal in CLAUDE.md, one command (modal run launcher.py), no SSH, no Docker, auto scale-to-zero. **$30/month free tier** —...

Basic usage or getting-started notes:
- **v0.4.10** (2026-05-17) — Stream + MCP reliability + multi-provider pricing. C6 whole-stream restart in Anthropic MessageStream + OpenAI SSE loop on chunk decode failure / premature EOF (ARIS_STREAM_RETRY, default 2,...
- 🌙 **Let Claude Code do research while you sleep.** Wake up to find your paper scored, weaknesses identified, experiments run, and narrative rewritten — autonomously.
- Custom [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills for autonomous ML research workflows. These skills orchestrate **cross-model collaboration** — Claude Code drives the research while an exter...

- Source: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- Extracted from upstream docs: https://raw.githubusercontent.com/wanshuiyin/Auto-claude-code-research-in-sleep/HEAD/README.md

## Documentation

- https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automate-ml-research-loops-with-aris-skills/)
