---
title: "Review Dockerfiles for risky patterns and bad defaults with hadolint"
description: "Use hadolint when an agent is reviewing Dockerfiles before build or release. It can flag risky base-image choices, bad package installation patterns, missing cleanup, and shell mistakes that make container images less secure or less reproducible. The boundary is Dockerfile review before image creation, not a generic container platform or registry listing."
verification: listed
source: "https://github.com/hadolint/hadolint"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hadolint/hadolint"
  github_stars: 12065
---

# Review Dockerfiles for risky patterns and bad defaults with hadolint

Use hadolint when an agent is reviewing Dockerfiles before build or release. It can flag risky base-image choices, bad package installation patterns, missing cleanup, and shell mistakes that make container images less secure or less reproducible. The boundary is Dockerfile review before image creation, not a generic container platform or registry listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint/)
