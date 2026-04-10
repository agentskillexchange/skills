---
name: SigNoz Open-Source Observability Platform
description: SigNoz is an open-source observability platform built around OpenTelemetry
  for logs, metrics, and traces in one place. It is a practical fit when you want
  Datadog-style visibility with a self-hosted stack, first-party docs, and active
  upstream maintenance.
verification: security_reviewed
source: https://github.com/SigNoz/signoz
category:
- Monitoring &amp; Alerts
framework:
- Multi-Framework
---
# SigNoz Open-Source Observability Platform

SigNoz is an open-source observability platform from the SigNoz team that brings application performance monitoring, log management, distributed tracing, and dashboards into one product. The upstream project is built around OpenTelemetry, which makes it useful for teams that already instrument services with standard telemetry pipelines and want a single place to inspect logs, traces, and metrics without stitching together several tools by hand.
In practice, SigNoz is well suited to debugging production regressions, latency spikes, and service-to-service failures. Its README highlights out-of-the-box charts for latency, error rate, Apdex, and operations per second, along with centralized log search and distributed trace views. The docs cover instrumentation for common runtimes, deployment guidance, and ClickHouse-backed storage for high-volume telemetry workloads. That gives this skill a concrete job-to-be-done: help an agent stand up or integrate an observability stack that can collect telemetry through OpenTelemetry and surface it quickly for troubleshooting.
Integration points are straightforward. Agents can use SigNoz when they need to add observability to an application, connect OpenTelemetry SDKs, configure dashboards, or document incident-debugging workflows against a real upstream platform. The project has a large and active GitHub repository, current releases, and maintained docs, which clears the intake gate for verified metadata publication.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/signoz-open-source-observability-platform/)
