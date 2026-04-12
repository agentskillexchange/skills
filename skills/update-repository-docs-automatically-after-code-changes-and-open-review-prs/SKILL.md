---
title: "Update repository docs automatically after code changes and open review PRs"
slug: "update-repository-docs-automatically-after-code-changes-and-open-review-prs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
source: "https://github.com/githubnext/agentics/blob/main/docs/update-docs.md"
---

# Update repository docs automatically after code changes and open review PRs

Use GitHub Next’s update-docs workflow when code changes should trigger documentation maintenance instead of waiting for humans to remember it later. The agent analyzes what changed, generates the missing docs updates, and opens a reviewable PR rather than silently rewriting the docs in place.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/update-repository-docs-automatically-after-code-changes-and-open-review-prs/)
