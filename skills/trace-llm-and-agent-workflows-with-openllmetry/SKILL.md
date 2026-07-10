---
title: "Trace LLM and agent workflows with OpenLLMetry"
description: "Add OpenTelemetry-based instrumentation to LLM and agent code so operators can inspect prompts, tool calls, latency, errors, and provider behavior in their existing observability stack."
verification: "security_reviewed"
source: "https://github.com/traceloop/openllmetry"
author: "Traceloop"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "traceloop/openllmetry"
  github_stars: 7170
---

# Trace LLM and agent workflows with OpenLLMetry

Add OpenTelemetry-based instrumentation to LLM and agent code so operators can inspect prompts, tool calls, latency, errors, and provider behavior in their existing observability stack.

## Prerequisites

Python, OpenLLMetry or Traceloop SDK, OpenTelemetry-compatible collector or backend

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the SDK with pip install traceloop-sdk, initialize tracing with the Traceloop SDK in the application, then route the emitted OpenTelemetry data to the team's collector or observability backend.
```

## Documentation

- https://traceloop.com/docs/openllmetry/getting-started-python

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-llm-and-agent-workflows-with-openllmetry/)
