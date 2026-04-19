---
title: "Trace Python memory allocation hotspots before leaks and spikes reach production with Memray"
description: "Use Memray when an agent needs to answer a specific diagnostic question: where is Python memory actually being allocated, retained, or leaking? It fits incident response, performance regression triage, and pre-release investigations where heap growth is real but the cause is not yet clear. Invoke this instead of using the product normally when the agent must capture an allocation trace, compare runs, and turn the resulting evidence into a concrete remediation path. This is skill-shaped because the workflow boundary is narrow and operational: capture memory traces, inspect hotspots, and identify leak sources. It is not a generic Python tooling card or broad observability platform listing."
source: "https://github.com/bloomberg/memray"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bloomberg/memray"
  github_stars: 14986
  npm_package: "memray"
  npm_weekly_downloads: 16282665
---

# Trace Python memory allocation hotspots before leaks and spikes reach production with Memray

Use Memray when an agent needs to answer a specific diagnostic question: where is Python memory actually being allocated, retained, or leaking? It fits incident response, performance regression triage, and pre-release investigations where heap growth is real but the cause is not yet clear. Invoke this instead of using the product normally when the agent must capture an allocation trace, compare runs, and turn the resulting evidence into a concrete remediation path. This is skill-shaped because the workflow boundary is narrow and operational: capture memory traces, inspect hotspots, and identify leak sources. It is not a generic Python tooling card or broad observability platform listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-python-memory-allocation-hotspots-before-leaks-and-spikes-reach-production-with-memray/)
