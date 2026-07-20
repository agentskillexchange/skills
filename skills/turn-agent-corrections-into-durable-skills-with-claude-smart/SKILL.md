---
name: "Turn Agent Corrections Into Durable Skills With claude-smart"
slug: "turn-agent-corrections-into-durable-skills-with-claude-smart"
description: "Use claude-smart to capture corrections and working patterns as preferences, project skills, and shared skills that Claude Code, Codex, and OpenCode reuse later."
github_stars: 748
verification: "security_reviewed"
source: "https://github.com/ReflexioAI/claude-smart"
author: "Yi Lu / ReflexioAI"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ReflexioAI/claude-smart"
  github_stars: 748
  npm_package: "claude-smart"
  npm_weekly_downloads: 1890
---

# Turn Agent Corrections Into Durable Skills With claude-smart

Use claude-smart to capture corrections and working patterns as preferences, project skills, and shared skills that Claude Code, Codex, and OpenCode reuse later.

## Prerequisites

Node.js 20+, npx, target host CLI on PATH such as claude, codex, or opencode; learned local data under ~/.reflexio/ and ~/.claude-smart/

## Installation

Use the upstream install or setup path that matches your environment:
- **Learning:** “for this repo, always use pnpm dev:all to start the full local stack — npm run dev only starts the frontend and causes missing service errors”

Requirements and caveats from upstream:
- <img src="https://img.shields.io/badge/python-%3E%3D3.12-brightgreen.svg" alt="Python">
- <img src="https://img.shields.io/badge/node-%3E%3D20-brightgreen.svg" alt="Node">
- *Example:* Claude spends several iterations trying to start the local dev environment before discovering that this repo requires pnpm dev:all instead of the usual npm run dev.<br>

Basic usage or getting-started notes:
- <a href="#quick-start">Quick Start</a> •
- *Example:* a deploy fails after Claude bumps prisma from 5.x to 6.0; you tell it to roll back because 6.0 breaks nested writes in your order flow.<br>
- **Memory:** “user mentioned that npm run dev did not work”<br>

- Source: https://github.com/ReflexioAI/claude-smart
- Extracted from upstream docs: https://raw.githubusercontent.com/ReflexioAI/claude-smart/HEAD/README.md

## Documentation

- https://www.reflexio.ai/docs/claude-smart

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-agent-corrections-into-durable-skills-with-claude-smart/)
