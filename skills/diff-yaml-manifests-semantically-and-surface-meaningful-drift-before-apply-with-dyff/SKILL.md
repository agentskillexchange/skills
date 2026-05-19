---
name: "Diff YAML manifests semantically and surface meaningful drift before apply with dyff"
slug: "diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff"
description: "Use dyff to compare YAML documents by structure and changed paths so agents can review configuration drift without the noise of plain line diffs."
github_stars: 1800
verification: "security_reviewed"
source: "https://github.com/homeport/dyff"
author: "homeport"
publisher_type: "open_source_project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "homeport/dyff"
  github_stars: 1800
---

# Diff YAML manifests semantically and surface meaningful drift before apply with dyff

Use dyff to compare YAML documents by structure and changed paths so agents can review configuration drift without the noise of plain line diffs.

## Prerequisites

dyff

## Installation

Use the upstream install or setup path that matches your environment:
- make install clean
- brew install homeport/tap/dyff
- go install github.com/homeport/dyff/cmd/dyff@latest

Requirements and caveats from upstream:
- get Go (dyff requires Go version 1.23 or greater)

Basic usage or getting-started notes:
- export KUBECTL_EXTERNAL_DIFF="dyff between --omit-header --set-exit-code"
- kubectl diff [...]
- ![dyff between example with kubectl diff](.docs/dyff-between-kubectl-diff.png?raw=true "dyff in kubectl diff example")

- Source: https://github.com/homeport/dyff
- Extracted from upstream docs: https://raw.githubusercontent.com/homeport/dyff/HEAD/README.md

## Documentation

- https://github.com/homeport/dyff

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff/)
