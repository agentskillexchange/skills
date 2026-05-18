---
name: "Format shell scripts into a stable house style before review with shfmt"
slug: "format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt"
description: "Normalize Bash, POSIX shell, and Zsh scripts before review or CI so style noise stops hiding the real changes."
github_stars: 8700
verification: "listed"
source: "https://github.com/mvdan/sh"
author: "mvdan"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "mvdan/sh"
  github_stars: 8700
---

# Format shell scripts into a stable house style before review with shfmt

Normalize Bash, POSIX shell, and Zsh scripts before review or CI so style noise stops hiding the real changes.

## Prerequisites

Go or packaged shfmt binary, shell script files, optional CI or pre-commit integration

## Installation

Use the upstream install or setup path that matches your environment:
- go install mvdan.cc/sh/v3/cmd/shfmt@latest
- go install mvdan.cc/sh/v3/cmd/gosh@latest
- docker build -t my:tag -f cmd/shfmt/Dockerfile .
- docker run --rm -u "$(id -u):$(id -g)" -v "$PWD:/mnt" -w /mnt my:tag <shfmt arguments>

Requirements and caveats from upstream:
- Supports [POSIX Shell], [Bash], [Zsh], and [mksh]. Requires Go 1.25 or later.
- Packages are available on [Alpine], [Arch], [Debian], [Docker], [Fedora], [FreeBSD],
- ### Docker

Basic usage or getting-started notes:
- To parse shell scripts, inspect them, and print them out,
- see the [syntax package](https://pkg.go.dev/mvdan.cc/sh/v3/syntax).
- For high-level operations like performing shell expansions on strings,

- Source: https://github.com/mvdan/sh
- Extracted from upstream docs: https://raw.githubusercontent.com/mvdan/sh/HEAD/README.md

## Documentation

- https://pkg.go.dev/mvdan.cc/sh/v3

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt/)
