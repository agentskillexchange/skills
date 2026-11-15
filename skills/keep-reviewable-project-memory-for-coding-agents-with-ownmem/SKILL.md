---
name: "Keep reviewable project memory for coding agents with OwnMem"
slug: "keep-reviewable-project-memory-for-coding-agents-with-ownmem"
description: "Initialize Git-native project memory that Claude Code, Codex, Cursor, Gemini CLI, and compatible coding agents can recall deterministically."
github_stars: 200
verification: "security_reviewed"
source: "https://github.com/grpcer/ownmem"
author: "grpcer"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "grpcer/ownmem"
  github_stars: 200
  npm_package: "ownmem"
  npm_weekly_downloads: 361
---

# Keep reviewable project memory for coding agents with OwnMem

Initialize Git-native project memory that Claude Code, Codex, Cursor, Gemini CLI, and compatible coding agents can recall deterministically.

## Prerequisites

Node.js 20.6 or newer, npm/npx, OwnMem package, target repository, selected coding-agent hosts

## Installation

Install or set up from the source-backed instructions:

From the repository that should own memory, run `npm install --save-dev ownmem` and then `npx ownmem init --locale auto --hosts claude,codex --layers dashboard --hook`; adjust `--hosts` for Claude Code, Codex, Cursor, or Gemini CLI as needed.

- Source: https://github.com/grpcer/ownmem

## Documentation

- https://github.com/grpcer/ownmem

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-reviewable-project-memory-for-coding-agents-with-ownmem/)
