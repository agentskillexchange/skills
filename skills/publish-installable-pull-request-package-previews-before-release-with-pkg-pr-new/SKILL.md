---
title: "Publish installable pull-request package previews before release with pkg.pr.new"
description: "Use pkg.pr.new when an agent needs an installable preview build from a pull request so reviewers can test a package before the maintainer cuts a real npm release."
verification: "security_reviewed"
source: "https://github.com/stackblitz-labs/pkg.pr.new"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stackblitz-labs/pkg.pr.new"
  github_stars: 1840
  ase_npm_package: "pkg-pr-new"
  npm_weekly_downloads: 387380
---

# Publish installable pull-request package previews before release with pkg.pr.new

pkg.pr.new gives an agent a narrow release-preview workflow. It builds package artifacts from commits or pull requests, exposes them through npm-compatible URLs, and lets reviewers install the preview immediately in downstream apps or reproduction repos. That is useful when the job is proving a library change in real conditions before merge or publish.


The boundary is clear enough to be skill-shaped. Invoke it when an agent needs temporary, installable PR previews for a package review or release workflow, not when the user wants a general package registry, CI platform, or npm publishing product. The job-to-be-done is preview-release distribution from pull requests without cutting a normal release.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/publish-installable-pull-request-package-previews-before-release-with-pkg-pr-new/)
