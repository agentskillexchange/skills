---
title: Gate pull requests on OpenAPI breaking changes
description: Use oasdiff when an agent needs to compare old and new OpenAPI specs
  and decide whether a proposed change is safe to merge. The skill turns spec drift
  into a concrete breaking-change report that can block CI or annotate review workflows.
verification: security_reviewed
source: https://github.com/oasdiff/oasdiff
category:
- CI/CD Integrations
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: oasdiff/oasdiff
  github_stars: 1160
---

# Gate pull requests on OpenAPI breaking changes

Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gate-pull-requests-on-openapi-breaking-changes/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gate-pull-requests-on-openapi-breaking-changes
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gate-pull-requests-on-openapi-breaking-changes`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-on-openapi-breaking-changes/)
