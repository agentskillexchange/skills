---
title: "Shard slow pytest suites by historic timings before CI bottlenecks pile up with pytest-split"
description: "Use pytest-split when an agent needs to break a growing pytest suite into balanced groups based on historical run times. It fits CI tuning work where the problem is not test correctness but slow, uneven, or unpredictable lane completion. Invoke this instead of running pytest normally when the agent must produce balanced shards and reduce end-to-end CI time without hand-curating test buckets. This is skill-shaped because the boundary is specific: timing-aware pytest sharding for CI. It is not a generic pytest plugin catalog entry or broad Python testing framework listing."
source: "https://github.com/jerry-git/pytest-split"
verification: "listed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jerry-git/pytest-split"
  github_stars: 308
  npm_package: "pytest-split"
  npm_weekly_downloads: 12820130
---

# Shard slow pytest suites by historic timings before CI bottlenecks pile up with pytest-split

Use pytest-split when an agent needs to break a growing pytest suite into balanced groups based on historical run times. It fits CI tuning work where the problem is not test correctness but slow, uneven, or unpredictable lane completion. Invoke this instead of running pytest normally when the agent must produce balanced shards and reduce end-to-end CI time without hand-curating test buckets. This is skill-shaped because the boundary is specific: timing-aware pytest sharding for CI. It is not a generic pytest plugin catalog entry or broad Python testing framework listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shard-slow-pytest-suites-by-historic-timings-before-ci-bottlenecks-pile-up-with-pytest-split/)
