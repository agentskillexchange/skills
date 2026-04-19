---
title: "Review Dockerfiles for risky patterns and bad defaults with hadolint"
description: "Use hadolint when an agent is reviewing Dockerfiles before build or release. It can flag risky base-image choices, bad package installation patterns, missing cleanup, and shell mistakes that make container images less secure or less reproducible. The boundary is Dockerfile review before image creation, not a generic container platform or registry listing."
source: "https://github.com/hadolint/hadolint"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hadolint/hadolint"
  github_stars: 12065
---

# Review Dockerfiles for risky patterns and bad defaults with hadolint

Use hadolint when an agent is reviewing Dockerfiles before build or release. It can flag risky base-image choices, bad package installation patterns, missing cleanup, and shell mistakes that make container images less secure or less reproducible. The boundary is Dockerfile review before image creation, not a generic container platform or registry listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint/)
