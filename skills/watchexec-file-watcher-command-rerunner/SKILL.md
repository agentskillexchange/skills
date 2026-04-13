---
title: "watchexec File Watcher and Command Re-Runner"
description: "watchexec is a standalone file-watching tool written in Rust that automatically executes commands when it detects file modifications. It respects .gitignore rules, coalesces rapid filesystem events, and works cross-platform without requiring any language runtime."
verification: "security_reviewed"
source: "https://github.com/watchexec/watchexec"
category: ["Developer Tools"]
framework: ["Custom Agents"]
tool_ecosystem:
  github_repo: "watchexec/watchexec"
  github_stars: 6882
---

# watchexec File Watcher and Command Re-Runner

watchexec is a standalone file-watching tool written in Rust that automatically executes commands when it detects file modifications. It respects .gitignore rules, coalesces rapid filesystem events, and works cross-platform without requiring any language runtime.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watchexec-file-watcher-command-rerunner/)
