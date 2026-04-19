---
title: "git-absorb Automatic Fixup Commit Generator"
description: "git-absorb is a command-line tool that automates one of the most tedious parts of maintaining clean Git history: folding review feedback into the right commits. Originally ported from Facebook&#8217;s hg absorb for Mercurial, this Rust implementation brings the same workflow to Git. How It Works When you have a feature branch with multiple commits and need to apply fixes from code review, git-absorb examines your staged changes and automatically determines which existing commits each change belongs to. It then creates fixup! commits targeting the correct ancestors. With the &#8211;and-rebase flag, these fixup commits are immediately squashed into their targets via autosquash rebase. The algorithm identifies which commits are safe to modify by analyzing line-level changes. For each staged hunk, it traces which commit last modified those lines and creates a corresponding fixup commit. If a change cannot be unambiguously attributed to a single commit, it remains staged for manual handling. Typical Workflow After receiving code review feedback, you make your fixes, stage them with git add, and run git absorb &#8211;and-rebase. The tool handles the rest. Alternatively, you can run git absorb without &#8211;and-rebase to inspect the generated fixup commits before running git rebase -i &#8211;autosquash yourself. This two-step approach gives you full control over history rewriting. Integration Points git-absorb installs as a standard git subcommand, so it is invoked as git absorb from any Git repository. It is available through Homebrew, apt, pacman, dnf, cargo install, and most major package managers. The tool uses a bundled libgit2 so no external Git library installation is required. It works with any Git hosting platform and integrates into existing pull request workflows on GitHub, GitLab, or Bitbucket. Output git-absorb outputs the list of fixup commits it creates, showing which original commit each fixup targets. When run with &#8211;and-rebase, it also performs the interactive rebase automatically, producing a clean commit history with the fixes folded in."
source: "https://github.com/tummychow/git-absorb"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "tummychow/git-absorb"
  github_stars: 5455
---

# git-absorb Automatic Fixup Commit Generator

git-absorb is a command-line tool that automates one of the most tedious parts of maintaining clean Git history: folding review feedback into the right commits. Originally ported from Facebook&#8217;s hg absorb for Mercurial, this Rust implementation brings the same workflow to Git. How It Works When you have a feature branch with multiple commits and need to apply fixes from code review, git-absorb examines your staged changes and automatically determines which existing commits each change belongs to. It then creates fixup! commits targeting the correct ancestors. With the &#8211;and-rebase flag, these fixup commits are immediately squashed into their targets via autosquash rebase. The algorithm identifies which commits are safe to modify by analyzing line-level changes. For each staged hunk, it traces which commit last modified those lines and creates a corresponding fixup commit. If a change cannot be unambiguously attributed to a single commit, it remains staged for manual handling. Typical Workflow After receiving code review feedback, you make your fixes, stage them with git add, and run git absorb &#8211;and-rebase. The tool handles the rest. Alternatively, you can run git absorb without &#8211;and-rebase to inspect the generated fixup commits before running git rebase -i &#8211;autosquash yourself. This two-step approach gives you full control over history rewriting. Integration Points git-absorb installs as a standard git subcommand, so it is invoked as git absorb from any Git repository. It is available through Homebrew, apt, pacman, dnf, cargo install, and most major package managers. The tool uses a bundled libgit2 so no external Git library installation is required. It works with any Git hosting platform and integrates into existing pull request workflows on GitHub, GitLab, or Bitbucket. Output git-absorb outputs the list of fixup commits it creates, showing which original commit each fixup targets. When run with &#8211;and-rebase, it also performs the interactive rebase automatically, producing a clean commit history with the fixes folded in.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-absorb-automatic-fixup-commit-generator/)
