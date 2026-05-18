---
name: "SAST Rule Compiler for Semgrep"
slug: "sast-rule-compiler-semgrep"
description: "Compiles and validates custom Semgrep SAST rules using the semgrep-core engine. Tests pattern matching against sample codebases and generates rule performance benchmarks with p/ci rulesets."
github_stars: 14802
verification: "listed"
source: "https://github.com/semgrep/semgrep"
category: "Security & Verification"
framework: "Codex"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14802
---

# SAST Rule Compiler for Semgrep

Compiles and validates custom Semgrep SAST rules using the semgrep-core engine. Tests pattern matching against sample codebases and generates rule performance benchmarks with p/ci rulesets.

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

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sast-rule-compiler-semgrep/)
