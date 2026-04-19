---
title: "Turn GitHub Issues into Fix PRs"
description: "Tool: gh-issues in OpenClaw The gh-issues skill is an orchestration workflow for maintainers who want an agent to move from issue intake to working pull requests with less manual supervision. It fetches issues through the GitHub REST API, filters them by labels, milestone, assignee, and state, skips duplicates or already-claimed work, spawns coding sub-agents to implement fixes, opens PRs, and can keep watching for review comments that need follow-up changes. Invoke this instead of using GitHub normally when the bottleneck is repetitive coordination. If a maintainer already knows the repo, has a token, and wants to clear a queue of bugs or routine tickets, the skill packages that operator playbook into a repeatable flow. The user is not asking for generic GitHub browsing or API access, but for a controlled automation that turns triaged issues into branches, commits, and PRs. The boundary is narrow enough to stay skill-shaped. This is not a listing for GitHub itself, the gh CLI, or OpenClaw as a platform. It is specifically the issue-fetch, branch-claim, sub-agent, and PR-review loop encoded in the gh-issues workflow. Integration points are clear: GitHub REST API, local git checkout, GH_TOKEN, optional cron mode, and sub-agent runtimes for implementation and review-response passes."
source: "https://github.com/openclaw/openclaw/tree/main/skills/gh-issues"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/openclaw"
  github_stars: 356821
---

# Turn GitHub Issues into Fix PRs

Tool: gh-issues in OpenClaw The gh-issues skill is an orchestration workflow for maintainers who want an agent to move from issue intake to working pull requests with less manual supervision. It fetches issues through the GitHub REST API, filters them by labels, milestone, assignee, and state, skips duplicates or already-claimed work, spawns coding sub-agents to implement fixes, opens PRs, and can keep watching for review comments that need follow-up changes. Invoke this instead of using GitHub normally when the bottleneck is repetitive coordination. If a maintainer already knows the repo, has a token, and wants to clear a queue of bugs or routine tickets, the skill packages that operator playbook into a repeatable flow. The user is not asking for generic GitHub browsing or API access, but for a controlled automation that turns triaged issues into branches, commits, and PRs. The boundary is narrow enough to stay skill-shaped. This is not a listing for GitHub itself, the gh CLI, or OpenClaw as a platform. It is specifically the issue-fetch, branch-claim, sub-agent, and PR-review loop encoded in the gh-issues workflow. Integration points are clear: GitHub REST API, local git checkout, GH_TOKEN, optional cron mode, and sub-agent runtimes for implementation and review-response passes.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-github-issues-into-fix-prs/)
