---
name: "Draft release notes continuously with Release Drafter"
slug: "draft-release-notes-continuously-with-release-drafter"
description: "Keep a living release draft in GitHub so merged pull requests are organized into release notes before ship day."
github_stars: 3869
verification: "security_reviewed"
source: "https://github.com/release-drafter/release-drafter"
author: "Release Drafter maintainers"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "release-drafter/release-drafter"
  github_stars: 3869
---

# Draft release notes continuously with Release Drafter

Keep a living release draft in GitHub so merged pull requests are organized into release notes before ship day.

## Prerequisites

GitHub Actions, Release Drafter

## Installation

Use the upstream install or setup path that matches your environment:
- Before pushing, run npm run all to format, lint, type-check, test, and

Requirements and caveats from upstream:
- The action requires a configuration file. Default location is
- | filter-by-range | Optional | Filter releases that satisfies a semver range. Evaluates the tag name againts node's semver.satisfies(). Default : "*". |
- | $NEXT_PRERELEASE_VERSION | The next prerelease suffix. Depends on prerelease-identifier. Ex: v1.2.3-beta.3. Default : '' |

Basic usage or getting-started notes:
- You can use the
- [Release Drafter GitHub Action](https://github.com/marketplace/actions/release-drafter)
- in a

- Source: https://github.com/release-drafter/release-drafter
- Extracted from upstream docs: https://raw.githubusercontent.com/release-drafter/release-drafter/HEAD/README.md

## Documentation

- https://github.com/marketplace/actions/release-drafter

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/draft-release-notes-continuously-with-release-drafter/)
