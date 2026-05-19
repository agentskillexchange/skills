---
name: "SAST Pipeline Scanner"
slug: "sast-pipeline-scanner"
description: "Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management."
github_stars: 14922
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
author: "Semgrep"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14922
---

# SAST Pipeline Scanner

Runs static application security testing using Semgrep rules and CodeQL queries against pull request diffs. Supports SARIF output format and integrates with GitHub Advanced Security for findings management.

## Installation

Use the upstream install or setup path that matches your environment:
- $ brew install semgrep
- $ docker run -it -v "${PWD}:/src" semgrep/semgrep semgrep login
- $ docker run -e SEMGREP_APP_TOKEN=<TOKEN> --rm -v "${PWD}:/src" semgrep/semgrep semgrep ci
- $ brew upgrade semgrep

Requirements and caveats from upstream:
- <a href="https://hub.docker.com/r/semgrep/semgrep">
- <img src="https://img.shields.io/docker/pulls/semgrep/semgrep.svg?style=flat-square" alt="Docker Pulls" />
- <img src="https://img.shields.io/docker/pulls/semgrep/semgrep.svg?style=flat-square" alt="Docker Pulls (Old)" />

Basic usage or getting-started notes:
- Semgrep is a fast, open-source, static analysis tool that searches code, finds bugs, and enforces secure guardrails and coding standards. Semgrep [supports 30+ languages](#language-support) and can run in an IDE, as a...
- [From the Semgrep AppSec Platform](#option-1-getting-started-from-the-semgrep-appsec-platform-recommended)
- [From the CLI](#option-2-getting-started-from-the-cli)

- Source: https://github.com/semgrep/semgrep
- Extracted from upstream docs: https://raw.githubusercontent.com/semgrep/semgrep/HEAD/README.md

## Documentation

- https://semgrep.dev/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-pipeline-scanner/)
