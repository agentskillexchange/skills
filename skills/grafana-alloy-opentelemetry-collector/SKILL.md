---
name: Grafana Alloy OpenTelemetry Collector Distribution
description: Grafana Alloy is an open-source OpenTelemetry Collector distribution
  with programmable pipelines for metrics, logs, traces, and profiles. This skill
  enables agents to configure and manage observability data collection using Alloy.
verification: security_reviewed
source: https://github.com/grafana/alloy
category:
- Monitoring &amp; Alerts
framework:
- Custom Agents
tool_ecosystem:
  github_repo: grafana/alloy
  github_stars: 3026
  license: Apache-2.0
---
# Grafana Alloy OpenTelemetry Collector Distribution

Grafana Alloy is an open-source OpenTelemetry Collector distribution that adds programmable pipelines, native Prometheus support, and Kubernetes-native configuration to the standard OTel collector. Maintained by Grafana Labs, Alloy replaces the older Grafana Agent and provides a single binary for collecting metrics, logs, traces, and continuous profiling data from any environment.
This skill enables agents to write and manage Alloy configuration using its expression-based syntax called Alloy Configuration Language. Agents learn to compose observability pipelines by connecting receiver, processor, and exporter components that handle data from OpenTelemetry, Prometheus, Loki, Tempo, and Pyroscope sources. The configuration language supports variables, conditional logic, and component references, making complex pipeline topologies readable and maintainable.
Key features include automatic workload distribution through built-in clustering, where multiple Alloy instances coordinate to split scrape targets without a separate coordinator service; centralized configuration management via remote config pull from GitHub, S3, or HTTP endpoints; and a built-in debugging UI for visualizing pipeline topology and inspecting data flow in real time. Alloy supports dozens of OTel Collector components alongside custom components purpose-built for the Grafana ecosystem.
Agents using this skill produce production-ready observability configurations that collect and route telemetry data to backends like Prometheus, Grafana Mimir, Loki, Tempo, and any OpenTelemetry-compatible endpoint. Alloy modules allow reusable pipeline snippets to be shared across teams, reducing complex multi-page configs to a few import lines. The tool runs on Linux, macOS, Windows, and Kubernetes with native service discovery for pods, nodes, and services. It is Apache-2.0 licensed with regular six-week release cycles backed by Grafana Labs.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-alloy-opentelemetry-collector/)
