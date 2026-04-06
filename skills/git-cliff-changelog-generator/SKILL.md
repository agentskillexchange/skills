---
name: "git-cliff Customizable Changelog Generator for Git Repositories"
description: "git-cliff generates changelog files from Git history using conventional commits and regex-powered custom parsers. Written in Rust, it provides highly customizable templates via a TOML configuration file, with integrations for GitHub Actions, Docker, and CI/CD pipelines."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/orhun/git-cliff"
tool_ecosystem:
  github_repo: "https://github.com/orhun/git-cliff"
  github_stars: 11671
---
# git-cliff Customizable Changelog Generator for Git Repositories

git-cliff generates changelog files from Git history using conventional commits and regex-powered custom parsers. Written in Rust, it provides highly customizable templates via a TOML configuration file, with integrations for GitHub Actions, Docker, and CI/CD pipelines.

Overview

git-cliff is a highly customizable changelog generator that reads your Git commit history and produces structured changelogs following the Conventional Commits specification. Built in Rust for speed and reliability, git-cliff parses commits using conventional commit patterns or user-defined regex parsers, groups them by type (features, fixes, breaking changes, etc.), and renders the output through a flexible Tera template engine.

How It Works

At its core, git-cliff operates in three stages: parsing, grouping, and rendering. The parser scans Git history and matches each commit against configurable patterns defined in a cliff.toml file. Commits are then grouped into release contexts based on tags and version boundaries. Finally, the template engine renders these contexts into your desired changelog format—whether that is Markdown, Keep a Changelog, or a completely custom layout.

Key Features

- Conventional Commits Support: Automatically categorizes commits by type (feat, fix, docs, chore, etc.) following the conventional commit standard.

- Custom Parsers: Define regex-powered commit parsers for projects that do not follow conventional commit conventions.

- Template Engine: Uses Tera templates for full control over changelog output format, including variables for commit metadata, authors, dates, and links.

- Monorepo Support: Generate changelogs for specific packages within a monorepo by filtering commits to relevant paths.

- GitHub/GitLab Integration: Fetches additional metadata like PR numbers, contributor usernames, and release URLs from remote repositories.

- Bump Detection: Automatically determines the next semantic version based on commit types since the last tag.

Integration Points

git-cliff integrates into CI/CD pipelines via its official GitHub Action, Docker images, and pre-built binaries for Linux, macOS, and Windows. It can be installed via cargo, Homebrew, Scoop, pacman, and other package managers. The tool also provides a Rust library (git-cliff-core) for programmatic usage in custom tooling.

Agent Integration

Agents can use git-cliff as a CLI tool to automate release workflows: generating changelogs before publishing, computing the next version bump, or validating that recent commits follow project conventions. The TOML configuration and template system make it straightforward for agents to customize output without modifying source code.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-cliff-changelog-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-cliff-changelog-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-cliff-changelog-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-cliff-changelog-generator -a codex
```

### OpenClaw

```bash
clawhub install git-cliff-changelog-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-cliff-changelog-generator/)
