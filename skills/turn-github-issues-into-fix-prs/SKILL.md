---
title: "Turn GitHub Issues into Fix PRs"
description: "Use the gh-issues workflow to fetch filtered GitHub issues, spawn sub-agents for fixes, open PRs, and follow review comments. This is a bounded backlog-to-PR operator loop, not a general GitHub product listing."
verification: "security_reviewed"
source: "https://github.com/openclaw/openclaw/tree/main/skills/gh-issues"
category: ["Developer Tools"]
framework: ["OpenClaw"]
---

# Turn GitHub Issues into Fix PRs

Use the gh-issues workflow to fetch filtered GitHub issues, spawn sub-agents for fixes, open PRs, and follow review comments. This is a bounded backlog-to-PR operator loop, not a general GitHub product listing.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-github-issues-into-fix-prs/)
