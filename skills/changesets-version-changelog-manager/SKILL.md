---
title: Changesets Version and Changelog Manager
description: Overview Changesets is a tool for managing versioning and changelogs
  with a focus on multi-package repositories (monorepos). Created and battle-tested
  by the Atlassian team, Changesets provides a structured workflow where contributors
  declare how their changes should be released, and the tool automates version bumps,
  changelog updates, and package publishing. The core concept is the “changeset” —
  a markdown file that describes an intent to release one or more packages at specific
  semver bump levels (major, minor, or patch) along with a human-readable summary.
  Multiple changesets accumulate over time and are combined into a single release
  that correctly handles internal dependency relationships between packages in a monorepo.
  How It Works The @changesets/cli package provides the command-line interface. When
  a developer makes a change, they run npx changeset which prompts them to select
  affected packages, choose bump types, and write a summary. This creates a markdown
  file in a .changeset directory that gets committed with the code change. At release
  time, running npx changeset version consumes all pending changeset files, calculates
  the final version bump for each package (flattening multiple changesets into a single
  bump), updates package.json versions, adjusts internal dependency references, and
  generates changelog entries. Then npx changeset publish publishes all updated packages
  to npm. Automation and Integration Changesets provides a GitHub bot that checks
  PRs for changeset files and a GitHub Action that automates the entire release flow
  by creating versioning pull requests and optionally publishing packages. The project
  is used by Atlaskit, Emotion, Keystone, XState, pnpm, React Select, and many other
  major open source projects. With over 11,000 GitHub stars and a rich ecosystem of
  plugins for custom changelog formats, Changesets is the standard tool for monorepo
  release management in the JavaScript ecosystem.
verification: security_reviewed
source: https://github.com/changesets/changesets
category:
- Developer Tools
framework:
- Claude Code
tool_ecosystem:
  github_repo: changesets/changesets
  github_stars: 11620
  npm_package: '@changesets/cli'
  npm_weekly_downloads: 2420314
---

# Changesets Version and Changelog Manager

Overview Changesets is a tool for managing versioning and changelogs with a focus on multi-package repositories (monorepos). Created and battle-tested by the Atlassian team, Changesets provides a structured workflow where contributors declare how their changes should be released, and the tool automates version bumps, changelog updates, and package publishing. The core concept is the “changeset” — a markdown file that describes an intent to release one or more packages at specific semver bump levels (major, minor, or patch) along with a human-readable summary. Multiple changesets accumulate over time and are combined into a single release that correctly handles internal dependency relationships between packages in a monorepo. How It Works The @changesets/cli package provides the command-line interface. When a developer makes a change, they run npx changeset which prompts them to select affected packages, choose bump types, and write a summary. This creates a markdown file in a .changeset directory that gets committed with the code change. At release time, running npx changeset version consumes all pending changeset files, calculates the final version bump for each package (flattening multiple changesets into a single bump), updates package.json versions, adjusts internal dependency references, and generates changelog entries. Then npx changeset publish publishes all updated packages to npm. Automation and Integration Changesets provides a GitHub bot that checks PRs for changeset files and a GitHub Action that automates the entire release flow by creating versioning pull requests and optionally publishing packages. The project is used by Atlaskit, Emotion, Keystone, XState, pnpm, React Select, and many other major open source projects. With over 11,000 GitHub stars and a rich ecosystem of plugins for custom changelog formats, Changesets is the standard tool for monorepo release management in the JavaScript ecosystem.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/changesets-version-changelog-manager/)
