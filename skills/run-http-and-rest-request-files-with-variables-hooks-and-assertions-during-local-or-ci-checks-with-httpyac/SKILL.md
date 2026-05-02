---
title: "Run .http and .rest request files with variables, hooks, and assertions during local or CI checks with httpYac"
description: "Execute repository-stored HTTP request files from the command line so API smoke tests, assertions, and environment-driven checks can run without a GUI client."
verification: "listed"
source: "https://github.com/AnWeber/httpyac"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "AnWeber/httpyac"
  github_stars: 809
  npm_package: "httpyac"
  npm_weekly_downloads: 36676
---

# Run .http and .rest request files with variables, hooks, and assertions during local or CI checks with httpYac

Use httpYac when an agent needs to run versioned .http or .rest request files with variables, tags, hooks, and assertions as part of a repeatable API check. It fits local preflight runs, CI smoke tests, and handoff workflows where the requests should stay in the repo instead of a hosted workspace.

This is skill-shaped because the job is not “use an API client” in the abstract. The bounded workflow is to execute scripted request files, filter which requests run, pass environment variables, and emit machine-usable results such as JSON or JUnit for downstream automation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-http-and-rest-request-files-with-variables-hooks-and-assertions-during-local-or-ci-checks-with-httpyac/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-http-and-rest-request-files-with-variables-hooks-and-assertions-during-local-or-ci-checks-with-httpyac
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-http-and-rest-request-files-with-variables-hooks-and-assertions-during-local-or-ci-checks-with-httpyac`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-http-and-rest-request-files-with-variables-hooks-and-assertions-during-local-or-ci-checks-with-httpyac/)
