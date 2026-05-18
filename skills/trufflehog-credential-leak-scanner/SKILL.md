---
name: "TruffleHog Credential Leak Scanner"
slug: "trufflehog-credential-leak-scanner"
description: "Find, verify, and analyze leaked credentials across Git repositories, Slack, Jira, Docker images, and more using TruffleHog. Classifies 800+ secret types and validates whether discovered credentials are live."
github_stars: 25299
verification: "listed"
source: "https://github.com/trufflesecurity/trufflehog"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "trufflesecurity/trufflehog"
  github_stars: 25299
---

# TruffleHog Credential Leak Scanner

Find, verify, and analyze leaked credentials across Git repositories, Slack, Jira, Docker images, and more using TruffleHog. Classifies 800+ secret types and validates whether discovered credentials are live.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trufflehog-credential-leak-scanner/)
