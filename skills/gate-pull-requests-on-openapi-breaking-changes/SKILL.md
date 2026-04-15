---
title: "Gate pull requests on OpenAPI breaking changes"
description: "Use oasdiff when an agent needs to compare old and new OpenAPI specs and decide whether a proposed change is safe to merge. The skill turns spec drift into a concrete breaking-change report that can block CI or annotate review workflows."
verification: security_reviewed
source: "https://github.com/oasdiff/oasdiff"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
---

# Gate pull requests on OpenAPI breaking changes

This skill uses oasdiff, the open source OpenAPI diff engine, to compare two API specifications and classify the changes that matter for compatibility. An agent invokes it when reviewing a pull request, release branch, or generated spec artifact and needs to answer a focused question: did this change introduce a breaking contract change, and if so, where?

The boundary here matters. This is not a generic OpenAPI viewer, SDK generator, or documentation platform entry. The agent is carrying out a specific CI and code review job: collect a baseline spec and a candidate spec, run a diff, interpret the breaking-change rules, and surface only the compatibility-impacting results. If the user simply wants to browse or author an OpenAPI file, that is outside this skill.

Use it in release gates, API governance workflows, and repository automation where compatibility promises matter. Integration points include the oasdiff CLI, Go package usage, GitHub pull request checks, and any pipeline that stores a previous spec snapshot. The output is valuable to agents because it is already scoped to reviewable decisions: added or removed operations, parameter changes, response schema drift, enum tightening, security requirement changes, and other contract deltas. An agent can attach the report to a review, fail CI on configured rules, or request a version bump when the API surface changed in a non-backward-compatible way.

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
