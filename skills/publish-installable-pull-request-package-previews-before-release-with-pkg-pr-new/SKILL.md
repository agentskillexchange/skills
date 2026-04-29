---
title: "Publish installable pull-request package previews before release with pkg.pr.new"
description: "Use pkg.pr.new when an agent needs an installable preview build from a pull request so reviewers can test a package before the maintainer cuts a real npm release."
verification: "security_reviewed"
source: "https://github.com/stackblitz-labs/pkg.pr.new"
author: "StackBlitz Labs"
publisher_type: "company"
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

Use pkg.pr.new when an agent needs an installable preview build from a pull request so reviewers can test a package before the maintainer cuts a real npm release.

## Prerequisites

A GitHub repository with Actions enabled, the pkg.pr.new GitHub App installed, Node.js/npm for the package build, and a package that can be built from CI.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install the <a href="https://github.com/apps/pkg-pr-new">pkg.pr.new GitHub App</a> on the repository, then add <code>npx pkg-pr-new publish</code> or a dev dependency on <code>pkg-pr-new</code> to your CI workflow. For monorepos, run the publish command once with all package paths so one workflow generates all preview URLs.</p>
```

## Documentation

- https://pkg.pr.new

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new/)
