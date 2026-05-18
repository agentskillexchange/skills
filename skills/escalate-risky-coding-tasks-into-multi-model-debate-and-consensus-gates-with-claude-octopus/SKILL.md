---
name: "Escalate risky coding tasks into multi-model debate and consensus gates with Claude Octopus"
slug: "escalate-risky-coding-tasks-into-multi-model-debate-and-consensus-gates-with-claude-octopus"
description: "Use Claude Octopus when ordinary Claude Code flows are not enough and a risky coding task needs adversarial multi-model review, disagreement surfacing, and a consensus gate before shipping."
github_stars: 2806
verification: "listed"
source: "https://github.com/nyldn/claude-octopus"
author: "nyldn"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "nyldn/claude-octopus"
  github_stars: 2806
---

# Escalate risky coding tasks into multi-model debate and consensus gates with Claude Octopus

Use Claude Octopus when ordinary Claude Code flows are not enough and a risky coding task needs adversarial multi-model review, disagreement surfacing, and a consensus gate before shipping.

## Prerequisites

Claude Code; optional additional model providers such as Codex, Gemini, Copilot, Qwen, Ollama, Perplexity, or OpenRouter

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @openai/codex @google/gemini-cli @qwen-code/qwen-code 2>/dev/null || true
- npm install github:nyldn/claude-octopus#main --prefix openclaw

Requirements and caveats from upstream:
- <img src="https://img.shields.io/badge/Claude_Code-v2.1.14+_required-blueviolet" alt="Requires Claude Code v2.1.14+">
- Provider API calls require internet access from the hosted environment.
- "command": "node",

Basic usage or getting-started notes:
- For scheduled Claude Code tasks, run /octo:sentinel for triage and /octo:security for recurring audits. Keep jobs read-only by default and route fixes through /octo:debug, /octo:review, or /octo:embrace after triage.
- | Reduce token usage | /octo:doctor (includes RTK install + token tips) |
- | Just run something quick | /octo:quick |

- Source: https://github.com/nyldn/claude-octopus
- Extracted from upstream docs: https://raw.githubusercontent.com/nyldn/claude-octopus/HEAD/README.md

## Documentation

- https://github.com/nyldn/claude-octopus

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/escalate-risky-coding-tasks-into-multi-model-debate-and-consensus-gates-with-claude-octopus/)
