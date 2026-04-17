---
title: "Trace Python memory allocation hotspots before leaks and spikes reach production with Memray"
description: "Lets an agent record Python allocation traces and inspect the biggest allocators, retained objects, and leak paths before memory growth turns into a production incident."
verification: listed
source: "https://github.com/bloomberg/memray"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bloomberg/memray"
  github_stars: 14986
  npm_package: "memray"
  npm_weekly_downloads: 16282665
---

# Trace Python memory allocation hotspots before leaks and spikes reach production with Memray

Use Memray when an agent needs to answer a specific diagnostic question: where is Python memory actually being allocated, retained, or leaking? It fits incident response, performance regression triage, and pre-release investigations where heap growth is real but the cause is not yet clear.

Invoke this instead of using the product normally when the agent must capture an allocation trace, compare runs, and turn the resulting evidence into a concrete remediation path. This is skill-shaped because the workflow boundary is narrow and operational: capture memory traces, inspect hotspots, and identify leak sources. It is not a generic Python tooling card or broad observability platform listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trace-python-memory-allocation-hotspots-before-leaks-and-spikes-reach-production-with-memray
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/trace-python-memory-allocation-hotspots-before-leaks-and-spikes-reach-production-with-memray` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-python-memory-allocation-hotspots-before-leaks-and-spikes-reach-production-with-memray/)
