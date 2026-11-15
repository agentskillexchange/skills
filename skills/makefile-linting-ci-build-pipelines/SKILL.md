---
name: "Makefile Linting for CI and Build Pipelines"
slug: "makefile-linting-ci-build-pipelines"
description: "Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing."
github_stars: 1188
verification: "security_reviewed"
source: "https://github.com/checkmake/checkmake"
author: "checkmake maintainers"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "checkmake/checkmake"
  github_stars: 1188
---

# Makefile Linting for CI and Build Pipelines

Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing.

## Prerequisites

checkmake binary and existing Makefiles

## Installation

Use the upstream install or setup path that matches your environment:
- docker build --build-arg BUILDER_NAME='Your Name' --build-arg BUILDER_EMAIL=your.name@example.com . -t checker
- docker run --workdir / -v "$PWD"/Makefile:/Makefile quay.io/checkmake/checkmake:latest
- docker run --workdir / -v "$PWD"/Makefile:/Makefile -v "$PWD"/checkmake.ini:/checkmake.ini quay.io/checkmake/checkmake:latest
- go install github.com/checkmake/checkmake/cmd/checkmake@latest

Requirements and caveats from upstream:
- building or running a container image can be done with docker and podman.
- The container command used for building (docker or podman) is auto-detected with a preference for podman but can be overridden by the make variable CONTAINER_CMD.
- The locally built image can be published with a make image-pushcommand corresponding to the previously described make image-buildcommand or alrenatively directly using docker push or podman push

Basic usage or getting-started notes:
- console
- % checkmake Makefile
- % checkmake Makefile foo.mk bar.mk baz.mk

- Source: https://github.com/checkmake/checkmake
- Extracted from upstream docs: https://raw.githubusercontent.com/checkmake/checkmake/HEAD/README.md

## Documentation

- https://github.com/checkmake/checkmake

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-linting-ci-build-pipelines/)
