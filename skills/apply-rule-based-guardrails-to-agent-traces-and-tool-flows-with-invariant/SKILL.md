---
name: "Apply rule-based guardrails to agent traces and tool flows with Invariant"
slug: "apply-rule-based-guardrails-to-agent-traces-and-tool-flows-with-invariant"
description: "Insert a trace-aware guardrail layer between agents and their tools so unsafe message patterns or tool-call sequences are blocked by explicit rules."
github_stars: 409
verification: "security_reviewed"
source: "https://github.com/invariantlabs-ai/invariant"
author: "Invariant Labs"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
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

Requirements and caveats from upstream:
- Guardrailing rules are simple Python-inspired matching rules, that can be written to identify and prevent malicious agent behavior:
- python
- Here, (msg: Message) automatically is assigned every checkable message, whereas the second line executes like regular Python. To facilitate checking Guardrails comes with an extensive standard library of operations, a...

Basic usage or getting-started notes:
- <a href="https://invariantlabs-ai.github.io/docs/mcp-scan/guardrails-reference/">Getting Started</a> |

- Source: https://github.com/invariantlabs-ai/invariant
- Extracted from upstream docs: https://raw.githubusercontent.com/invariantlabs-ai/invariant/HEAD/README.md

## Documentation

- https://invariantlabs-ai.github.io/docs/mcp-scan/guardrails-reference/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apply-rule-based-guardrails-to-agent-traces-and-tool-flows-with-invariant/)
