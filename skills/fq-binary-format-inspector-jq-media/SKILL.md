---
name: "fq Binary Format Inspector and jq for Media Files"
slug: "fq-binary-format-inspector-jq-media"
description: "fq is a command-line tool that brings jq-style querying to binary formats. It decodes, inspects, and transforms media containers, executables, packet captures, and dozens of other binary formats using familiar jq expressions and an interactive REPL."
github_stars: 10468
verification: "security_reviewed"
source: "https://github.com/wader/fq"
author: "Mattias Wadman"
publisher_type: "Individual Developer"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "wader/fq"
  github_stars: 10468
---

# fq Binary Format Inspector and jq for Media Files

fq is a command-line tool that brings jq-style querying to binary formats. It decodes, inspects, and transforms media containers, executables, packet captures, and dozens of other binary formats using familiar jq expressions and an interactive REPL.

## Prerequisites

Go 1.22+

## Installation

Use the upstream install or setup path that matches your environment:
- brew install wader/tap/fq
- Make sure you have [go](https://go.dev) 1.22 or later installed.
- go install github.com/wader/fq@latest
- go install github.com/wader/fq@master

Requirements and caveats from upstream:
- [hachoir](https://github.com/vstinner/hachoir) - General python library for working binary data.

Basic usage or getting-started notes:
- Basic usage is fq . file, fq d file or fq 'some query' file ....
- For details see [usage.md](doc/usage.md).
- For details see [formats.md](doc/formats.md) and [usage.md](doc/usage.md).

- Source: https://github.com/wader/fq
- Extracted from upstream docs: https://raw.githubusercontent.com/wader/fq/HEAD/README.md

## Documentation

- https://github.com/wader/fq/blob/master/doc/usage.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fq-binary-format-inspector-jq-media/)
