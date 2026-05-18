---
name: "Harness Open Source Self-Hosted Git and CI/CD Development Platform"
slug: "harness-open-source-git-cicd-platform"
description: "Harness Open Source (formerly Gitness) is an end-to-end developer platform that integrates Git repository hosting, CI/CD pipelines, hosted development environments, and artifact registries in a single self-hosted binary."
github_stars: 34735
verification: "listed"
source: "https://github.com/harness/harness"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "harness/harness"
  github_stars: 34735
---

# Harness Open Source Self-Hosted Git and CI/CD Development Platform

Harness Open Source (formerly Gitness) is an end-to-end developer platform that integrates Git repository hosting, CI/CD pipelines, hosted development environments, and artifact registries in a single self-hosted binary.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -d \
- If your version is different than v3.21.11, run brew unlink protobuf
- $ make dep
- $ make tools

Requirements and caveats from upstream:
- The latest publicly released docker image can be found on [harness/harness](https://hub.docker.com/r/harness/harness).
- -v /var/run/docker.sock:/var/run/docker.sock \

Basic usage or getting-started notes:
- To install Harness yourself, simply run the command below. Once the container is up, you can visit http://localhost:3000 in your browser.
- Check if you've already installed protobuf protoc --version
- Get v3.21.11 curl -s https://raw.githubusercontent.com/Homebrew/homebrew-core/9de8de7a533609ebfded833480c1f7c05a3448cb/Formula/protobuf.rb > /tmp/protobuf.rb

- Source: https://github.com/harness/harness
- Extracted from upstream docs: https://raw.githubusercontent.com/harness/harness/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/harness-open-source-git-cicd-platform/)
