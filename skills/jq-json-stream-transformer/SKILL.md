---
name: "jq JSON Stream Transformer"
slug: "jq-json-stream-transformer"
description: "Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq's streaming parser."
github_stars: 34478
verification: "listed"
source: "https://github.com/jqlang/jq"
author: "jqlang"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "jqlang/jq"
  github_stars: 34478
---

# jq JSON Stream Transformer

Constructs complex jq filter expressions for transforming JSON/NDJSON streams, including recursive descent, object construction, and reduce operations. Handles multi-gigabyte streams with jq's streaming parser.

## Installation

Use the upstream install or setup path that matches your environment:
- #### Run with Docker
- docker run --rm -i ghcr.io/jqlang/jq:latest < package.json '.version'
- docker run --rm -i -v "$PWD:$PWD" -w "$PWD" ghcr.io/jqlang/jq:latest '.version' package.json
- make clean # if upgrading from a version previously built from source

Requirements and caveats from upstream:
- ### Docker Image
- Pull the [jq image](https://github.com/jqlang/jq/pkgs/container/jq) to start quickly with Docker.

Basic usage or getting-started notes:
- ### Prebuilt Binaries
- Download the latest releases from the [GitHub release page](https://github.com/jqlang/jq/releases).
- ##### Example: Extracting the version from a package.json file

- Source: https://github.com/jqlang/jq
- Extracted from upstream docs: https://raw.githubusercontent.com/jqlang/jq/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jq-json-stream-transformer/)
