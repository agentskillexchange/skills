---
name: "Pyroscope Continuous Profiling Platform by Grafana"
description: "Pyroscope is an open-source continuous profiling platform by Grafana Labs that helps identify CPU, memory, and I/O bottlenecks at the line-of-code level. It integrates natively with Grafana for flame graph visualization and supports profiling for Go, Java, Python, Ruby, Node.js, Rust, and .NET applications."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/grafana/pyroscope"
tool_ecosystem:
  github_repo: "grafana/pyroscope"
  github_stars: 11338
---
# Pyroscope Continuous Profiling Platform by Grafana

Pyroscope is an open-source continuous profiling platform by Grafana Labs that helps identify CPU, memory, and I/O bottlenecks at the line-of-code level. It integrates natively with Grafana for flame graph visualization and supports profiling for Go, Java, Python, Ruby, Node.js, Rust, and .NET applications.

Overview

Grafana Pyroscope is a continuous profiling platform designed to surface performance insights from running applications, helping teams optimize resource usage for CPU, memory, and I/O operations. Originally an independent open-source project, Pyroscope was acquired by Grafana Labs and is now part of the Grafana observability stack alongside Loki (logs), Tempo (traces), and Mimir (metrics).



How Continuous Profiling Works

Unlike traditional profiling which captures snapshots during development, continuous profiling runs in production with minimal overhead (typically 2-5% CPU). Pyroscope collects profiling data from your applications using either SDK-based push or Grafana Alloy-based pull, stores it efficiently, and lets you query it through flame graphs in Grafana.



Language Support

Pyroscope provides SDKs and auto-instrumentation for multiple languages:



- Go — Native pprof-based profiling



- Java — async-profiler integration



- Python — py-spy based profiling



- Ruby — rbspy integration



- Node.js — V8 profiler integration



- Rust — pprof-rs integration



- .NET — dotnet-trace integration



- eBPF — Kernel-level profiling without code changes



Explore Profiles UI

The Explore Profiles UI is part of the Grafana Explore Apps suite and provides a queryless, intuitive experience for visualizing profiling data. Users can browse services, compare time periods, and drill into specific functions without writing queries.



Use Cases

Proactive: Reducing resource consumption, improving application performance, preventing latency issues, and right-sizing cloud infrastructure. Reactive: Quickly resolving incidents with line-level detail, debugging active CPU spikes, memory leaks, or I/O bottlenecks in production.



Agent Integration Points

AI agents can query Pyroscope’s HTTP API to retrieve profiling data, identify hot functions, and correlate performance regressions with code changes. The flame graph data can be programmatically analyzed to find the top resource consumers in a service. Combined with Grafana’s alerting, agents can be triggered when profiling data shows anomalous resource usage patterns.



Installation

# Homebrew (macOS)

brew install pyroscope-io/brew/pyroscope

brew services start pyroscope



# Docker

docker run -it -p 4040:4040 grafana/pyroscope



# Helm (Kubernetes)

helm repo add grafana https://grafana.github.io/helm-charts

helm install pyroscope grafana/pyroscope

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pyroscope-continuous-profiling-platform-grafana
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pyroscope-continuous-profiling-platform-grafana -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pyroscope-continuous-profiling-platform-grafana -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pyroscope-continuous-profiling-platform-grafana -a codex
```

### OpenClaw

```bash
clawhub install pyroscope-continuous-profiling-platform-grafana
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pyroscope-continuous-profiling-platform-grafana/)
