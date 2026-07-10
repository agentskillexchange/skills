---
name: "Generate release PRs and changelog updates from Conventional Commits"
slug: "generate-release-prs-and-changelog-updates-from-conventional-commits"
description: "Use release-please when an agent should turn merged Conventional Commits into structured release PRs, version bumps, and changelog updates before a human reviews and merges. This is a release-management workflow, not a generic package or CI listing."
github_stars: 6700
verification: "security_reviewed"
source: "https://github.com/googleapis/release-please"
author: "Google APIs"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "googleapis/release-please"
  github_stars: 6700
  npm_package: "release-please"
  npm_weekly_downloads: 162701
---

# Generate release PRs and changelog updates from Conventional Commits

Use release-please when an agent should turn merged Conventional Commits into structured release PRs, version bumps, and changelog updates before a human reviews and merges. This is a release-management workflow, not a generic package or CI listing.

## Prerequisites

GitHub, Conventional Commits

## Installation

Use the upstream install or setup path that matches your environment:
- make sense when merged in the main branch. For example, you may have

Requirements and caveats from upstream:
- "docs" is a prefix for releasable units in Java and Python.
- | node | [A Node.js repository, with a package.json and CHANGELOG.md](https://github.com/yargs/yargs) |
- | python | [A Python repository with a pyproject.toml, &lt;project&gt;/\_\_init\_\_.py, CHANGELOG.md or optionally a setup.py, setup.cfg](https://github.com/googleapis/python-storage) |

Basic usage or getting-started notes:
- Updates your changelog file (for example CHANGELOG.md), along with other language specific files (for example package.json).
- **Empty commit example:**
- Some languages have their specific releasable unit configuration. For example,

- Source: https://github.com/googleapis/release-please
- Extracted from upstream docs: https://raw.githubusercontent.com/googleapis/release-please/HEAD/README.md

## Documentation

- https://github.com/googleapis/release-please

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-release-prs-and-changelog-updates-from-conventional-commits/)
