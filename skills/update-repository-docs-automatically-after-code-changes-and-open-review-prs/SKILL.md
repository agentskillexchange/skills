---
title: "Update repository docs automatically after code changes and open review PRs"
description: "Use GitHub Next's update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place."
verification: security_reviewed
source: "https://github.com/githubnext/agentics/blob/main/docs/update-docs.md"
---

# Update repository docs automatically after code changes and open review PRs

Use GitHub Next's update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/update-repository-docs-automatically-after-code-changes-and-open-review-prs/)
