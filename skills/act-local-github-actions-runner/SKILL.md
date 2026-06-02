---
name: "act Local GitHub Actions Runner"
slug: "act-local-github-actions-runner"
description: "act is an open-source CLI tool that runs GitHub Actions workflows locally using Docker, enabling fast feedback on workflow changes without pushing to GitHub. It is a standard tool for local Actions development and testing."
github_stars: 69661
verification: "security_reviewed"
source: "https://github.com/nektos/act"
category: "CI/CD Integrations"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "nektos/act"
  github_stars: 69661
---

# act Local GitHub Actions Runner

act is an open-source CLI tool that runs GitHub Actions workflows locally using Docker, enabling fast feedback on workflow changes without pushing to GitHub. It is a standard tool for local Actions development and testing.

## Installation

Use the upstream install or setup path that matches your environment:
- Install Docker first. On macOS, use Docker Desktop. On Linux, install Docker Engine.
- On macOS, install act with Homebrew: \`brew install act\`
- git clone https://github.com/nektos/act.git
- make build

Requirements and caveats from upstream:
- act depends on the Docker Engine API to run workflows in containers.
- Jobs that do not require container isolation can be run directly on the host runner when that fits the workflow.

Basic usage or getting-started notes:
- Run all local workflow jobs: \`act\`
- Run a specific job: \`act -j <job>\`

- Source: https://github.com/nektos/act
- Extracted from upstream docs: https://nektosact.com/installation/index.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/act-local-github-actions-runner/)
