---
title: "Apply rule-based guardrails to agent traces and tool flows with Invariant"
description: "Insert a trace-aware guardrail layer between agents and their tools so unsafe message patterns or tool-call sequences are blocked by explicit rules."
verification: "security_reviewed"
source: "https://github.com/invariantlabs-ai/invariant"
author: "Invariant Labs"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "invariantlabs-ai/invariant"
  github_stars: 409
  npm_package: "invariant-ai"
  npm_weekly_downloads: 1473
---

# Apply rule-based guardrails to agent traces and tool flows with Invariant

Insert a trace-aware guardrail layer between agents and their tools so unsafe message patterns or tool-call sequences are blocked by explicit rules.

## Prerequisites

Python environment or Invariant Gateway deployment, target LLM or MCP-enabled agent workflow, guardrail rules or policies, sample traces or live requests to evaluate

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the upstream package or gateway from the documented instructions, define guardrail rules for the target workflow, then run Invariant inline as a proxy or locally against captured traces to review and enforce violations.
```

## Documentation

- https://invariantlabs-ai.github.io/docs/mcp-scan/guardrails-reference/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apply-rule-based-guardrails-to-agent-traces-and-tool-flows-with-invariant/)
