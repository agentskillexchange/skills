---
title: "Govern agent skills, MCP servers, prompts, and tool calls with DefenseClaw"
slug: "govern-agent-skills-mcp-servers-prompts-and-tool-calls-with-defenseclaw"
description: "Use DefenseClaw as an operator-controlled admission, runtime guardrail, sandbox, and audit layer before untrusted agent capabilities run."
github_stars: 647
verification: "security_reviewed"
source: "https://github.com/cisco-ai-defense/defenseclaw"
author: "Cisco AI Defense"
publisher_type: "vendor"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cisco-ai-defense/defenseclaw"
  github_stars: 647
---

# Govern agent skills, MCP servers, prompts, and tool calls with DefenseClaw

Use DefenseClaw as an operator-controlled admission, runtime guardrail, sandbox, and audit layer before untrusted agent capabilities run.

## Prerequisites

DefenseClaw CLI, Go gateway sidecar, policy rules, optional OpenClaw plugin, optional OTLP/Splunk/webhook sinks

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream install and quick-start docs for the Python CLI and gateway sidecar, run initial health/setup checks, scan candidate skills or MCP servers in observe mode first, then enable action-mode blocking only after policy review.
```

## Documentation

- https://cisco-ai-defense.github.io/docs/defenseclaw

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/govern-agent-skills-mcp-servers-prompts-and-tool-calls-with-defenseclaw/)
