---
title: "Gate pull requests on OpenAPI breaking changes"
description: "Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows."
verification: security_reviewed
source: "https://github.com/oasdiff/oasdiff"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oasdiff/oasdiff"
  github_stars: 1160
---

# Gate pull requests on OpenAPI breaking changes

Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gate-pull-requests-on-openapi-breaking-changes
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gate-pull-requests-on-openapi-breaking-changes` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-on-openapi-breaking-changes/)
