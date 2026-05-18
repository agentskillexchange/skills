---
name: "Review Dockerfiles for risky patterns and bad defaults with hadolint"
slug: "review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint"
description: "Catch insecure Dockerfile patterns, brittle package-install habits, and shell pitfalls before image builds ship."
github_stars: 12065
verification: "listed"
source: "https://github.com/hadolint/hadolint"
author: "hadolint"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hadolint/hadolint"
  github_stars: 12065
---

# Review Dockerfiles for risky patterns and bad defaults with hadolint

Catch insecure Dockerfile patterns, brittle package-install habits, and shell pitfalls before image builds ship.

## Prerequisites

hadolint binary and Dockerfiles

## Installation

Use the upstream install or setup path that matches your environment:
- Docker comes to the rescue, providing an easy way how to run hadolint on most
- docker run --rm -i hadolint/hadolint < Dockerfile
- docker run --rm -i ghcr.io/hadolint/hadolint < Dockerfile
- brew install hadolint

Requirements and caveats from upstream:
- [![Docker pulls][docker-img]][docker]
- A smarter Dockerfile linter that helps you build [best practice][] Docker
- Just pipe your Dockerfile to docker run:

Basic usage or getting-started notes:
- the Bash code inside RUN instructions.
- You can run hadolint locally to lint your Dockerfile.
- podman run --rm -i ghcr.io/hadolint/hadolint < Dockerfile

- Source: https://github.com/hadolint/hadolint
- Extracted from upstream docs: https://raw.githubusercontent.com/hadolint/hadolint/HEAD/README.md

## Documentation

- https://github.com/hadolint/hadolint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-dockerfiles-for-risky-patterns-and-bad-defaults-with-hadolint/)
