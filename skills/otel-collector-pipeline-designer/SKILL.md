---
name: "OpenTelemetry Collector Pipeline Designer"
slug: "otel-collector-pipeline-designer"
description: "Designs OpenTelemetry Collector pipeline configurations with receivers (otlp, prometheus, filelog), processors (batch, attributes, tail_sampling), and exporters (otlphttp, jaeger, elasticsearch)."
github_stars: 6867
verification: "security_reviewed"
source: "https://github.com/open-telemetry/opentelemetry-collector"
author: "OpenTelemetry"
category: "Monitoring & Alerts"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "open-telemetry/opentelemetry-collector"
  github_stars: 6867
---

# OpenTelemetry Collector Pipeline Designer

Designs OpenTelemetry Collector pipeline configurations with receivers (otlp, prometheus, filelog), processors (batch, attributes, tail_sampling), and exporters (otlphttp, jaeger, elasticsearch).

## Prerequisites

Go

## Installation

Requirements and caveats from upstream:
- [{"critical":{"identity":{"docker-reference":"ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib"},"image":{"docker-manifest-digest":"sha256:5cea85bcbc734a3c0a641368e5a4ea9d31b4729...
- In addition to what is described at the organization-level, the SIG Collector requires all core approvers to take part in rotating

Basic usage or getting-started notes:
- to run, operate and maintain multiple agents/collectors in order to support
- We are signing the images otel/opentelemetry-collector and otel/opentelemetry-collector-contrib using [sigstore cosign](https://github.com/sigstore/cosign) tool and to verify the signatures you can run the following c...
- Example:

- Source: https://github.com/open-telemetry/opentelemetry-collector
- Extracted from upstream docs: https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/HEAD/README.md

## Documentation

- https://opentelemetry.io/docs/collector/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/otel-collector-pipeline-designer/)
