---
title: "OpenTelemetry Collector Pipeline Designer"
description: "Designs OpenTelemetry Collector pipeline configurations with receivers (otlp, prometheus, filelog), processors (batch, attributes, tail_sampling), and exporters (otlphttp, jaeger, elasticsearch)."
verification: "security_reviewed"
source: "https://github.com/open-telemetry/opentelemetry-collector"
author: "OpenTelemetry"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "open-telemetry/opentelemetry-collector"
  github_stars: 6867
---

# OpenTelemetry Collector Pipeline Designer

Designs OpenTelemetry Collector pipeline configurations with receivers (otlp, prometheus, filelog), processors (batch, attributes, tail_sampling), and exporters (otlphttp, jaeger, elasticsearch).

## Prerequisites

Go

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
go install go.opentelemetry.io/collector/cmd/otelcol@latest
```

## Documentation

- https://opentelemetry.io/docs/collector/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/otel-collector-pipeline-designer/)
