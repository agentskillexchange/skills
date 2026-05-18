---
name: "act Local GitHub Actions Runner"
slug: "act-local-github-actions-runner"
description: "act is an open-source CLI tool that runs GitHub Actions workflows locally using Docker, enabling fast feedback on workflow changes without pushing to GitHub. With 57,000+ stars on GitHub, it is the standard tool for local Actions development and testing."
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

act is an open-source CLI tool that runs GitHub Actions workflows locally using Docker, enabling fast feedback on workflow changes without pushing to GitHub. With 57,000+ stars on GitHub, it is the standard tool for local Actions development and testing.

## Installation

Use the upstream install or setup path that matches your environment:
- Install Docker first. act depends on the Docker Engine API for container-backed workflow runs.
- On macOS or Linux with Homebrew, install act with: `brew install act`
- To build from source: `git clone https://github.com/nektos/act.git && cd act && make build`
- Run workflows locally from a repository with GitHub Actions configured: `act`

Requirements and caveats from upstream:
- Docker Desktop is the documented Docker path for macOS and Windows.
- Linux users need Docker Engine when running container-backed jobs.
- act is not officially supported with podman or other container backends.

Basic usage or getting-started notes:
- Run `act` from a repository root to read workflows from `.github/workflows/`.
- Use act for fast local feedback before pushing workflow changes to GitHub.

- Source: https://github.com/nektos/act
- Extracted from upstream docs: https://nektosact.com/installation/index.html and https://nektosact.com/usage/index.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/act-local-github-actions-runner/)
