---
name: "Regression-test coding agents and skills with Coder Eval"
slug: "regression-test-coding-agents-and-skills-with-coder-eval"
description: "Run sandboxed YAML evaluation suites against Claude Code, Codex, Gemini, OpenCode, or Pi agents, then gate CI on task scores and skill-trigger checks."
github_stars: 151
verification: "security_reviewed"
source: "https://github.com/UiPath/coder_eval"
author: "UiPath"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "UiPath/coder_eval"
  github_stars: 151
---

# Regression-test coding agents and skills with Coder Eval

Run sandboxed YAML evaluation suites against Claude Code, Codex, Gemini, OpenCode, or Pi agents, then gate CI on task scores and skill-trigger checks.

## Prerequisites

Python 3.13+, uv or pip, at least one supported coding-agent runtime such as Claude Code, Codex, Gemini Antigravity, OpenCode, or Pi, model credentials or existing agent login, optional GitHub Actions runner

## Installation

Install or set up from the source-backed instructions:

Install with uv tool install coder-eval, or uv tool install coder-eval[codex,antigravity] for bundled agent extras. Define or reuse YAML tasks, run coder-eval plan, coder-eval run, and coder-eval report locally or through the documented GitHub Action.

- Source: https://github.com/UiPath/coder_eval

## Documentation

- https://coder-eval.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regression-test-coding-agents-and-skills-with-coder-eval/)
