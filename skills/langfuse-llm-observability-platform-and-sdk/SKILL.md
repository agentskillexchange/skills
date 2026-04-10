---
name: "Langfuse LLM Observability Platform and SDK"
description: "Use Langfuse to capture prompts, traces, generations, evaluations, and cost telemetry for LLM applications and agent workflows. This skill turns Langfuse from a generic observability brand into a concrete implementation pattern for tracing and analyzing model behavior."
verification: security_reviewed
source: "https://github.com/langfuse/langfuse"
category:
  - "Monitoring &amp; Alerts"
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/langfuse-llm-observability-platform-and-sdk/)
