---
title: "Update repository docs automatically after code changes and open review PRs"
description: "Use GitHub Next’s update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/update-docs.md"
category: ["CI/CD Integrations"]
framework: ["Multi-Framework"]
---

# Update repository docs automatically after code changes and open review PRs

Use GitHub Next’s update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/update-repository-docs-automatically-after-code-changes-and-open-review-prs/)
