---
name: "Regenerate Helm chart READMEs from values and comments before release"
slug: "regenerate-helm-chart-readmes-from-values-and-comments-before-release"
description: "Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff."
github_stars: 1732
verification: "security_reviewed"
source: "https://github.com/norwoodj/helm-docs"
author: "norwoodj"
publisher_type: "Open Source Project"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "norwoodj/helm-docs"
  github_stars: 1732
---

# Regenerate Helm chart READMEs from values and comments before release

Uses helm-docs to rebuild Helm chart documentation from Chart.yaml, values.yaml, and inline comments so README files stay aligned with the actual chart. The agent can run this before commit or release, then surface changed tables, missing descriptions, and documentation drift in a review-friendly diff.

## Prerequisites

Helm charts and the helm-docs CLI

## Installation

Use the upstream install or setup path that matches your environment:
- brew install norwoodj/tap/helm-docs
- go install github.com/norwoodj/helm-docs/cmd/helm-docs@latest
- docker run --rm --volume "$(pwd):/helm-docs" -u $(id -u) jnorwood/helm-docs:latest

Requirements and caveats from upstream:
- ### Using docker
- _and_ a leaf node within that field, description comments must be added for both

Basic usage or getting-started notes:
- helm-docs can be installed using [homebrew](https://brew.sh/):
- bash
- or [scoop](https://scoop.sh):

- Source: https://github.com/norwoodj/helm-docs
- Extracted from upstream docs: https://raw.githubusercontent.com/norwoodj/helm-docs/HEAD/README.md

## Documentation

- https://github.com/norwoodj/helm-docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regenerate-helm-chart-readmes-from-values-and-comments-before-release/)
