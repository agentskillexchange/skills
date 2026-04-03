---
name: "markdownlint-cli2 Markdown Linting for Docs and Repos"
description: "This skill uses markdownlint-cli2 to enforce consistent Markdown quality across docs, READMEs, and content repositories. It is built for local authoring, pull-request checks, and CI enforcement with rule-based output."
category: "Content Writing & SEO"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/DavidAnson/markdownlint-cli2"
tool_ecosystem:
  github_repo: "DavidAnson/markdownlint-cli2"
  github_stars: 740
  npm_package: "markdownlint-cli2"
  npm_weekly_downloads: 529196
---
# markdownlint-cli2 Markdown Linting for Docs and Repos

This skill uses markdownlint-cli2 to enforce consistent Markdown quality across docs, READMEs, and content repositories. It is built for local authoring, pull-request checks, and CI enforcement with rule-based output.

## Overview

markdownlint-cli2 is a fast command-line interface for linting Markdown and CommonMark files with the markdownlint rule engine. This skill turns the tool into a practical documentation quality gate for teams that manage READMEs, docs sites, knowledge bases, onboarding guides, changelogs, or content-heavy repositories. It focuses on repeatable rule enforcement: scan targeted globs, apply shared configuration, report rule IDs and line numbers, and fail CI when formatting or structure drifts away from the project standard.

The skill explains how to run markdownlint-cli2 across monorepos and docs folders, configure it with project-level settings, ignore generated paths, and combine it with pre-commit hooks or GitHub Actions. Typical checks include heading structure, list indentation, fenced code block formatting, blank-line rules, trailing spaces, and other CommonMark conventions that tend to create noisy reviews when handled manually. Because markdownlint-cli2 is designed around glob patterns and configuration files, it fits well into documentation pipelines that need deterministic output instead of ad hoc proofreading.

Outputs usually include machine-readable or terminal-readable violation reports showing file paths, rule codes, and exact lines that need attention. In some workflows the skill is paired with auto-fixable formatting tools, but its core role is standards enforcement and review reduction. Integration points include npm-based toolchains, Git hooks, CI/CD jobs, static site generators, docs portals, and engineering handbooks. If a repository depends on clean Markdown as part of shipping, reviewing, or publishing content, markdownlint-cli2 provides a solid rule-based layer for keeping that corpus consistent.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill markdownlint-cli2-markdown-linting-docs-repos
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill markdownlint-cli2-markdown-linting-docs-repos -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill markdownlint-cli2-markdown-linting-docs-repos -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill markdownlint-cli2-markdown-linting-docs-repos -a codex
```

### OpenClaw

```bash
clawhub install markdownlint-cli2-markdown-linting-docs-repos
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markdownlint-cli2-markdown-linting-docs-repos/)
