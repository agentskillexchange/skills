---
title: "git-cliff Customizable Changelog Generator for Git Repositories"
description: "git-cliff generates changelog files from Git history using conventional commits and regex-powered custom parsers. Written in Rust, it provides highly customizable templates via a TOML configuration file, with integrations for GitHub Actions, Docker, and CI/CD pipelines."
slug: "git-cliff-changelog-generator"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/orhun/git-cliff"
tool_ecosystem:
  github_repo: "orhun/git-cliff"
  github_stars: 11678
listed: true
---

# git-cliff Customizable Changelog Generator for Git Repositories

git-cliff generates changelog files from Git history using conventional commits and regex-powered custom parsers. Written in Rust, it provides highly customizable templates via a TOML configuration file, with integrations for GitHub Actions, Docker, and CI/CD pipelines.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install git-cliff-changelog-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

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

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-cliff-changelog-generator/)
