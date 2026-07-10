---
name: "Dockerfile Security Hardening Advisor"
slug: "dockerfile-security-hardening-advisor"
description: "Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy container scanner. Recommends hardening steps based on CIS Docker Benchmark and Snyk container advisories."
github_stars: 12100
verification: "security_reviewed"
source: "https://github.com/hadolint/hadolint"
author: "hadolint"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "hadolint/hadolint"
  github_stars: 12100
---

# Dockerfile Security Hardening Advisor

Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy container scanner. Recommends hardening steps based on CIS Docker Benchmark and Snyk container advisories.

## Installation

Use the upstream install or setup path that matches your environment:
- Docker comes to the rescue, providing an easy way how to run hadolint on most
- docker run --rm -i hadolint/hadolint < Dockerfile
- docker run --rm -i ghcr.io/hadolint/hadolint < Dockerfile
- brew install hadolint

Requirements and caveats from upstream:
- [![Docker pulls][docker-img]][docker]
- A smarter Dockerfile linter that helps you build [best practice][] Docker
- Just pipe your Dockerfile to docker run:

Basic usage or getting-started notes:
- the Bash code inside RUN instructions.
- You can run hadolint locally to lint your Dockerfile.
- podman run --rm -i ghcr.io/hadolint/hadolint < Dockerfile

- Source: https://github.com/hadolint/hadolint
- Extracted from upstream docs: https://raw.githubusercontent.com/hadolint/hadolint/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/)
