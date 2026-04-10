---
title: "git-absorb Automatic Fixup Commit Generator"
description: "Automatically generates fixup commits by analyzing staged changes and matching them to the correct ancestor commits. A Rust port of Facebook’s hg absorb that eliminates manual interactive rebasing for review feedback."
slug: "git-absorb-automatic-fixup-commit-generator"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/tummychow/git-absorb"
tool_ecosystem:
  github_repo: "tummychow/git-absorb"
  github_stars: 5455
listed: true
---

# git-absorb Automatic Fixup Commit Generator

Automatically generates fixup commits by analyzing staged changes and matching them to the correct ancestor commits. A Rust port of Facebook’s hg absorb that eliminates manual interactive rebasing for review feedback.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install git-absorb-automatic-fixup-commit-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

git-absorb is a command-line tool that automates one of the most tedious parts of maintaining clean Git history: folding review feedback into the right commits. Originally ported from Facebook’s hg absorb for Mercurial, this Rust implementation brings the same workflow to Git.
How It Works
When you have a feature branch with multiple commits and need to apply fixes from code review, git-absorb examines your staged changes and automatically determines which existing commits each change belongs to. It then creates fixup! commits targeting the correct ancestors. With the –and-rebase flag, these fixup commits are immediately squashed into their targets via autosquash rebase.
The algorithm identifies which commits are safe to modify by analyzing line-level changes. For each staged hunk, it traces which commit last modified those lines and creates a corresponding fixup commit. If a change cannot be unambiguously attributed to a single commit, it remains staged for manual handling.
Typical Workflow
After receiving code review feedback, you make your fixes, stage them with git add, and run git absorb –and-rebase. The tool handles the rest. Alternatively, you can run git absorb without –and-rebase to inspect the generated fixup commits before running git rebase -i –autosquash yourself. This two-step approach gives you full control over history rewriting.
Integration Points
git-absorb installs as a standard git subcommand, so it is invoked as git absorb from any Git repository. It is available through Homebrew, apt, pacman, dnf, cargo install, and most major package managers. The tool uses a bundled libgit2 so no external Git library installation is required. It works with any Git hosting platform and integrates into existing pull request workflows on GitHub, GitLab, or Bitbucket.
Output
git-absorb outputs the list of fixup commits it creates, showing which original commit each fixup targets. When run with –and-rebase, it also performs the interactive rebase automatically, producing a clean commit history with the fixes folded in.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-absorb-automatic-fixup-commit-generator/)
