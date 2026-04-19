---
title: "Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis"
description: "Tool: github-to-sqlite from the Dogsheep project. This skill is for agents that need to turn live GitHub data into a durable local dataset before doing analysis, reporting, or follow-on automation. Instead of reading one issue page at a time or stitching together fragile API calls in memory, the agent uses github-to-sqlite to fetch issues, pull requests, issue comments, commits, releases, tags, contributors, repository lists, or workflow metadata into a SQLite database. That database becomes the working surface for SQL queries, audits, dashboards, changelog prep, triage reports, and historical snapshots. Invoke this when the job is bigger than normal GitHub browsing. Good examples include reviewing all open pull requests across an organization, building a release report from issues and merged PRs, taking a repeatable snapshot before a cleanup project, or joining GitHub records with other local tables. In those cases, a local mirror is more useful than the product UI because the agent can search, aggregate, diff, and export results without repeatedly hitting rate limits or losing context between requests. The scope boundary matters. This skill is not a generic GitHub SDK listing, and it is not for mutating GitHub state, reviewing code in the browser, or replacing gh for everyday one-off commands. Its job is narrower: fetch selected GitHub entities into SQLite so downstream agent work becomes deterministic and query-driven. Integration points are straightforward: a GitHub token can be supplied through auth.json or GITHUB_TOKEN ; the resulting database can be opened with SQLite tools, Datasette, Python, or any agent workflow that benefits from structured local records. That makes it a clean fit for research agents, reporting agents, release-prep agents, and repository health audits."
source: "https://github.com/dogsheep/github-to-sqlite"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dogsheep/github-to-sqlite"
  github_stars: 461
---

# Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis

Tool: github-to-sqlite from the Dogsheep project. This skill is for agents that need to turn live GitHub data into a durable local dataset before doing analysis, reporting, or follow-on automation. Instead of reading one issue page at a time or stitching together fragile API calls in memory, the agent uses github-to-sqlite to fetch issues, pull requests, issue comments, commits, releases, tags, contributors, repository lists, or workflow metadata into a SQLite database. That database becomes the working surface for SQL queries, audits, dashboards, changelog prep, triage reports, and historical snapshots. Invoke this when the job is bigger than normal GitHub browsing. Good examples include reviewing all open pull requests across an organization, building a release report from issues and merged PRs, taking a repeatable snapshot before a cleanup project, or joining GitHub records with other local tables. In those cases, a local mirror is more useful than the product UI because the agent can search, aggregate, diff, and export results without repeatedly hitting rate limits or losing context between requests. The scope boundary matters. This skill is not a generic GitHub SDK listing, and it is not for mutating GitHub state, reviewing code in the browser, or replacing gh for everyday one-off commands. Its job is narrower: fetch selected GitHub entities into SQLite so downstream agent work becomes deterministic and query-driven. Integration points are straightforward: a GitHub token can be supplied through auth.json or GITHUB_TOKEN ; the resulting database can be opened with SQLite tools, Datasette, Python, or any agent workflow that benefits from structured local records. That makes it a clean fit for research agents, reporting agents, release-prep agents, and repository health audits.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
