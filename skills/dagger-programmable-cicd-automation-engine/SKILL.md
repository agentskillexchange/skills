---
name: "Dagger Programmable CI/CD Automation Engine"
slug: "dagger-programmable-cicd-automation-engine"
description: "Dagger is an open-source automation engine for building, testing, and shipping any codebase. It replaces shell scripts and proprietary YAML with real code using SDKs in Go, Python, TypeScript, and 5 other languages, with built-in caching and OpenTelemetry tracing."
github_stars: 15582
verification: "security_reviewed"
source: "https://github.com/dagger/dagger"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dagger/dagger"
  github_stars: 15582
---

# Dagger Programmable CI/CD Automation Engine

Dagger is an open-source automation engine for building, testing, and shipping any codebase. It replaces shell scripts and proprietary YAML with real code using SDKs in Go, Python, TypeScript, and 5 other languages, with built-in caching and OpenTelemetry tracing.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install dagger/tap/dagger

Requirements and caveats from upstream:
- **SDKs in 8 languages**. Native SDKs for Go, Python, TypeScript, PHP, Java, .NET, Elixir and Rust. Each SDK is generated from the API schema, so you get idiomatic code with full type safety and editor support.
- **Runs anywhere**. The only requirement is a Linux container runtime. Runs natively on Linux, or via Docker Desktop and similar products on macOS and Windows. Local and CI behavior are identical.

Basic usage or getting-started notes:
- **Local-first**. Once you automate a task with Dagger, it will reliably run on any supported system: your laptop, AI sandbox, CI server, or dedicated cloud infrastructure. The only dependency is a container runtime li...
- **Repeatable**. Tools run in containers, orchestrated by sandboxed functions. Host dependencies are explicit and strictly typed. Intermediate artifacts are built just-in-time. Every operation is incremental by default...
- **Incremental execution**. Every operation is keyed by its inputs. Change one file and only the affected operations re-run. Caching is content-addressed and works automatically across local runs and CI.

- Source: https://github.com/dagger/dagger
- Extracted from upstream docs: https://raw.githubusercontent.com/dagger/dagger/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dagger-programmable-cicd-automation-engine/)
