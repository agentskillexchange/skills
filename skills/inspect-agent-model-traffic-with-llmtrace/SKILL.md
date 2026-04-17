---
title: "Inspect agent model traffic with LLMTrace"
description: "Proxy OpenAI-compatible model traffic so operators can inspect prompts, detect risks, and enforce budget or policy controls."
verification: listed
source: "https://github.com/epappas/llmtrace"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "epappas/llmtrace"
  github_stars: 46
---

# Inspect agent model traffic with LLMTrace

Use LLMTrace when an operator wants to put OpenAI-compatible traffic behind a proxy that can inspect prompts, flag prompt injection or PII, and enforce cost or policy controls before responses hit downstream systems. Invoke it instead of calling the model endpoint directly when the task is security and observability around agent traffic, not routine application usage. The boundary is a traffic-inspection and guardrail workflow for model calls, not a generic SDK, model host, or broad observability platform listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inspect-agent-model-traffic-with-llmtrace
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/inspect-agent-model-traffic-with-llmtrace` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-agent-model-traffic-with-llmtrace/)
