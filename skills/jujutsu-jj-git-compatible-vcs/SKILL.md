---
title: Jujutsu Git-Compatible Version Control System
description: Jujutsu (jj) is a modern version control system designed from the ground
  up to simplify and improve upon Git workflow model while maintaining full Git compatibility.
  With over 27,000 stars on GitHub and active daily development, it represents the
  most significant evolution in version control tooling since Git itself. The core
  innovation of Jujutsu is its treatment of the working copy as a commit. Every change
  you make to files is automatically recorded as a normal commit and amended on subsequent
  changes. This eliminates the need for Git staging area and stash commands entirely.
  The data model is simpler since commits are the only visible object, which means
  fewer commands to learn and fewer opportunities for mistakes. Jujutsu introduces
  first-class conflict tracking, treating conflicts as objects in the version control
  graph rather than just textual markers. When you resolve a conflict in one commit,
  that resolution automatically propagates to all descendant commits. Combined with
  automatic rebasing where every descendant is rebased when you modify a commit, this
  makes patch-based and stacked-diff workflows dramatically easier than in Git. The
  operation log is another standout feature. Jujutsu records every operation performed
  on the repository including commits, pulls, pushes, and rebases, creating a complete
  audit trail. This makes it trivial to undo mistakes, debug repository state, and
  answer questions about how the repository reached its current state. The revset
  query language, inspired by Mercurial, provides powerful composable expressions
  for selecting commits. Because Jujutsu uses Git repositories as its storage backend,
  it works with GitHub, GitLab, and any Git forge. An AI agent can use jj to manage
  complex branching workflows, rebase stacks of changes, and resolve conflicts programmatically,
  all with simpler commands than equivalent Git operations. Installation is available
  via cargo, brew, and platform packages.
verification: security_reviewed
source: https://github.com/jj-vcs/jj
category:
- Developer Tools
framework:
- OpenClaw
tool_ecosystem:
  github_repo: jj-vcs/jj
  github_stars: 27472
---

# Jujutsu Git-Compatible Version Control System

Jujutsu (jj) is a modern version control system designed from the ground up to simplify and improve upon Git workflow model while maintaining full Git compatibility. With over 27,000 stars on GitHub and active daily development, it represents the most significant evolution in version control tooling since Git itself. The core innovation of Jujutsu is its treatment of the working copy as a commit. Every change you make to files is automatically recorded as a normal commit and amended on subsequent changes. This eliminates the need for Git staging area and stash commands entirely. The data model is simpler since commits are the only visible object, which means fewer commands to learn and fewer opportunities for mistakes. Jujutsu introduces first-class conflict tracking, treating conflicts as objects in the version control graph rather than just textual markers. When you resolve a conflict in one commit, that resolution automatically propagates to all descendant commits. Combined with automatic rebasing where every descendant is rebased when you modify a commit, this makes patch-based and stacked-diff workflows dramatically easier than in Git. The operation log is another standout feature. Jujutsu records every operation performed on the repository including commits, pulls, pushes, and rebases, creating a complete audit trail. This makes it trivial to undo mistakes, debug repository state, and answer questions about how the repository reached its current state. The revset query language, inspired by Mercurial, provides powerful composable expressions for selecting commits. Because Jujutsu uses Git repositories as its storage backend, it works with GitHub, GitLab, and any Git forge. An AI agent can use jj to manage complex branching workflows, rebase stacks of changes, and resolve conflicts programmatically, all with simpler commands than equivalent Git operations. Installation is available via cargo, brew, and platform packages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jujutsu-jj-git-compatible-vcs/)
