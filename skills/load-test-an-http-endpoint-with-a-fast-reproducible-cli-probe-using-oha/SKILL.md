---
title: "Load-test an HTTP endpoint with a fast reproducible CLI probe using oha"
description: "Run a quick concurrent HTTP benchmark against a URL before deeper performance work or regression triage."
verification: "listed"
source: "https://github.com/hatoo/oha"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hatoo/oha"
  github_stars: 10198
---

# Load-test an HTTP endpoint with a fast reproducible CLI probe using oha

Use oha when an agent needs to hit a specific HTTP endpoint with controlled concurrency and duration to get a fast latency and throughput snapshot. A user should invoke this instead of using a full performance platform normally when the task is a quick reproducible endpoint probe or comparison run, not scenario modeling, distributed testing, or long-lived monitoring. The scope boundary is skill-shaped: it benchmarks one HTTP target from a simple CLI invocation and returns concrete performance measurements, not a general observability stack or load-testing platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/load-test-an-http-endpoint-with-a-fast-reproducible-cli-probe-using-oha/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/load-test-an-http-endpoint-with-a-fast-reproducible-cli-probe-using-oha
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/load-test-an-http-endpoint-with-a-fast-reproducible-cli-probe-using-oha`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-an-http-endpoint-with-a-fast-reproducible-cli-probe-using-oha/)
