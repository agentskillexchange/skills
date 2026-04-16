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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diff-yaml-manifests-semantically-and-surface-meaningful-drift-before-apply-with-dyff/)
