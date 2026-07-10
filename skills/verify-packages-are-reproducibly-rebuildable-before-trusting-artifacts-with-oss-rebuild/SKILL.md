---
name: "Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild"
slug: "verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild"
description: "Query OSS Rebuild attestations and rebuild metadata so an agent can verify whether a published package artifact matches a reproducible upstream rebuild."
github_stars: 687
verification: "security_reviewed"
source: "https://github.com/google/oss-rebuild"
author: "Google and contributors"
publisher_type: "Open Source"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "google/oss-rebuild"
  github_stars: 687
---

# Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild

Query OSS Rebuild attestations and rebuild metadata so an agent can verify whether a published package artifact matches a reproducible upstream rebuild.

## Prerequisites

Go, oss-rebuild CLI, optional gcloud ADC credentials for signature verification

## Installation

Use the upstream install or setup path that matches your environment:
- $ go install github.com/google/oss-rebuild/cmd/oss-rebuild@latest

Requirements and caveats from upstream:
- PyPI (Python)
- chained with docker to execute a rebuild locally:
- $ oss-rebuild get pypi absl-py 2.0.0 --output=dockerfile | docker run $(docker buildx build -q -)

Basic usage or getting-started notes:
- The oss-rebuild CLI tool provides access to OSS Rebuild data:
- bash
- $ go run github.com/google/oss-rebuild/cmd/oss-rebuild@latest --help

- Source: https://github.com/google/oss-rebuild
- Extracted from upstream docs: https://raw.githubusercontent.com/google/oss-rebuild/HEAD/README.md

## Documentation

- https://docs.oss-rebuild.dev/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild/)
