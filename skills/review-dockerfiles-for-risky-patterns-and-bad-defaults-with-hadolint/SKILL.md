---
title: "Review Dockerfiles for risky patterns and bad defaults with hadolint"
description: "Catch insecure Dockerfile patterns, brittle package-install habits, and shell pitfalls before image builds ship."
verification: "listed"
source: "https://github.com/hadolint/hadolint"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hadolint/hadolint"
  github_stars: 12065
---

# Review Dockerfiles for risky patterns and bad defaults with hadolint

Use hadolint when an agent is reviewing Dockerfiles before build or release. It can flag risky base-image choices, bad package installation patterns, missing cleanup, and shell mistakes that make container images less secure or less reproducible. The boundary is Dockerfile review before image creation, not a generic container platform or registry listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint/)
