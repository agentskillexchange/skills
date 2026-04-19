---
title: "Inspect agent model traffic with LLMTrace"
description: "Use LLMTrace when an operator wants to put OpenAI-compatible traffic behind a proxy that can inspect prompts, flag prompt injection or PII, and enforce cost or policy controls before responses hit downstream systems. Invoke it instead of calling the model endpoint directly when the task is security and observability around agent traffic, not routine application usage. The boundary is a traffic-inspection and guardrail workflow for model calls, not a generic SDK, model host, or broad observability platform listing."
source: "https://github.com/epappas/llmtrace"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "epappas/llmtrace"
  github_stars: 46
---

# Inspect agent model traffic with LLMTrace

Use LLMTrace when an operator wants to put OpenAI-compatible traffic behind a proxy that can inspect prompts, flag prompt injection or PII, and enforce cost or policy controls before responses hit downstream systems. Invoke it instead of calling the model endpoint directly when the task is security and observability around agent traffic, not routine application usage. The boundary is a traffic-inspection and guardrail workflow for model calls, not a generic SDK, model host, or broad observability platform listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-agent-model-traffic-with-llmtrace/)
