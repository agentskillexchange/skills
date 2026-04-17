---
title: "Langfuse LLM Observability Platform and SDK"
description: "Langfuse is an LLM observability platform for tracing prompts, completions, tool calls, evaluations, latency, and usage across AI systems. A skill anchored to Langfuse is useful when the job-to-be-done is “instrument this agent or app so we can understand quality, cost, and failure modes.” That includes prompt logging, trace correlation, dataset creation, experiment tracking, human review, and production debugging.\nIn operation, the skill would configure the Langfuse SDK, attach trace or span metadata, record generations and tool invocations, tag sessions, capture token and cost data, and optionally push scores or feedback from downstream evaluators. The outputs can include trace URLs, span trees, latency summaries, token counts, cost reports, prompt/version metadata, and evaluation records. That is valuable for agent teams running prompt experiments, troubleshooting regressions, or building monitoring dashboards around model behavior.\nThe major integration points are the Langfuse platform itself, the Langfuse SDK, API keys, trace and observation models, dataset/evaluation workflows, and instrumentation hooks inside server-side apps or agent runtimes. Technical terms include spans, traces, prompt versioning, token accounting, latency histograms, feedback signals, observability pipelines, and LLMOps. This gives a marketplace user a precise, source-backed skill for implementing Langfuse rather than a hand-wavy “AI monitoring” description."
verification: security_reviewed
source: "https://github.com/langfuse/langfuse"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "langfuse/langfuse"
  github_stars: 24091
---

# Langfuse LLM Observability Platform and SDK

Langfuse is an LLM observability platform for tracing prompts, completions, tool calls, evaluations, latency, and usage across AI systems. A skill anchored to Langfuse is useful when the job-to-be-done is “instrument this agent or app so we can understand quality, cost, and failure modes.” That includes prompt logging, trace correlation, dataset creation, experiment tracking, human review, and production debugging.
In operation, the skill would configure the Langfuse SDK, attach trace or span metadata, record generations and tool invocations, tag sessions, capture token and cost data, and optionally push scores or feedback from downstream evaluators. The outputs can include trace URLs, span trees, latency summaries, token counts, cost reports, prompt/version metadata, and evaluation records. That is valuable for agent teams running prompt experiments, troubleshooting regressions, or building monitoring dashboards around model behavior.
The major integration points are the Langfuse platform itself, the Langfuse SDK, API keys, trace and observation models, dataset/evaluation workflows, and instrumentation hooks inside server-side apps or agent runtimes. Technical terms include spans, traces, prompt versioning, token accounting, latency histograms, feedback signals, observability pipelines, and LLMOps. This gives a marketplace user a precise, source-backed skill for implementing Langfuse rather than a hand-wavy “AI monitoring” description.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/langfuse-llm-observability-platform-and-sdk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/langfuse-llm-observability-platform-and-sdk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/langfuse-llm-observability-platform-and-sdk/)
