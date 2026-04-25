---
title: "Diff YAML manifests semantically and surface meaningful drift before apply with dyff"
description: "Use dyff to compare YAML documents by structure and changed paths so agents can review configuration drift without the noise of plain line diffs."
verification: "listed"
source: "https://github.com/homeport/dyff"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "homeport/dyff"
  github_stars: 1800
---

# Diff YAML manifests semantically and surface meaningful drift before apply with dyff

Use dyff when an agent needs to compare YAML documents semantically, identify exactly which paths changed, and summarize meaningful drift before approving or applying config updates. Invoke this instead of plain `diff` when the real problem is structured review of YAML or JSON-like documents, not raw line-by-line text comparison. The scope boundary is tight and skill-shaped: dyff is a semantic structured-diff workflow for YAML change review and drift inspection, not a general YAML processor, generic viewer, or product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff/)
