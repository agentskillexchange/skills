---
name: "Score open source repositories for supply-chain risk signals before adoption or release decisions with Scorecard"
slug: "score-open-source-repositories-for-supply-chain-risk-signals-before-adoption-or-release-decisions-with-scorecard"
description: "Check a repository against OpenSSF security heuristics before you trust it as a dependency, approve it for use, or ship from it."
github_stars: 5376
verification: "listed"
source: "https://github.com/ossf/scorecard"
author: "OpenSSF"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ossf/scorecard"
  github_stars: 5376
---

# Score open source repositories for supply-chain risk signals before adoption or release decisions with Scorecard

Check a repository against OpenSSF security heuristics before you trust it as a dependency, approve it for use, or ship from it.

## Prerequisites

Scorecard CLI or GitHub Action, network access to the target repository host, and optional GitHub authentication for higher API limits.

## Installation

Use the upstream install or setup path that matches your environment:
- docker pull ghcr.io/ossf/scorecard:latest
- docker pull ghcr.io/ossf/scorecard:v3.2.1
- docker run -e GITHUB_AUTH_TOKEN=token ghcr.io/ossf/scorecard:latest --show-details --repo=https://github.com/ossf/scorecard
- docker run -e GITHUB_AUTH_TOKEN=token ghcr.io/ossf/scorecard:v3.2.1 --show-details --repo=https://github.com/ossf/scorecard

Requirements and caveats from upstream:
- [Prerequisites](#prerequisites)
- projects the world depends on.
- If OSS consumers require certain behaviors from their dependencies,

Basic usage or getting-started notes:
- [Basic Usage](#basic-usage)
- Scorecard has been run on thousands of projects to monitor and track security
- For example:

- Source: https://github.com/ossf/scorecard
- Extracted from upstream docs: https://raw.githubusercontent.com/ossf/scorecard/HEAD/README.md

## Documentation

- https://scorecard.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/score-open-source-repositories-for-supply-chain-risk-signals-before-adoption-or-release-decisions-with-scorecard/)
