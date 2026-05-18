---
name: "git-absorb Automatic Fixup Commit Generator"
slug: "git-absorb-automatic-fixup-commit-generator"
description: "Automatically generates fixup commits by analyzing staged changes and matching them to the correct ancestor commits. A Rust port of Facebook's hg absorb that eliminates manual interactive rebasing for review feedback."
github_stars: 5455
verification: "security_reviewed"
source: "https://github.com/tummychow/git-absorb"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "tummychow/git-absorb"
  github_stars: 5455
---

# git-absorb Automatic Fixup Commit Generator

Automatically generates fixup commits by analyzing staged changes and matching them to the correct ancestor commits. A Rust port of Facebook's hg absorb that eliminates manual interactive rebasing for review feedback.

## Installation

Use the upstream install or setup path that matches your environment:
- Note: cargo install does not currently know how to install manpages ([cargo#2729](https://github.com/rust-lang/cargo/issues/2729)), so if you use cargo for installation then git absorb --help will not work. There are...
- make

Requirements and caveats from upstream:
- This requires that the [a2x](https://asciidoc-py.github.io/a2x.1.html) tool be installed on your system.

Basic usage or getting-started notes:
- Facebook demoed hg absorb which is probably the coolest workflow enhancement I've seen to version control in years. Essentially, when your working directory has uncommitted changes on top of draft changesets, you can...
- Note that git absorb does _not_ use the system libgit2. This means you do not need to have libgit2 installed to build or run it. However, this does mean you have to be able to build libgit2. (Due to [recent changes](h...
- git add any changes that you want to absorb. By design, git absorb will only consider content in the git index (staging area).

- Source: https://github.com/tummychow/git-absorb
- Extracted from upstream docs: https://raw.githubusercontent.com/tummychow/git-absorb/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-absorb-automatic-fixup-commit-generator/)
