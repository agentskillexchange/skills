---
name: "Inspect agent model traffic with LLMTrace"
slug: "inspect-agent-model-traffic-with-llmtrace"
description: "Proxy OpenAI-compatible model traffic so operators can inspect prompts, detect risks, and enforce budget or policy controls."
github_stars: 46
verification: "listed"
source: "https://github.com/epappas/llmtrace"
author: "epappas"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "epappas/llmtrace"
  github_stars: 46
---

# Inspect agent model traffic with LLMTrace

Proxy OpenAI-compatible model traffic so operators can inspect prompts, detect risks, and enforce budget or policy controls.

## Prerequisites

Rust or Docker runtime, OpenAI-compatible client or SDK

## Installation

Use the upstream install or setup path that matches your environment:
- cargo install llmtrace # from crates.io
- docker pull ghcr.io/epappas/llmtrace-proxy:latest # Docker
- cargo install llmtrace
- pip install llmtracing

Requirements and caveats from upstream:
- python
- ### OpenAI Python SDK
- ### OpenAI Node.js SDK

Basic usage or getting-started notes:
- **Cost runaway** — Uncontrolled API spend, inefficient token usage
- **Performance Monitoring** — Latency, token usage, streaming metrics (TTFT), error tracking
- ### 1. Install

- Source: https://github.com/epappas/llmtrace
- Extracted from upstream docs: https://raw.githubusercontent.com/epappas/llmtrace/HEAD/README.md

## Documentation

- https://github.com/epappas/llmtrace/tree/main/docs/getting-started

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-agent-model-traffic-with-llmtrace/)
