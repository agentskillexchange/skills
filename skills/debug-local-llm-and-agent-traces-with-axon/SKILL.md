---
name: "Debug local LLM and agent traces with Axon"
slug: "debug-local-llm-and-agent-traces-with-axon"
description: "Run Axon as a local OpenTelemetry endpoint and dashboard for inspecting LangChain and instrumented agent traces without sending run data to a cloud service."
github_stars: 151
verification: "security_reviewed"
source: "https://github.com/langchain-tracer/Axon"
author: "AXON AI TEAM"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "langchain-tracer/Axon"
  github_stars: 151
  npm_package: "@axon-ai/cli"
  npm_weekly_downloads: 394
---

# Debug local LLM and agent traces with Axon

Run Axon as a local OpenTelemetry endpoint and dashboard for inspecting LangChain and instrumented agent traces without sending run data to a cloud service.

## Prerequisites

Node.js, @axon-ai/cli, LangChain or OpenTelemetry-instrumented agent application, local OTLP endpoint

## Installation

Install or set up from the source-backed instructions:

Install with `npm install -g @axon-ai/cli`, run `axon-ai init --project ` inside the target project, then run `axon-ai start`. Point LangChain, OpenLLMetry, OpenInference, or raw OTEL exporters at `http://localhost:4000/v1/traces` or the configured port, then inspect traces in the local dashboard.

- Source: https://github.com/langchain-tracer/Axon

## Documentation

- https://github.com/langchain-tracer/Axon

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-local-llm-and-agent-traces-with-axon/)
