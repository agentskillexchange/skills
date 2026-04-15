---
title: "Publish installable pull-request package previews before release with pkg.pr.new"
description: "Use pkg.pr.new when an agent needs an installable preview build from a pull request so reviewers can test a package before the maintainer cuts a real npm release."
verification: security_reviewed
source: "https://github.com/stackblitz-labs/pkg.pr.new"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stackblitz-labs/pkg.pr.new"
  github_stars: 1840
  npm_package: "pkg-pr-new"
  npm_weekly_downloads: 387380
---

# Publish installable pull-request package previews before release with pkg.pr.new

pkg.pr.new gives an agent a narrow release-preview workflow. It builds package artifacts from commits or pull requests, exposes them through npm-compatible URLs, and lets reviewers install the preview immediately in downstream apps or reproduction repos. That is useful when the job is proving a library change in real conditions before merge or publish.

The boundary is clear enough to be skill-shaped. Invoke it when an agent needs temporary, installable PR previews for a package review or release workflow, not when the user wants a general package registry, CI platform, or npm publishing product. The job-to-be-done is preview-release distribution from pull requests without cutting a normal release.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new/)
