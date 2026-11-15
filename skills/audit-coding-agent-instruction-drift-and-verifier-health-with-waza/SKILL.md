---
name: "Audit coding-agent instruction drift and verifier health with Waza"
slug: "audit-coding-agent-instruction-drift-and-verifier-health-with-waza"
description: "Run a bounded, report-only audit of coding-agent settings, instruction reachability, hooks, MCP wiring, and verification evidence with actionable findings."
github_stars: 7307
verification: "security_reviewed"
source: "https://github.com/tw93/Waza"
author: "Tw93"
publisher_type: "community"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tw93/Waza"
  github_stars: 7307
  npm_package: "@tw93/waza"
  npm_weekly_downloads: 0
---

# Audit coding-agent instruction drift and verifier health with Waza

Run a bounded, report-only audit of coding-agent settings, instruction reachability, hooks, MCP wiring, and verification evidence with actionable findings.

## Prerequisites

SKILL.md-compatible coding agent; Node.js/npx for skills installation or supported host plugin; Bash and trusted Python 3 for complete collector coverage; project-local read access

## Installation

Install or set up from the source-backed instructions:

Install skills: npx skills add tw93/Waza -a claude-code codex cursor -g -y. Invoke the installed health skill by name and request instructions-only scope when session history is out of scope. Claude Code plugin alternative: /plugin marketplace add tw93/Waza then /plugin install waza@waza; invoke /waza:health. Codex plugin alternative: codex plugin marketplace add tw93/Waza then codex plugin add waza@waza. Read the installed health/SKILL.md and use its collector launcher; no optional persistent rules or statusline setup is required.

- Source: https://github.com/tw93/Waza

## Documentation

- https://github.com/tw93/Waza/blob/main/skills/health/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-coding-agent-instruction-drift-and-verifier-health-with-waza/)
