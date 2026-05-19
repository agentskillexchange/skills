---
name: "Git Secret Scanner with Gitleaks"
slug: "git-secret-scanner-gitleaks"
description: "Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history."
github_stars: 26101
verification: "security_reviewed"
source: "https://github.com/gitleaks/gitleaks"
author: "Gitleaks"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "gitleaks/gitleaks"
  github_stars: 26101
---

# Git Secret Scanner with Gitleaks

Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history.

## Prerequisites

Git

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

## Documentation

- https://github.com/gitleaks/gitleaks#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
