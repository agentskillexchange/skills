---
name: NPM Package Changelog Analyzer
description: Analyzes NPM package changelogs and release notes using the NPM Registry
  API and GitHub Releases API. Detects breaking changes, security patches, and dependency
  conflicts across package upgrade paths.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-package-changelog-analyzer/
category:
- Library &amp; API Reference
framework:
- Cursor
---
# NPM Package Changelog Analyzer

The NPM Package Changelog Analyzer skill provides intelligent analysis of package update histories to assist with dependency management decisions. It queries the NPM Registry API to retrieve version metadata, dist-tags, and time-stamped release information for any published package.
The skill cross-references changelog entries with the GitHub Releases API to correlate version bumps with pull request links, commit SHAs, and contributor information. It uses semver for semantic version range analysis and detects breaking changes by parsing conventional commit messages and BREAKING CHANGE footers.
Advanced capabilities include transitive dependency conflict detection by building resolution trees similar to npm ls, security advisory correlation with the GitHub Advisory Database API and npm audit signatures, peer dependency compatibility validation, and license change detection across versions. The skill generates upgrade impact reports with risk scores and suggested update ordering for monorepo environments using Lerna or Turborepo.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-changelog-analyzer/)
