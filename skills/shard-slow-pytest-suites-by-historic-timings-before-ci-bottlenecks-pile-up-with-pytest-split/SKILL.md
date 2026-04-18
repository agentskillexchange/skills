---
title: "Shard slow pytest suites by historic timings before CI bottlenecks pile up with pytest-split"
description: "Lets an agent split a large pytest suite into timing-balanced shards so parallel CI lanes finish faster and with less variance."
verification: listed
source: "https://github.com/jerry-git/pytest-split"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jerry-git/pytest-split"
  github_stars: 308
  ase_npm_package: "pytest-split"
  npm_weekly_downloads: 12820130
---

# Shard slow pytest suites by historic timings before CI bottlenecks pile up with pytest-split

Use pytest-split when an agent needs to break a growing pytest suite into balanced groups based on historical run times. It fits CI tuning work where the problem is not test correctness but slow, uneven, or unpredictable lane completion.

Invoke this instead of running pytest normally when the agent must produce balanced shards and reduce end-to-end CI time without hand-curating test buckets. This is skill-shaped because the boundary is specific: timing-aware pytest sharding for CI. It is not a generic pytest plugin catalog entry or broad Python testing framework listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/shard-slow-pytest-suites-by-historic-timings-before-ci-bottlenecks-pile-up-with-pytest-split
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/shard-slow-pytest-suites-by-historic-timings-before-ci-bottlenecks-pile-up-with-pytest-split` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shard-slow-pytest-suites-by-historic-timings-before-ci-bottlenecks-pile-up-with-pytest-split/)
