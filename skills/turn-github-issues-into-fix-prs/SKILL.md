---
title: "Turn GitHub Issues into Fix PRs"
description: "Use the gh-issues workflow to fetch filtered GitHub issues, spawn sub-agents for fixes, open PRs, and follow review comments. This is a bounded backlog-to-PR operator loop, not a general GitHub product listing."
verification: security_reviewed
source: "https://github.com/openclaw/openclaw/tree/main/skills/gh-issues"
category:
  - "Developer Tools"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/openclaw"
  github_stars: 356821
---

# Turn GitHub Issues into Fix PRs

Tool: gh-issues in OpenClaw

The gh-issues skill is an orchestration workflow for maintainers who want an agent to move from issue intake to working pull requests with less manual supervision. It fetches issues through the GitHub REST API, filters them by labels, milestone, assignee, and state, skips duplicates or already-claimed work, spawns coding sub-agents to implement fixes, opens PRs, and can keep watching for review comments that need follow-up changes.

Invoke this instead of using GitHub normally when the bottleneck is repetitive coordination. If a maintainer already knows the repo, has a token, and wants to clear a queue of bugs or routine tickets, the skill packages that operator playbook into a repeatable flow. The user is not asking for generic GitHub browsing or API access, but for a controlled automation that turns triaged issues into branches, commits, and PRs.

The boundary is narrow enough to stay skill-shaped. This is not a listing for GitHub itself, the gh CLI, or OpenClaw as a platform. It is specifically the issue-fetch, branch-claim, sub-agent, and PR-review loop encoded in the gh-issues workflow. Integration points are clear: GitHub REST API, local git checkout, GH_TOKEN, optional cron mode, and sub-agent runtimes for implementation and review-response passes.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-github-issues-into-fix-prs/)
