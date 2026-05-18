---
name: "Post linter and analyzer findings back into pull requests"
slug: "post-linter-and-analyzer-findings-back-into-pull-requests"
description: "This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI."
github_stars: 9207
verification: "listed"
source: "https://github.com/reviewdog/reviewdog"
author: "reviewdog"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "reviewdog/reviewdog"
  github_stars: 9207
---

# Post linter and analyzer findings back into pull requests

This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI.

## Prerequisites

One or more linters or analyzers that emit machine-readable diagnostics, plus local git diff or CI pull request context

## Installation

Use the upstream install or setup path that matches your environment:
- $ brew install reviewdog/tap/reviewdog
- $ brew upgrade reviewdog/tap/reviewdog
- $ go install github.com/reviewdog/reviewdog/cmd/reviewdog@latest
- $ npm install --save-dev eslint-formatter-rdjson

Requirements and caveats from upstream:
- As described above, github-pr-check reporter with Option 2 depends on
- This reporter requires a valid GitHub API token to generate a diff, but will not
- Docker

Basic usage or getting-started notes:
- shell
- # Specify installation directory ($(go env GOPATH)/bin/) and version.
- # In alpine linux (as it does not come with curl by default)

- Source: https://github.com/reviewdog/reviewdog
- Extracted from upstream docs: https://raw.githubusercontent.com/reviewdog/reviewdog/HEAD/README.md

## Documentation

- https://github.com/reviewdog/reviewdog/blob/master/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/post-linter-and-analyzer-findings-back-into-pull-requests/)
