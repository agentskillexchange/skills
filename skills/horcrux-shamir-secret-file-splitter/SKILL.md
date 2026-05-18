---
name: "Horcrux Shamir Secret Sharing File Encryption and Splitting Tool"
slug: "horcrux-shamir-secret-file-splitter"
description: "Horcrux splits files into encrypted fragments using Shamir Secret Sharing, so you can distribute pieces across locations and reconstruct the original with a configurable threshold — no password required."
github_stars: 5041
verification: "security_reviewed"
source: "https://github.com/jesseduffield/horcrux"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "jesseduffield/horcrux"
  github_stars: 5041
---

# Horcrux Shamir Secret Sharing File Encryption and Splitting Tool

Horcrux splits files into encrypted fragments using Shamir Secret Sharing, so you can distribute pieces across locations and reconstruct the original with a configurable threshold — no password required.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install jesseduffield/horcrux/horcrux

Requirements and caveats from upstream:
- [Haystack](https://github.com/henrysdev/Haystack). Implements another file sharding and reassembly algorithm inspired by SSSS, but requires a password for reassembly and does not support thresholds of horcruxes.

Basic usage or getting-started notes:
- and it will prompt me for how many horcruxes I want, and how many will be needed to resurrect the original file. For example I might want 5 horcruxes with the ability to resurrect the file if I have any 3. The horcrux...
- via homebrew:
- via [scoop](https://scoop.sh/):

- Source: https://github.com/jesseduffield/horcrux
- Extracted from upstream docs: https://raw.githubusercontent.com/jesseduffield/horcrux/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/horcrux-shamir-secret-file-splitter/)
