---
title: "Orchestrate stacked Git branches, sync safely, and ship pull requests in order"
description: "This ASE entry is built around Git Town, the open source Git workflow tool maintained at git-town/git-town. The agent behavior here is specific: it manages a stack of related branches in a repeatable way, keeps them synchronized with the main branch, helps move work forward branch by branch, and reduces the chance of a human or agent wrecking a repository with a messy sequence of raw Git commands. In practice that means using Git Town for tasks like syncing feature branches before review, rebasing child branches after a parent branch changes, shipping merged work in the right order, and cleaning up branches that no longer need to exist.\nUse this when the job is multi-branch workflow orchestration, especially in repositories that use stacked pull requests or long-running feature branches. It is a better fit than using Git manually when an agent needs to perform the same safe branch choreography over and over, produce predictable outcomes, and avoid hand-written command sequences that vary from run to run. It is also a good fit for CI-adjacent repository automation, release prep, or assistant-driven maintenance sessions where branch order matters.\nThe boundary is important: this is not a generic Git client listing, not a hosting platform entry, and not a broad developer toolkit card. The scope is branch-stack operations and pull request shipping workflows only. Integration points include the Git CLI, local repository automation, developer shells, and pull request flows on platforms such as GitHub, GitLab, Bitbucket, and Gitea, all of which are documented upstream by Git Town itself."
verification: security_reviewed
source: "https://github.com/git-town/git-town"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "git-town/git-town"
  github_stars: 3143
---

# Orchestrate stacked Git branches, sync safely, and ship pull requests in order

This ASE entry is built around Git Town, the open source Git workflow tool maintained at git-town/git-town. The agent behavior here is specific: it manages a stack of related branches in a repeatable way, keeps them synchronized with the main branch, helps move work forward branch by branch, and reduces the chance of a human or agent wrecking a repository with a messy sequence of raw Git commands. In practice that means using Git Town for tasks like syncing feature branches before review, rebasing child branches after a parent branch changes, shipping merged work in the right order, and cleaning up branches that no longer need to exist.
Use this when the job is multi-branch workflow orchestration, especially in repositories that use stacked pull requests or long-running feature branches. It is a better fit than using Git manually when an agent needs to perform the same safe branch choreography over and over, produce predictable outcomes, and avoid hand-written command sequences that vary from run to run. It is also a good fit for CI-adjacent repository automation, release prep, or assistant-driven maintenance sessions where branch order matters.
The boundary is important: this is not a generic Git client listing, not a hosting platform entry, and not a broad developer toolkit card. The scope is branch-stack operations and pull request shipping workflows only. Integration points include the Git CLI, local repository automation, developer shells, and pull request flows on platforms such as GitHub, GitLab, Bitbucket, and Gitea, all of which are documented upstream by Git Town itself.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/orchestrate-stacked-git-branches-sync-safely-and-ship-pull-requests-in-order
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/orchestrate-stacked-git-branches-sync-safely-and-ship-pull-requests-in-order` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-stacked-git-branches-sync-safely-and-ship-pull-requests-in-order/)
