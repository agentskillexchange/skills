---
name: "A/B test agent skills and MCP changes with Caliper"
slug: "ab-test-agent-skills-mcp-changes-with-caliper"
description: "Use Caliper to run real agent tasks with and without a skill, MCP server, or rule change so reliability and token cost are measurable."
github_stars: 175
verification: "security_reviewed"
source: "https://github.com/edonadei/caliper"
author: "edonadei"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "edonadei/caliper"
  github_stars: 175
---

# A/B test agent skills and MCP changes with Caliper

Use Caliper to run real agent tasks with and without a skill, MCP server, or rule change so reliability and token cost are measurable.

## Prerequisites

Python 3.10+, Caliper CLI, target agent runtime such as Claude Code, Codex, Pi, or Hermes, skills or MCP servers under test

## Installation

Install or set up from the source-backed instructions:

Install the CLI with `pipx install caliper-eval` for direct runs, or add the agent skill with `npx skills@latest add edonadei/caliper`; then create an `.eval.yaml`, run `caliper run ... --k 3`, run an ablated control with `--ablate`, and compare results with `caliper compare`.

- Source: https://github.com/edonadei/caliper

## Documentation

- https://github.com/edonadei/caliper

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ab-test-agent-skills-mcp-changes-with-caliper/)
