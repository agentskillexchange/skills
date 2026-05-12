---
title: "Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild"
slug: "verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild"
description: "Query OSS Rebuild attestations and rebuild metadata so an agent can verify whether a published package artifact matches a reproducible upstream rebuild."
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
go install github.com/google/oss-rebuild/cmd/oss-rebuild@latest
```

## Documentation

- https://docs.oss-rebuild.dev/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild/)
