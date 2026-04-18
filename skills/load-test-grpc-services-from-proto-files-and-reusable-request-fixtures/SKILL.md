---
title: "Load-test gRPC services from proto files and reusable request fixtures"
description: "This ASE skill uses ghz to run repeatable gRPC load tests from proto files, protosets, or server reflection. An agent can replay request fixtures at controlled concurrency, capture latency and error rates, and export machine-readable reports for regression checks or performance investigations."
verification: security_reviewed
source: "https://github.com/bojand/ghz"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bojand/ghz"
  github_stars: 3315
---

# Load-test gRPC services from proto files and reusable request fixtures

This ASE skill is built around ghz, the open source gRPC benchmarking and load testing tool maintained in the bojand/ghz project. The agent job is concrete: point ghz at a gRPC method using a proto file, a protoset bundle, or server reflection, replay request data under controlled concurrency or rate schedules, and return structured latency, throughput, and error results. That makes the entry skill-shaped instead of a generic CLI listing, because the useful outcome is not “install ghz.” The useful outcome is “exercise a specific gRPC endpoint with known request fixtures and compare the service behavior under load.”

Invoke this when an agent needs to validate a performance-sensitive gRPC change, reproduce a latency regression, smoke-test a service contract after deployment, or benchmark a method before tuning infrastructure. ghz supports unary and streaming calls, JSON and binary payloads, config files, metadata templates, and multiple output formats including summary, JSON, CSV, HTML, and Influx-friendly formats. That makes it practical for CI checks, staging environment probes, incident follow-up, and repeatable engineering baselines.

The scope boundary is clear. This skill is not a general observability platform, not an HTTP load tester, and not an always-on monitoring system. It is a synthetic gRPC benchmarking workflow that depends on explicit service definitions or reflection and reproducible request fixtures. Integration points include protobuf repos, generated protosets, reflection-enabled services, JSON or TOML test configs, CI pipelines, and downstream reporting tools. If an agent needs to answer “how does this gRPC method behave under a defined load pattern?” ghz is a strong upstream fit.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/load-test-grpc-services-from-proto-files-and-reusable-request-fixtures
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/load-test-grpc-services-from-proto-files-and-reusable-request-fixtures` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-grpc-services-from-proto-files-and-reusable-request-fixtures/)
