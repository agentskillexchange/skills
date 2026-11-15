---
name: "Run Suede Creator Skills across Codex and Claude Code workflows"
slug: "run-suede-creator-skills-across-codex-and-claude-code-workflows"
description: "Install Suede Creator Skills when an agent needs repeatable Codex, Claude Code, or MCP-backed workflows for orchestration, code review, ship gates, AI evals, design, copy, SEO, app packaging, creator rights, and recovery audits."
github_stars: 166
verification: "security_reviewed"
source: "https://github.com/JasonColapietro/suede-creator-skills"
author: "Jason Colapietro"
publisher_type: "Individual Developer"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "JasonColapietro/suede-creator-skills"
  github_stars: 166
---

# Run Suede Creator Skills across Codex and Claude Code workflows

Install Suede Creator Skills when an agent needs repeatable Codex, Claude Code, or MCP-backed workflows for orchestration, code review, ship gates, AI evals, design, copy, SEO, app packaging, creator rights, and recovery audits.

## Prerequisites

Codex CLI or Claude Code, Git, shell access, optional Node.js for the Suede Skills MCP server

## Installation

Install or set up from the source-backed instructions:

For Codex, run `codex plugin marketplace add JasonColapietro/suede-creator-skills --ref main` and then `codex plugin add suede-skills@suede-codex`, then restart Codex. For Claude Code, clone `https://github.com/JasonColapietro/suede-creator-skills` and run `bash install.sh`, or copy selected `skills/` folders into the appropriate Claude skills directory after review. For MCP discovery and QA, run `node mcp/suede-skills-mcp.mjs --profile all` from the repository.

- Source: https://github.com/JasonColapietro/suede-creator-skills

## Documentation

- https://jasoncolapietro.github.io/suede-creator-skills/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-suede-creator-skills-across-codex-and-claude-code-workflows/)
