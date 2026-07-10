---
name: "Git Secret Scanner"
slug: "git-secret-scanner"
description: "Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis."
github_stars: 26420
verification: "security_reviewed"
source: "https://github.com/gitleaks/gitleaks"
author: "gitleaks"
category: "Security & Verification"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "gitleaks/gitleaks"
  github_stars: 26420
---

# Git Secret Scanner

Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log --all -p analysis.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install gitleaks
- docker pull zricethezav/gitleaks:latest
- docker run -v ${path_to_host_folder_to_scan}:/path zricethezav/gitleaks:latest [COMMAND] [OPTIONS] [SOURCE_PATH]
- docker pull ghcr.io/gitleaks/gitleaks:latest

Requirements and caveats from upstream:
- [dockerhub]: https://hub.docker.com/r/zricethezav/gitleaks
- [dockerhub-badge]: https://img.shields.io/docker/pulls/zricethezav/gitleaks.svg
- [![Docker Hub][dockerhub-badge]][dockerhub]

Basic usage or getting-started notes:
- ### Installing
- bash
- # MacOS

- Source: https://github.com/gitleaks/gitleaks
- Extracted from upstream docs: https://raw.githubusercontent.com/gitleaks/gitleaks/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner/)
