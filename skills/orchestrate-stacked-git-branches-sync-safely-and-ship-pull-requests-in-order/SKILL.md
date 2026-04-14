---
title: "Orchestrate stacked Git branches, sync safely, and ship pull requests in order"
description: "Uses Git Town to keep a branch stack healthy by syncing with the main branch, rebasing dependent branches in order, opening or updating pull requests, and cleaning up after merge. Best when an agent needs repeatable multi-branch workflow control instead of improvising long git command chains."
verification: security_reviewed
source: "https://github.com/git-town/git-town"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
---

# Orchestrate stacked Git branches, sync safely, and ship pull requests in order

This ASE entry is built around Git Town, the open source Git workflow tool maintained at git-town/git-town. The agent behavior here is specific: it manages a stack of related branches in a repeatable way, keeps them synchronized with the main branch, helps move work forward branch by branch, and reduces the chance of a human or agent wrecking a repository with a messy sequence of raw Git commands. In practice that means using Git Town for tasks like syncing feature branches before review, rebasing child branches after a parent branch changes, shipping merged work in the right order, and cleaning up branches that no longer need to exist.

Use this when the job is multi-branch workflow orchestration, especially in repositories that use stacked pull requests or long-running feature branches. It is a better fit than using Git manually when an agent needs to perform the same safe branch choreography over and over, produce predictable outcomes, and avoid hand-written command sequences that vary from run to run. It is also a good fit for CI-adjacent repository automation, release prep, or assistant-driven maintenance sessions where branch order matters.

The boundary is important: this is not a generic Git client listing, not a hosting platform entry, and not a broad developer toolkit card. The scope is branch-stack operations and pull request shipping workflows only. Integration points include the Git CLI, local repository automation, developer shells, and pull request flows on platforms such as GitHub, GitLab, Bitbucket, and Gitea, all of which are documented upstream by Git Town itself.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-stacked-git-branches-sync-safely-and-ship-pull-requests-in-order/)
