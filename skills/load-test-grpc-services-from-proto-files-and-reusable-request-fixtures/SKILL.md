---
title: "Load-test gRPC services from proto files and reusable request fixtures"
description: "This ASE skill is built around ghz, the open source gRPC benchmarking and load testing tool maintained in the bojand/ghz project. The agent job is concrete: point ghz at a gRPC method using a proto file, a protoset bundle, or server reflection, replay request data under controlled concurrency or rate schedules, and return structured latency, throughput, and error results. That makes the entry skill-shaped instead of a generic CLI listing, because the useful outcome is not “install ghz.” The useful outcome is “exercise a specific gRPC endpoint with known request fixtures and compare the service behavior under load.” Invoke this when an agent needs to validate a performance-sensitive gRPC change, reproduce a latency regression, smoke-test a service contract after deployment, or benchmark a method before tuning infrastructure. ghz supports unary and streaming calls, JSON and binary payloads, config files, metadata templates, and multiple output formats including summary, JSON, CSV, HTML, and Influx-friendly formats. That makes it practical for CI checks, staging environment probes, incident follow-up, and repeatable engineering baselines. The scope boundary is clear. This skill is not a general observability platform, not an HTTP load tester, and not an always-on monitoring system. It is a synthetic gRPC benchmarking workflow that depends on explicit service definitions or reflection and reproducible request fixtures. Integration points include protobuf repos, generated protosets, reflection-enabled services, JSON or TOML test configs, CI pipelines, and downstream reporting tools. If an agent needs to answer “how does this gRPC method behave under a defined load pattern?” ghz is a strong upstream fit."
source: "https://github.com/bojand/ghz"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bojand/ghz"
  github_stars: 3315
---

# Load-test gRPC services from proto files and reusable request fixtures

This ASE skill is built around ghz, the open source gRPC benchmarking and load testing tool maintained in the bojand/ghz project. The agent job is concrete: point ghz at a gRPC method using a proto file, a protoset bundle, or server reflection, replay request data under controlled concurrency or rate schedules, and return structured latency, throughput, and error results. That makes the entry skill-shaped instead of a generic CLI listing, because the useful outcome is not “install ghz.” The useful outcome is “exercise a specific gRPC endpoint with known request fixtures and compare the service behavior under load.” Invoke this when an agent needs to validate a performance-sensitive gRPC change, reproduce a latency regression, smoke-test a service contract after deployment, or benchmark a method before tuning infrastructure. ghz supports unary and streaming calls, JSON and binary payloads, config files, metadata templates, and multiple output formats including summary, JSON, CSV, HTML, and Influx-friendly formats. That makes it practical for CI checks, staging environment probes, incident follow-up, and repeatable engineering baselines. The scope boundary is clear. This skill is not a general observability platform, not an HTTP load tester, and not an always-on monitoring system. It is a synthetic gRPC benchmarking workflow that depends on explicit service definitions or reflection and reproducible request fixtures. Integration points include protobuf repos, generated protosets, reflection-enabled services, JSON or TOML test configs, CI pipelines, and downstream reporting tools. If an agent needs to answer “how does this gRPC method behave under a defined load pattern?” ghz is a strong upstream fit.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-grpc-services-from-proto-files-and-reusable-request-fixtures/)
