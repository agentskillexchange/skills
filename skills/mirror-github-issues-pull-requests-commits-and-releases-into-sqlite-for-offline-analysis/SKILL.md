---
title: "Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis"
description: "Use dogsheep/github-to-sqlite when an agent needs a local, queryable snapshot of GitHub activity instead of bouncing through the web UI or ad hoc API calls. The agent authenticates once, pulls the exact GitHub objects it needs, and leaves behind a SQLite database that can be inspected, joined, diffed, or handed to downstream tools."
verification: "security_reviewed"
source: "https://github.com/dogsheep/github-to-sqlite"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dogsheep/github-to-sqlite"
  github_stars: 461
---

# Mirror GitHub issues, pull requests, commits, and releases into SQLite for offline analysis

Tool: github-to-sqlite from the Dogsheep project.


This skill is for agents that need to turn live GitHub data into a durable local dataset before doing analysis, reporting, or follow-on automation. Instead of reading one issue page at a time or stitching together fragile API calls in memory, the agent uses github-to-sqlite to fetch issues, pull requests, issue comments, commits, releases, tags, contributors, repository lists, or workflow metadata into a SQLite database. That database becomes the working surface for SQL queries, audits, dashboards, changelog prep, triage reports, and historical snapshots.


Invoke this when the job is bigger than normal GitHub browsing. Good examples include reviewing all open pull requests across an organization, building a release report from issues and merged PRs, taking a repeatable snapshot before a cleanup project, or joining GitHub records with other local tables. In those cases, a local mirror is more useful than the product UI because the agent can search, aggregate, diff, and export results without repeatedly hitting rate limits or losing context between requests.


The scope boundary matters. This skill is not a generic GitHub SDK listing, and it is not for mutating GitHub state, reviewing code in the browser, or replacing gh for everyday one-off commands. Its job is narrower: fetch selected GitHub entities into SQLite so downstream agent work becomes deterministic and query-driven.


Integration points are straightforward: a GitHub token can be supplied through auth.json or GITHUB_TOKEN; the resulting database can be opened with SQLite tools, Datasette, Python, or any agent workflow that benefits from structured local records. That makes it a clean fit for research agents, reporting agents, release-prep agents, and repository health audits.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-github-issues-pull-requests-commits-and-releases-into-sqlite-for-offline-analysis/)
