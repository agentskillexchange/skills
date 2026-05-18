---
name: "Generate structured release notes from merged pull requests between two refs with Copilot Release Notes"
slug: "generate-structured-release-notes-from-merged-pull-requests-between-two-refs-with-copilot-release-notes"
description: "Compare two tags, branches, or SHAs and turn merged pull requests into reviewable markdown and JSON release notes for a release workflow."
github_stars: 2
verification: "listed"
source: "https://github.com/github/copilot-release-notes"
author: "GitHub"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "github/copilot-release-notes"
  github_stars: 2
---

# Generate structured release notes from merged pull requests between two refs with Copilot Release Notes

Compare two tags, branches, or SHAs and turn merged pull requests into reviewable markdown and JSON release notes for a release workflow.

## Prerequisites

GitHub Actions runner, checked-out git history for the compared refs, GitHub Copilot license, fine-grained PAT with Copilot Requests read permission

## Installation

Use the upstream install or setup path that matches your environment:
- npm install
- npm test # run 42 unit tests
- npx ncc build src/index.ts -o dist # rebuild dist/

Requirements and caveats from upstream:
- This action requires a COPILOT_GITHUB_TOKEN — a GitHub fine-grained personal access token with the **"Copilot Requests: Read"** permission. The token owner must have an active GitHub Copilot license.
- Uses the GitHub API to find PRs associated with commits. Catches more PR types but requires API access and is slower for large ranges.

Basic usage or getting-started notes:
- A **GitHub Actions** runner (Ubuntu, macOS, or Windows)
- An active **GitHub Copilot license**
- A **fine-grained PAT** with the Copilot Requests: Read permission (see [Authentication](#authentication))

- Source: https://github.com/github/copilot-release-notes
- Extracted from upstream docs: https://raw.githubusercontent.com/github/copilot-release-notes/HEAD/README.md

## Documentation

- https://github.com/github/copilot-release-notes

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-structured-release-notes-from-merged-pull-requests-between-two-refs-with-copilot-release-notes/)
