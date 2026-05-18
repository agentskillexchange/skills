---
name: "Assemble minimal OCI images from declarative package configs with apko"
slug: "assemble-minimal-oci-images-from-declarative-package-configs-with-apko"
description: "Use apko to build small OCI images from declarative package manifests when supply-chain clarity and minimal contents matter more than a conventional Dockerfile flow."
github_stars: 1590
verification: "security_reviewed"
source: "https://github.com/chainguard-dev/apko"
author: "Chainguard"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "chainguard-dev/apko"
  github_stars: 1590
---

# Assemble minimal OCI images from declarative package configs with apko

Use apko to build small OCI images from declarative package manifests when supply-chain clarity and minimal contents matter more than a conventional Dockerfile flow.

## Prerequisites

apko and access to the package sources and OCI output destination you intend to use

## Installation

Use the upstream install or setup path that matches your environment:
- brew install apko
- go install chainguard.dev/apko@latest
- docker run cgr.dev/chainguard/apko version
- docker run -v "$PWD":/work cgr.dev/chainguard/apko build examples/alpine-base.yaml apko-alpine:edge apko-alpine.tar

Requirements and caveats from upstream:
- or, with Docker:
- You can then load the generated tar image into a Docker environment:

Basic usage or getting-started notes:
- **Fully reproducible by default.** Run apko twice and you will get exactly the same binary.
- **Services.** apko supports using the [s6 supervision suite](https://skarnet.org/software/s6) to run multiple processes
- You can install apko from Homebrew:

- Source: https://github.com/chainguard-dev/apko
- Extracted from upstream docs: https://raw.githubusercontent.com/chainguard-dev/apko/HEAD/README.md

## Documentation

- https://edu.chainguard.dev/open-source/build-tools/apko/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/assemble-minimal-oci-images-from-declarative-package-configs-with-apko/)
