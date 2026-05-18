---
name: "Git Secrets Pre-Commit Scanner"
slug: "git-secrets-precommit-scanner"
description: "Scans git diffs for exposed secrets using truffleHog entropy detection and custom regex patterns. Integrates with pre-commit hooks and GitHub push protection API for real-time blocking."
github_stars: 26006
verification: "listed"
source: "https://github.com/trufflesecurity/trufflehog"
author: "trufflesecurity"
category: "Security & Verification"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "trufflesecurity/trufflehog"
  github_stars: 26006
---

# Git Secrets Pre-Commit Scanner

Scans git diffs for exposed secrets using truffleHog entropy detection and custom regex patterns. Integrates with pre-commit hooks and GitHub push protection API for real-time blocking.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
- brew install trufflehog
- docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
- docker run --rm -it -v "%cd:/=\%:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys

Requirements and caveats from upstream:
- ### Docker:
- <sub><i>_Ensure Docker engine is running before executing the following commands:_</i></sub>
- ### Using installation script, verify checksum signature (requires cosign to be installed)

Basic usage or getting-started notes:
- # :rocket: Quick Start
- Clone the git repo. For example [test keys](git@github.com:trufflesecurity/test_keys.git) repo.

- Source: https://github.com/trufflesecurity/trufflehog
- Extracted from upstream docs: https://raw.githubusercontent.com/trufflesecurity/trufflehog/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secrets-precommit-scanner/)
