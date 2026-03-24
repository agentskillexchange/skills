---
name: "NPM Package Changelog Analyzer"
description: "Analyzes NPM package changelogs and release notes using the NPM Registry API and GitHub Releases API. Detects breaking changes, security patches, and dependency conflicts across package upgrade paths."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/npm-package-changelog-analyzer/"
---

# NPM Package Changelog Analyzer

Analyzes NPM package changelogs and release notes using the NPM Registry API and GitHub Releases API. Detects breaking changes, security patches, and dependency conflicts across package upgrade paths.

## Overview

The NPM Package Changelog Analyzer skill provides intelligent analysis of package update histories to assist with dependency management decisions. It queries the NPM Registry API to retrieve version metadata, dist-tags, and time-stamped release information for any published package.

The skill cross-references changelog entries with the GitHub Releases API to correlate version bumps with pull request links, commit SHAs, and contributor information. It uses semver for semantic version range analysis and detects breaking changes by parsing conventional commit messages and BREAKING CHANGE footers.

Advanced capabilities include transitive dependency conflict detection by building resolution trees similar to npm ls, security advisory correlation with the GitHub Advisory Database API and npm audit signatures, peer dependency compatibility validation, and license change detection across versions. The skill generates upgrade impact reports with risk scores and suggested update ordering for monorepo environments using Lerna or Turborepo.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-changelog-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-changelog-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-changelog-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-changelog-analyzer -a codex
```

### OpenClaw

```bash
clawhub install npm-package-changelog-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/npm-package-changelog-analyzer/
