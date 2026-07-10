---
name: "dust Intuitive Disk Usage Analyzer CLI"
slug: "dust-intuitive-disk-usage-analyzer-cli"
description: "A more intuitive version of the du command, written in Rust. dust instantly visualizes which directories consume the most disk space using colored proportional bars and smart recursive depth."
github_stars: 11500
verification: "security_reviewed"
source: "https://github.com/bootandy/dust"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "bootandy/dust"
  github_stars: 11500
---

# dust Intuitive Disk Usage Analyzer CLI

A more intuitive version of the du command, written in Rust. dust instantly visualizes which directories consume the most disk space using colored proportional bars and smart recursive depth.

## Installation

Requirements and caveats from upstream:
- Windows MSVC - requires: [VCRUNTIME140.dll](https://docs.microsoft.com/en-gb/cpp/windows/latest-supported-vc-redist?view=msvc-170)

Basic usage or getting-started notes:
- ![Example](media/snap.png)
- target/debug is the same size as target - so we know nearly all the disk usage of the 1.8G is in this folder
- target/debug/deps this is 1.2G - Note the bar jumps down to 70% to indicate that most disk usage is here but not all.

- Source: https://github.com/bootandy/dust
- Extracted from upstream docs: https://raw.githubusercontent.com/bootandy/dust/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dust-intuitive-disk-usage-analyzer-cli/)
