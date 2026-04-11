---
title: "Update repository docs automatically after code changes and open review PRs"
description: "Use GitHub Next’s update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place."
verification: "listed"
source: "https://github.com/githubnext/agentics/blob/main/docs/update-docs.md"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
---

# Update repository docs automatically after code changes and open review PRs

Use GitHub Next’s update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/update-repository-docs-automatically-after-code-changes-and-open-review-prs/)
