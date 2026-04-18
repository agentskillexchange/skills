---
title: "Apply rule-based guardrails to agent traces and tool flows with Invariant"
description: "Insert a trace-aware guardrail layer between agents and their tools so unsafe message patterns or tool-call sequences are blocked by explicit rules."
verification: listed
source: "https://github.com/invariantlabs-ai/invariant"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "invariantlabs-ai/invariant"
  github_stars: 409
  ase_npm_package: "invariant-ai"
  npm_weekly_downloads: 1473
---

# Apply rule-based guardrails to agent traces and tool flows with Invariant

Use Invariant when the job is to write and evaluate explicit guardrail rules that inspect tool-call sequences or message traces and block unsafe agent behavior before or during execution, not when a team just wants a general security product. The workflow is concrete: place Invariant between the agent and its MCP or LLM boundary, define rules, run traces through the policy engine, and inspect violations or blocked flows. That scope boundary, trace-aware guardrail enforcement for agent actions, keeps this publishable as a skill instead of a generic SDK or platform card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apply-rule-based-guardrails-to-agent-traces-and-tool-flows-with-invariant
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/apply-rule-based-guardrails-to-agent-traces-and-tool-flows-with-invariant` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apply-rule-based-guardrails-to-agent-traces-and-tool-flows-with-invariant/)
