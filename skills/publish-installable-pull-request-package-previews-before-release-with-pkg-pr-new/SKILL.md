---
name: "Publish installable pull-request package previews before release with pkg.pr.new"
slug: "publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new"
description: "Use pkg.pr.new when an agent needs an installable preview build from a pull request so reviewers can test a package before the maintainer cuts a real npm release."
github_stars: 1840
verification: "listed"
source: "https://github.com/stackblitz-labs/pkg.pr.new"
author: "StackBlitz Labs"
publisher_type: "company"
category: "CI/CD Integrations"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- npm i https://pkg.pr.new/tinylibs/tinybench/tinybench@a832a55
- Make sure it's installed on the repository before trying to publish a package. To read about the permissions the app needs, check [#305](https://github.com/stackblitz-labs/pkg.pr.new/issues/305).
- npm install --save-dev pkg-pr-new
- pnpm exec pkg-pr-new publish './packages/A' './packages/B' # or pnpm exec pkg-pr-new publish './packages/*'

Requirements and caveats from upstream:
- uses: actions/setup-node@v4
- node-version: 20

Basic usage or getting-started notes:
- First [install the GitHub Application](https://github.com/apps/pkg-pr-new).
- [!IMPORTANT]
- After installing on your repository, run pkg-pr-new from your lockfile in workflows (for example with pnpm exec pkg-pr-new publish) to get continuous releases.

- Source: https://github.com/stackblitz-labs/pkg.pr.new
- Extracted from upstream docs: https://raw.githubusercontent.com/stackblitz-labs/pkg.pr.new/HEAD/README.md

## Documentation

- https://pkg.pr.new

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new/)
