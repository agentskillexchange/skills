---
name: "yq YAML and Structured Data Processor"
slug: "yq-yaml-structured-data-processor"
description: "Process, query, and transform YAML, JSON, XML, CSV, TOML, and properties files from the command line using yq. Supports jq-like expressions for reading, updating, and converting between formats."
github_stars: 15143
verification: "security_reviewed"
source: "https://github.com/mikefarah/yq"
category: "Data Extraction & Transformation"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "mikefarah/yq"
  github_stars: 15143
---

# yq YAML and Structured Data Processor

Process, query, and transform YAML, JSON, XML, CSV, TOML, and properties files from the command line using yq. Supports jq-like expressions for reading, updating, and converting between formats.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install yq
- ### Run with Docker or Podman
- docker run --rm -v "${PWD}":/workdir mikefarah/yq '.a.b[0].c' file.yaml
- docker run --rm --security-opt=no-new-privileges --cap-drop all --network none \

Requirements and caveats from upstream:
- ![Build](https://github.com/mikefarah/yq/workflows/Build/badge.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/mikefarah/yq.svg) ![Github Releases (by Release)](https://img.shields.io/github/downloads/mikefar...
- yq is written in Go - so you can download a dependency free binary for your platform and you are good to go! If you prefer there are a variety of package managers that can be used as well as Docker and Podman, all lis...
- # Note: requires input file - add your file at the end

Basic usage or getting-started notes:
- ## Quick Usage Guide
- ### [Download the latest binary](https://github.com/mikefarah/yq/releases/latest)
- ### wget

- Source: https://github.com/mikefarah/yq
- Extracted from upstream docs: https://raw.githubusercontent.com/mikefarah/yq/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yq-yaml-structured-data-processor/)
